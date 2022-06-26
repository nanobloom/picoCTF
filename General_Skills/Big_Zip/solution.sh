#!/usr/bin/zsh

unzip -qq big-zip-files.zip
grep -ro 'pico.\{0,50\}' ./big-zip-files --color=NEVER | cut -d ":" -f 2