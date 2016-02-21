#!/bin/bash

COUNTTOTAL=114

for ((i=1; i<=$COUNTTOTAL; i++))
do
  curl "http://www.islam101.com/quran/yusufAli/QURAN/${i}.htm" -o "html/${i}.htm" 
done

