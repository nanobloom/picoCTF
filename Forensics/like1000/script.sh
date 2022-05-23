#!/usr/bin/zsh

for i in {1000..1}
do
    f=$i.tar
    tar xf $f
    rm $f
    ((i = i - 1))
done

rm filler.txt
