#!/bin/bash
#
# Copyright 2014 Allister Banks (see end for license)
#
# This simply echo's all the sparkle-using apps it finds to stdout

declare -xa APPINFOS=('/Applications/*/*.app/Contents/Info.plist' '/Applications/*.app/Contents/Info.plist' ~/Downloads'/*.app/Contents/Info.plist')
for infolist in ${APPINFOS[@]}; do
  declare -x URL=`/usr/libexec/PlistBuddy -c "Print :SUFeedURL" "$infolist" 2>/dev/null`
  if [[ `grep -c SUFeedURL "$infolist"` != 0 ]]; then
    echo -e "$infolist""\n"$URL
  fi
done

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.