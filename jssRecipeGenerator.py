#!/usr/bin/env python
#
# Copyright 2013 Allister Banks
#
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
import sys, os
# template_string = """<?xml version="1.0" encoding="UTF-8"?><category><name>%producto%</name></category>"""
template_string = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>Description</key>
    <string>Uses parent pkg recipe to downloads latest %producto% and import it into the JSS.</string>
    <key>Identifier</key>
    <string>com.github.autopkg.jss.%producto%</string>
    <key>Input</key>
    <dict>
      <key>CATEGORY</key>
      <string>%NAME%</string>
      <key>SMART_GROUP</key>
      <string>LessThanMostRecent_%NAME%</string>
      <key>SELFSERVE_POLICY</key>
      <string>SelfServeLatest_%NAME%</string>
      <!--<key>ARB_GROUP_NAME</key><string>arbitrary</string>-->
    </dict>
    <key>MinimumVersion</key>
    <string>0.2.5</string>
    <key>ParentRecipe</key>
    <string>%id%</string>
    <key>Process</key>
    <array>
      <dict>
        <key>Arguments</key>
        <dict>
          <key>prod_name</key>
          <string>%NAME%</string>
          <key>category</key>
          <string>%NAME%</string>
          <key>smart_group</key>
          <string>%SMART_GROUP%</string>
          <key>selfserve_policy</key>
          <string>%SELFSERVE_POLICY%</string>
          <!--<key>arb_group_name</key><string>%ARB_GROUP_NAME%</string>-->
        </dict>
        <key>Processor</key>
        <string>JSSImporter</string>
      </dict>
    </array>
  </dict>
</plist>"""

products = {"Adium" : "com.github.autopkg.pkg.Adium",
    "AdobeAIR" : "com.github.autopkg.pkg.AdobeAIR", 
    "AdobeFlashPlayer" : "com.github.autopkg.pkg.FlashPlayerExtractPackage", 
    "AdobeReader" : "com.googlecode.autopkg.pkg.AdobeReader", 
    "AutoPkg" : "com.github.autopkg.autopkg", 
    "BBEdit" : "com.github.autopkg.pkg.BBEdit", 
    "TextWrangler" : "com.github.autopkg.pkg.TextWrangler", 
    "Cyberduck" : "com.github.autopkg.pkg.Cyberduck", 
    "GoogleChrome" : "com.github.autopkg.pkg.googlechrome",
    "Handbrake" : "com.github.autopkg.pkg.Handbrake",
    "Firefox" : "com.github.autopkg.pkg.Firefox_EN",
    "Thunderbird" : "com.github.autopkg.pkg.Thunderbird",
    "MSOffice2011Updates" : "com.github.autopkg.pkg.Office2011Updates",
    "OmniFocus" : "com.github.autopkg.pkg.omnifocus",
    "OmniGraffle" : "com.github.autopkg.pkg.omnigraffle",
    "OmniGraffle6" : "com.github.autopkg.pkg.omnigraffle6",
    "OmniGrafflePro" : "com.github.autopkg.pkg.omnigrafflepro",
    "OmniGraphSketcher" : "com.github.autopkg.pkg.omnigraphsketcher",
    "OmniOutliner": "com.github.autopkg.pkg.omnioutliner",
    "OmniOutlinerPro" :  "com.github.autopkg.pkg.omnioutlinerpro",
    "OmniPlan" : "com.github.autopkg.pkg.omniplan",
    "OracleJava7" : "com.github.autopkg.pkg.OracleJava7Versioned",
    "Skype" : "com.github.autopkg.pkg.Skype",
    "VLC" : "com.github.autopkg.pkg.VLC"}
#  "TheUnarchiver" : "com.github.autopkg.download.TheUnarchiver", "XQuartz" : "com.github.autopkg.download.xquartz"
filename = "/tmp/scratch"
for product_name, identifier in products.items():
    new_string = template_string.replace("%producto%", product_name)
    new2_string = new_string.replace("%id%", identifier)
    target = open(filename, 'w')
    target.write(new2_string)
    target.close()
    os.rename(filename, "/tmp/" + product_name + ".jss.recipe")

print "Ding! Fries are done."