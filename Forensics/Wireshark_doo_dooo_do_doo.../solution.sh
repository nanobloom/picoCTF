#!/usr/bin/zsh

tshark -r shark1.pcapng -Y '(data-text-lines matches "[a-zA-Z0-9]{7}\{[a-zA-Z0-9_]{5,50}\}")' -e http.file_data -Tfields | tr 'A-Za-z' 'N-ZA-Mn-za-m' | head -c-3