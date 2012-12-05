TidyHTML Plugin for Sublime Text 2
==================================

Cleanup and reindent a saved file with TidyHTML. No php, no webservice required.

Installation
------------

1. Open the Sublime Text 2 Packages folder

    - OS X: ~/Library/Application Support/Sublime Text 2/Packages/
    - Windows: %APPDATA%/Sublime Text 2/Packages/
    - Linux: ~/.Sublime Text 2/Packages/

2. clone this repo
3. edit the TidyHTML.sublime-settings (or even better a copy of this file on your User folder) according to your desired settings (see http://w3c.github.com/tidy-html5/quickref.html for more details)

Commands
--------

`TidyHTML`: Converts characters to their HTML entity


Dependencies
------------

Based on https://github.com/w3c/tidy-html5

- Windows: binary provided via http://tidybatchfiles.info/tidy.zip
- OSX: Require separate install for best results (for HTML5 compatibility)
