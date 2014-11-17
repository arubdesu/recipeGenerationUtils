#!/usr/bin/env python
#
# Copyright 2014 Allister Banks (see end for license)
#
import sys, os
template_string = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Description</key>
    <string>Installs the current release version of %producto%.</string>
    <key>Identifier</key>
    <string>com.github.autopkg.install.%producto%</string>
    <key>Input</key>
    <dict>
    </dict>
    <key>MinimumVersion</key>
    <string>0.4.0</string>
    <key>ParentRecipe</key>
    <string>com.github.autopkg.pkg.%producto%</string>
    <key>Process</key>
    <array>
        <dict>
            <key>Processor</key>
            <string>Installer</string>
        </dict>
    </array>
</dict>
</plist>
"""

products = [
    "Bartender",
    "Fake",
    "Fluid",
    "Cinch",
    "iTeleport",
    "Limechat",
    "Mactracker",
    "MSLync",
    "OnCue2",
    "LingonX",
    "quickradar",
    "MarsEdit",
]

filename = "/tmp/scratch"
for product_name in products:
    new_string = template_string.replace("%producto%", product_name)
    target = open(filename, 'w')
    target.write(new_string)
    target.close()
    os.rename(filename, "/tmp/" + product_name + ".install.recipe")

print "Ding! Fries are done."

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
