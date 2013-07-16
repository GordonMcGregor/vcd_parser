VCD Parser
==========


A basic self contained VCD parser object

Walks through the definitions constructing the appropriate signal references.
Caches XMR paths if and when the signal value changes in the dump for future reference.
Needs some hooks for callbacks on signal changes and methods to allow sampling of a signal with an appropriate clock reference


Refer to IEEE SystemVerilog standard 1800-2009 for VCD details Section 21.7 Value Change Dump (VCD) files

Based on toggle count sample code from Donald 'Paddy' McCarthy
http://paddy3118.blogspot.com/2008/03/writing-vcd-to-toggle-count-generator.html


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

