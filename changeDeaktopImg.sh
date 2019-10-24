#!/bin/sh
python3 desk.py
sleep 1  #等1秒后执行下一条
localpath="/Users/$USER/dev/tool/desk/background.jpg"
echo $localpath
osascript -e "tell application \"Finder\" to set desktop picture to POSIX file \"$localpath\""

