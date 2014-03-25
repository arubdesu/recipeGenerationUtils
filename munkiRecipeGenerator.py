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
    <string>Downloads latest version of %producto% and imports it into a Munki repo.</string>
    <key>Identifier</key>
    <string>com.github.autopkg.munki.%producto%</string>
    <key>Input</key>
    <dict>
        <key>NAME</key>
        <string>%producto%</string>
        <key>MUNKI_REPO_SUBDIR</key>
        <string>apps</string>
        <key>pkginfo</key>
        <dict>
            <key>catalogs</key>
            <array>
                <string>testing</string>
            </array>
            <key>description</key>
            <string>%descript%</string>
            <key>display_name</key>
            <string>%producto%</string>
            <key>name</key>
            <string>%NAME%</string>
            <key>unattended_install</key>
            <true/>
        </dict>
    </dict>
    <key>MinimumVersion</key>
    <string>0.2.0</string>
    <key>ParentRecipe</key>
    <string>com.github.autopkg.download.%producto%</string>
    <key>Process</key>
    <array>
        <dict>
            <key>Processor</key>
            <string>MunkiPkginfoMerger</string>
        </dict>
        <dict>
            <key>Arguments</key>
            <dict>
                <key>pkg_path</key>
                <string>%pathname%</string>
                <key>repo_subdirectory</key>
                <string>%MUNKI_REPO_SUBDIR%</string>
            </dict>
            <key>Processor</key>
            <string>MunkiImporter</string>
        </dict>
    </array>
</dict>
</plist>
"""

products = {
     "HipChat" : """HipChat is hosted group chat and IM for companies and teams. Supercharge real-time collaboration with persistent chat rooms, file sharing, and chat history.""",
     "Bartender" : """Bartender lets you organize your Menu Bar Apps, by hiding them, rearranging them, or moving them to the Bartenders Bar. You can display the full menu bar, set options to have Menu Bar Apps show in the menu bar when they are updating, or have them always visible in the Bartenders Bar. There are loads of ways to configure Bartender to perform as you wish. Give it a go and find out.""",
     "Fake" : """Fake is a new browser for Mac OS X that makes web automation simple. Fake allows you to drag discrete browser Actions into a graphical Workflow that can be run again and again without human interaction. The Fake Workflows you create can be saved, reopened, and shared. Inspired by Apple's Automator application, Fake looks like a combination of Safari and Automator that allows you to run (and re-run) "fake" interactions with the web.""",
     "Fluid" : """Web applications like Gmail, Facebook, Campfire and Pandora are becoming more and more like desktop applications every day. Running each of these web apps in a separate tab in your browser can be a real pain. Fluid lets you create a Real Mac App (or "Fluid App") out of any website or web application, effectively turning your favorite web apps into OS X desktop apps.""",
     "ClipMenu" : """ClipMenu can manage clipboard history. You can record 8 clipboard types, from plain text to image.""",
     "Cinch" : """Cinch allows you to precisely resize a window simply by dragging to the left, right, or top screen edge.""",
     "Isolator" : """Isolator is a small menu bar application that helps you concentrate. When you're working on a document, and don't want to be distracted, turn on Isolator. It will cover up your desktop and all the icons on it, as well as the windows of all your other applications, so you can concentrate on the task in hand.""",
     "iTeleport" : """It's magic""",
     "Limechat" : """Limechat is an IRC client""",
     "Mactracker" : """Mactracker provides detailed information on every Apple Macintosh computer ever made, including items such as processor speed, memory, optical drives, graphic cards, supported OS versions, and expansion options. Also included is information on Apple mice, keyboards, displays, printers, scanners, speakers, cameras, iPod, Apple TV, iPhone, iPad, Wi-Fi products, Newton, iOS, Mac OS, and OS X versions.""",
     "Pacifist" : """Pacifist is a shareware application that opens Mac OS X .pkg package files, .dmg disk images, and .zip, .tar, .tar.gz, .tar.bz2, and .xar archives and allows you to extract individual files and folders out of them.""",
     "LingonX" : """LingonX is an easy to use yet powerful utility that runs things automatically on your Mac""",
     "MarsEdit" : """MarsEdit is a weblog editor for Mac OS X. It supports posting to many popular blogging services, such as Blogger, Movable Type, Tumblr and WordPress.""",
     "Reflector" : """Reflector lets you AirPlay mirror your iPhone or iPad to any Mac or PC, wirelessly. Play games, watch movies, demo apps or present to your computer from your iOS device.""",
     "ScreenSharingMenulet" : """ScreenSharing provides easy access to Screen Sharing from the menu bar. Local and Back to My Mac hosts are automatically detected with Bonjour.""",
}
filename = "/tmp/scratch"
for product_name, descript in products.items():
    new_string = template_string.replace("%producto%", product_name)
    new2_string = new_string.replace("%descript%", descript)
    target = open(filename, 'w')
    target.write(new2_string)
    target.close()
    os.rename(filename, "/tmp/" + product_name + ".munki.recipe")

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