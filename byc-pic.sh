#!/bin/bash
#半次元图片下载
#echo $1
url=$(xclip -o);
fname=${url##*/}
fname=~/bin/bcy-pics/$fname
wget $url -O $fname
title=$(grep  '<title>' "$fname")
title=$(echo "$title"|sed -n '/<title/s/<title>\(.*\)<\/title>/\1/p') 

backup_title=~/bin/bcy-pics/"$title"
(grep js-content-img-wrap -A 1 "$fname" |tail -1 ) >"$backup_title"


echo "$title"
vim -s /home/roya/bin/bcy-pic-ss "$backup_title"
wget -i "$backup_title" -P ~/Pictures/bcy/"$title"

rm "$fname"
