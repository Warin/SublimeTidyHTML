TidyHTML Plugin for Sublime Text 2
==================================

Cleanup and reindent a saved file with TidyHTML. No php, no webservice required.

Installation
------------

1. Open the Sublime Text 2 Packages folder
    - OS X: ~/Library/Application Support/Sublime Text 2/Packages/
    - Windows: %APPDATA%/Sublime Text 2/Packages/
    - Linux: ~/.Sublime Text 2/Packages/
2. clone this repo (folder name should be `SublimeTidyHTML£)
3. edit the TidyHTML.sublime-settings (or even better a copy of this file on your User folder) according to your desired settings (see http://w3c.github.com/tidy-html5/quickref.html for more details)


Commands
--------

### Via the Command Palette

1. `Ctrl (Win)|Command (OSX) + Shift + P` to open the Command Palette then 
2. type `TidyHTML` to convert characters to their HTML entity

### Via Keyboard Shortcut

- OSX: `Command + alt +h`
- Windows: `Ctrl + alt + h`


Dependencies
------------

Based on https://github.com/w3c/tidy-html5

- Windows: binary provided via http://tidybatchfiles.info/tidy.zip
- OSX: Require separate install for best results (for HTML5 compatibility)
