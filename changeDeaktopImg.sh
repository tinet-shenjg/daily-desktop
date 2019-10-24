#!/bin/sh
python3 desk.py
sleep 1  #等1秒后执行下一条
basedir=`cd $(dirname $0); pwd -P`
img="/background.jpg"
localpath=$basedir$img
echo $localpath
osascript -e "tell application \"Finder\" to set desktop picture to POSIX file \"$localpath\""

