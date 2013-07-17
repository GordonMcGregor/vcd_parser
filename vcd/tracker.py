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


VcdWatcher base class for a signal watcher object.

Provide a list of XMRs that the watcher is sensitive to (i.e., a clock to  sample on) 
and a list of signals to actually watch.

The VCD parser will call the watcher.update method when it sees a change to a signal 
on the sensitivity list and provide the changes to all watched signals.

Trackers are transaction recording finite statemachines. The watcher decides when to 
start a tracker (could be on every cycle/ update) and maintains a list of active trackers.

When the watcher is updated, it checks to see if it should start a new tracker and 
then updates all the currently active trackers, until they indicate that they have 
finished their transaction recording.c

'''
class VcdTracker(object):

	finished = False

	def update(self, changes, vcd):
		pass

