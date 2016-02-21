import re
import json

#the output of the script we want a json generated from an html file

for i in range(1,114):

  with open('html/'+str(i)+'.htm', 'r') as f:
    read_data = f.read()

  #get the title of the surah
  m=re.search('<h1>.+([0-9]+)\.(.+)</h1>', read_data, re.IGNORECASE)
  title= m.group(2)
  surah_number = m.group(1)
  print surah_number
  print title

  pattern = re.compile(r'<A NAME="(.+)"><b>.+</A>(.+)', re.IGNORECASE)
  #get he ayas
  m2=re.search(pattern, read_data)

  number_of_ayas = 0
  ayahs_array = []
  for (number, ayah) in re.findall(pattern, read_data):
    ayahs_array.append(ayah.strip('\r'))
    number_of_ayas = number_of_ayas + 1

  loc="makkah"
  order=1

  with open('json/'+str(i)+'.json', 'w') as outFile:
    json.dump({"chapter": surah_number,"name_of_chapter":title,"ayas":ayahs_array, "location":loc,"number_of_verses":number_of_ayas,"order_of_rev": order}, outFile)

