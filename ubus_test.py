#!python
'''
   Copyright  2013  Gordon McGregor

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.



  An example using the vcd parsing library. This parses VCD output from the UBUS
  example shipped with the UVM BCL

  This example can be extended to provide interleaved transaction recording, using
  UbusTrackers that exist for a transaction lifetime, or just extend the simple tracker 
  below to filter/ analyse a subset of signals within the VCD dump

'''

from vcd import *

class UbusWatcher(watcher.VcdWatcher):

	in_reset = False
	signals = ('sig_request', 'sig_grant', 'sig_addr', 'sig_size', 
		       'sig_read', 'sig_write', 'sig_start', 'sig_bip', 
	           'sig_data', 'sig_data_out', 'sig_wait', 'sig_error') 

	def __init__(self, hierarchy = None):
		# set the hierarchical path first, prior to adding signals
		# so they all get the correct prefix paths
		self.set_hierarchy(hierarchy)
		self.add_signals()

	def add_signals(self):
		# Signals in the 'sensitivty list' are automatically added to the watch list
		self.add_sensitive('sig_clock')
		self.add_sensitive('sig_reset')
		for signal in self.signals:
			self.add_watching(signal)

	def update(self, changes, vcd):
		# Called every time something in the 'sensitivity list' changes 
		# Doing effective posedge/ negedge checks here and reset/ clock behaviour filtering
		clock_id = self.get_id('sig_clock')
		reset_id = self.get_id('sig_reset')

		if reset_id in changes and changes[reset_id] == '1':
			print 'in RESET'
			self.in_reset = True
			return

		if reset_id in changes and changes[reset_id] == '0':
			print 'out of RESET'
			self.in_reset = False

		# Only update on rising clock edge (clock has changed and is 1)
		if clock_id in changes and changes[clock_id] == '1' and not self.in_reset:
			self.manage_trackers(changes, vcd)


	def start_tracker(self, changes, vcd):
		# Simple example - if we don't have a tracker, add one first time it is called
		if not len(self.trackers):
			return True


class UbusTracker(tracker.VcdTracker):

	def update(self, changes, vcd):
		print '+', '-'*40, '+'
		for change in changes:
			print '\t', vcd.get_xmr(change), changes[change]



# Create a parser object, attach a watcher within the hierarchy and start running
vcd = parser.VcdParser()

watcher = UbusWatcher('ubus_tb_top.vif')
watcher.set_tracker(UbusTracker)

vcd.register_watcher(watcher)


with open('ubus.vcd') as vcd_file:
	vcd.parse(vcd_file)


