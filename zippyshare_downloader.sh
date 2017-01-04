#!/bin/bash
# Sintaxe: ./zippyshare_downloader.sh link_zippyshare
# victor.oliveira@gmx.com

site=$(curl -s $1)

echo "$site"|grep 'File has expired and does not exist anymore on this server' &> /dev/null
if [ $? == 0 ]; then
	echo "Este arquivo foi apagado do Zippyshare."
	exit
fi

var_a=$(echo "$site"|grep -Eo var\ a\ \=\ [0-9]\+|cut -d ' ' -f4); var_a=$(($var_a*$var_a*$var_a))
var_b=3
var_final=$(($var_a+$var_b))

url=$(echo $1|sed 's\http://\\g'|cut -d '/' -f1)
id=$(echo $1|sed 's\http://\\g'|cut -d '/' -f3)
arq=$(echo "$site"|grep 'twitter:title'|cut -d '"' -f4)
tam=$(echo "$site"|grep Size\:|cut -d\> -f4|cut -d\< -f1)

echo -e "Baixando: $arq\tTamanho: $tam"

wget -q --show-progress "http://$url/d/$id/$var_final/$arq"
