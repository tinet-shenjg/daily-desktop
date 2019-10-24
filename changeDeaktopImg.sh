#!/bin/sh
localpath="/Users/$USER/dev/tool/desk/background.jpg"
osascript -e "tell application \"Finder\" to set desktop picture to POSIX file \"$localpath\""

