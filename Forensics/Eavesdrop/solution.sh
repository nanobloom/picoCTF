#!/usr/bin/zsh

echo $(tshark -r capture.flag.pcap -Y 'tcp.stream eq 2 && data' -e data.data -Tfields) | xxd -r -p > file.des3

$(tshark -r capture.flag.pcap -Y 'frame.number == 18' -e data.data -Tfields | xxd -r -p | sed 's/\*sigh\*\ //') &>/dev/null

cat file.txt