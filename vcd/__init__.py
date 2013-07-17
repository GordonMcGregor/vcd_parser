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


   Module initialization file

'''

__all__ = ['parser', 'watcher', 'tracker', 'v2d']

def v2d(value):

   format, data = value
   if format == 'b':
      return eval('0b' + data)
   if format == 'h':
      return eval ('0x' + data)
   return eval(data)
   