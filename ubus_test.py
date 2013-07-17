from vcd import *

class UbusWatcher(watcher.VcdWatcher):

	in_reset = False
	signals = ('sig_request', 'sig_grant', 'sig_addr', 'sig_size', 
		       'sig_read', 'sig_write', 'sig_start', 'sig_bip', 
	           'sig_data', 'sig_data_out', 'sig_wait', 'sig_error') 

	def __init__(self, hierarchy = None):
		self.set_hierarchy(hierarchy)
		self.add_signals()

	def add_signals(self):
		self.add_sensitive('sig_clock')
		self.add_sensitive('sig_reset')
		for signal in self.signals:
			self.add_watching(signal)

	def update(self, changes, vcd):

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
		print '+', '-'*40, '+'
		for change in changes:
			print '\t', vcd.get_xmr(change), changes[change]


vcd = parser.VcdParser()

watcher = UbusWatcher('ubus_tb_top.vif')
vcd.register_watcher(watcher)

with open('ubus.vcd') as vcd_file:
	vcd.parse(vcd_file)


