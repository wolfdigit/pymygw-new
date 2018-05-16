#!/bin/sh

if [ $# -ge 1 ]; then
	uci set wireless.sta.ssid=$1
	if [ $# -ge 2 ]; then
		uci set wireless.sta.key=$2
		uci set wireless.sta.encryption=psk2
	else
		uci set wireless.sta.encryption=none
	fi
	uci commit
	wifi
	wifi_mode
	sleep 8
fi

ifconfig | grep 'inet addr'
