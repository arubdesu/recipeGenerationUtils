Recipe Generation Utils
=================

This is a set of python scripts which ease the process of mass-generating [autopkg](http://autopkg.github.io/autopkg/) recipes. Currently there isn't much flexibility to the type of software you'd want to import or ways of polling for updates(sparkle only), and interactive options aren't yet available, but hopefully planned. (Want to beat me to it? Fork away!)

Intended Usage
=================

Apps that use the Sparkle framework or appcast rss-style update URLs can be polled with the recipes generated, but currently there isn't flexibility to handle dmg's and zip's in the same pkg-recipe-generation script, so please split out your products accordingly. You can then next that download recipe in a munki or pkg recipe, and once a pkg recipe is generated a jss recipe can be generated as well. There are example products in the body of each script, so you'd modify those dicts accordingly to insert the info about your software.

Preliminary notes(more detailed info coming soon:)
- The munki script assumes you're adding software you'd classify as 'apps', so modify the ```MUNKI_REPO_SUBDIR``` key accordingly (or clean that up afterwards if you're doing various types in one pass)
- product IDs can be found in the application bundle, or you'd often check the ~/Library/Preferences folder for the [reverse domain](http://superuser.com/questions/200167/what-does-com-developer-application-mean) (<- stackoverflow thread on the subject) of the software