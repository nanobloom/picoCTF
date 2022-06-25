#!/usr/bin/zsh

tshark -r shark2.pcapng -Y 'dns.qry.name matches "reddshrimpandherring.com$" && ip.dst == 18.217.1.57' -e dns.qry.name -T fields | cut -d '.' -f 1 | head -n 6 | tr -d '\n' | base64 -d