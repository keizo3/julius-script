#!/bin/sh

ALSADEV="plughw:0,0" /home/pi/dev/julius/julius/julius -C /home/pi/dev/dictation-kit/mybot.jconf &
sleep 2
/home/pi/dev/julius-script/remote_robo.py &

exit 0
