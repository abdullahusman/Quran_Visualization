from HTMLParser import HTMLParser
import re

#the output of the script we want a json generated from an html file


with open('html/1.htm', 'r') as f:
  read_data = f.read()

#get the title of the surah
m=re.search('<h1>(.+)</h1>', read_data)
title= m.group(1)

print title

pattern = re.compile(r'<A NAME="(.+)"><b>.+</A>(.+)')
#get he ayas
m2=re.search(pattern, read_data)

for (number, ayah) in re.findall(pattern, read_data):
  print number
  print ayah
