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
    <string>Downloads the current release version of %producto%.</string>
    <key>Identifier</key>
    <string>com.github.autopkg.download.%producto%</string>
    <key>Input</key>
    <dict>
        <key>NAME</key>
        <string>%producto%</string>
        <key>SPARKLE_FEED_URL</key>
        <string>%url%</string>
	</dict>
    <key>Process</key>
    <array>
        <dict>
            <key>Processor</key>
            <string>SparkleUpdateInfoProvider</string>
            <key>Arguments</key>
            <dict>
                <key>appcast_url</key>
                <string>%SPARKLE_FEED_URL%</string>
            </dict>
        </dict>
        <dict>
            <key>Processor</key>
            <string>URLDownloader</string>
            <key>Arguments</key>
            <dict>
                <key>filename</key>
                <string>%NAME%.zip</string>
            </dict>
        </dict>
        <dict>
            <key>Processor</key>
            <string>EndOfCheckPhase</string>
        </dict>
    </array>
</dict>
</plist>"""

products = {
  "Bartender" : "http://www.macbartender.com/updates/updates.php",
  "Fake" : "http://fakeapp.com/appcast/fake.rss",
  "Fluid" : "http://fluidapp.com/appcast/fluidapp.rss", 
   "Cinch" : "https://www.irradiatedsoftware.com/updates/profiles/cinch.php",
   "iTeleport" : "http://www.iteleportmobile.com/download/sparkle.xml",
   "Limechat" : "http://limechat.net/mac/appcast.xml",
   "Mactracker" : "http://update.mactracker.ca/appcast-b.xml",
   "Pacifist" : "http://www.charlessoft.com/cgi-bin/pacifist_sparkle.cgi",
   "LingonX" : "http://www.peterborgapps.com/updates/lingonx-appcast.xml",
   "MarsEdit" : "http://www.red-sweater.com/marsedit/appcast3.php",
   "ScreenSharingMenulet" : "http://www.klieme.com/Downloads/ScreenSharingMenulet/appcast.xml"}
filename = "/tmp/scratch"
for product_name, url in products.items():
    new_string = template_string.replace("%producto%", product_name)
    new2_string = new_string.replace("%url%", url)
    target = open(filename, 'w')
    target.write(new2_string)
    target.close()
    os.rename(filename, "/tmp/" + product_name + ".download.recipe")

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
