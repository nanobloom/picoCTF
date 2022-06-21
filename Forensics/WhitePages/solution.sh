#!/usr/bin/zsh

xxd -p whitepages.txt | tr -d '\n' | sed 's/e28083/0/g' | sed 's/20/1/g' | perl -lpe '$_=pack"B*",$_' | awk 'NR==6' | xargs