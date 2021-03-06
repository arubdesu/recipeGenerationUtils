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
	<string>Downloads the current release version of %producto% and builds a package.</string>
	<key>Identifier</key>
	<string>com.github.autopkg.pkg.%producto%</string>
	<key>Input</key>
	<dict>
		<key>NAME</key>
		<string>%producto%</string>
	</dict>
	<key>ParentRecipe</key>
	<string>com.github.autopkg.download.%producto%</string>
	<key>MinimumVersion</key>
	<string>0.2.0</string>
	<key>Process</key>
	<array>
		<dict>
			<key>Processor</key>
			<string>AppDmgVersioner</string>
			<key>Arguments</key>
			<dict>
				<key>dmg_path</key>
				<string>%pathname%</string>
			</dict>
		</dict>
		<dict>
			<key>Processor</key>
			<string>PkgRootCreator</string>
			<key>Arguments</key>
			<dict>
				<key>pkgroot</key>
				<string>%RECIPE_CACHE_DIR%/%NAME%</string>
				<key>pkgdirs</key>
				<dict>
					<key>Applications</key>
					<string>0775</string>
				</dict>
			</dict>
		</dict>
		<dict>
			<key>Processor</key>
			<string>Copier</string>
			<key>Arguments</key>
			<dict>
				<key>source_path</key>
				<string>%pathname%/%producto%.app</string>
				<key>destination_path</key>
				<string>%pkgroot%/Applications/%producto%.app</string>
			</dict>
		</dict>
		<dict>
			<key>Processor</key>
			<string>PkgCreator</string>
			<key>Arguments</key>
			<dict>
				<key>pkgname</key>
				<string>%NAME%-%version%</string>
				<key>pkg_request</key>
				<dict>
					<key>pkgdir</key>
					<string>%RECIPE_CACHE_DIR%</string>
					<key>id</key>
					<string>%id%</string>
					<key>options</key>
					<string>purge_ds_store</string>
					<key>chown</key>
					<array>
						<dict>
							<key>path</key>
							<string>Applications</string>
							<key>user</key>
							<string>root</string>
							<key>group</key>
							<string>admin</string>
						</dict>
					</array>
				</dict>
			</dict>
		</dict>
	</array>
</dict>
</plist>
"""

products = {
    "LibreOffice" : "org.libreoffice.script"}
filename = "/tmp/scratch"
for product_name, identifier in products.items():
    new_string = template_string.replace("%producto%", product_name)
    new2_string = new_string.replace("%id%", identifier)
    target = open(filename, 'w')
    target.write(new2_string)
    target.close()
    os.rename(filename, "/tmp/" + product_name + ".pkg.recipe")

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