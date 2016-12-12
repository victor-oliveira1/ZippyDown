#!/bin/bash
# Sintaxe: ./zippyshare_downloader.sh link_zippyshare
# victor.oliveira@gmx.com

site=$(curl -s $1)
var_a=$(echo "$site"|grep -Eo var\ a\ \=\ [0-9]\+|cut -d ' ' -f4)
var_b=$(echo "$site"|grep -Eo var\ b\ \=\ [0-9]\+|cut -d ' ' -f4)
var_a_div=$(($var_a/3))
var_final=$(($var_a+$var_a_div%$var_b))

url=$(echo $1|sed 's\http://\\g'|cut -d '/' -f1)
id=$(echo $1|sed 's\http://\\g'|cut -d '/' -f3)
arq=$(echo "$site"|grep 'twitter:title'|cut -d '"' -f4)

echo "Baixando: $arq"

wget -q --show-progress "http://$url/d/$id/$var_final/$arq"
