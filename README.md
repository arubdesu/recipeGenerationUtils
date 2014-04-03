Recipe Generation Utils
=================

This is a set of scripts which ease the process of finding compatible apps and then mass-generating [autopkg](http://autopkg.github.io/autopkg/) recipes. Currently there isn't much flexibility to the type of software compatible to download(currently only those that use the [Sparkle](http://sparkle.andymatuschak.org) framework), and interactive options aren't yet available, but may be applicable. (Want to show off more general-purpose recipes to generate? Fork away!)

Intended Usage
=================

Apps that use the Sparkle framework or appcast rss-style update URLs can be polled with the recipes generated, but currently there isn't flexibility to handle dmg's and zip's in the same pkg-recipe-generation script, so please split out your products accordingly. You can then nest that download recipe in a munki or pkg recipe. (And for those using JAMF's Casper, once a pkg recipe is generated, a jss recipe can be generated as well!) There are example products in the body of each script, so you'd modify those dicts accordingly to insert the info about your software.

Preliminary Usage Notes:
=================

- The munki script assumes you're adding software you'd classify as 'apps', so modify the ```MUNKI_REPO_SUBDIR``` key accordingly (or clean that up afterwards if you're doing various types in one pass)
- product IDs can be found in the application bundle, or you'd often check the ~/Library/Preferences folder for the [reverse domain](http://superuser.com/questions/200167/what-does-com-developer-application-mean) (<- stackoverflow thread on the subject) of the software

Comments/Questions/Ideas
=================

As with my other code, please share "ideas, patches, documentation, bug reports, or complaints..." ([source](https://github.com/logstash/logstash#contributing)) by either using [issues in this repo](https://github.com/arubdesu/recipeGenerationUtils/issues), or by contacting me in ##osx-server IRC(Allister) or on twitter, [@sacrilicious](https://twitter.com/Sacrilicious) or my email(shouldn't be too hard to find, try [the MacEnterprise list](http://www.macenterprise.org/mailing-list)).