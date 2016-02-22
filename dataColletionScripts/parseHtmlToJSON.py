import re
import json

#{chapter#: order}
order_dic = {96:1, 68:2, 73:3, 74:4, 1:5, 111:6, 81:7, 87:8, 92:9, 89:10,93:11,94:12, 103:13, 100:14, 108:15, 102:16, 107:17, 109:18, 105:19,113:20,114:21, 112:22, 53:23, 80:24, 97:25, 91:26, 85:27, 95:28, 106:29,101:30,75:31, 104:32, 77:33, 50:34, 90:35, 86:36, 54:37, 38:38, 7:39,72:40, 36:41,25:42, 35:43, 19:44, 20:45, 56:46, 26:47, 27:48, 28:49,17:50, 10:51, 11:52, 12:53, 15:54, 6:55, 37:56, 31:57, 34:58, 39:59, 40:60,41:61, 42:62, 43:63, 44:64, 45:65, 46:66, 51:67, 88:68, 18:69, 16:70,71:71, 14:72, 21:73, 23:74, 32:75, 52:76, 67:77, 69:78, 70:79, 78:80,79:81, 82:82, 84:83, 30:84, 29:85, 83:86, 2:87, 8:88, 3:89, 33:90, 60:91,4:92, 99:93, 57:94, 47:95, 13:96, 55:97, 76:98, 65:99, 98:100, 59:101,110:102, 24:103, 22:104, 63:105, 58:106, 49:107, 66:108, 62:109, 64:110,61:111, 48:112, 5:113, 9:114}

#the output of the script we want a json generated from an html file

for i in range(1,115):

  with open('html/'+str(i)+'.htm', 'r') as f:
    read_data = f.read()

  #get the title of the surah
  m=re.search('<h1>.*Surah ([0-9]+)\.(.+)</h1>', read_data, re.IGNORECASE | re.S)
  title= m.group(2)
  surah_number = m.group(1)
  print surah_number
  print title

  pattern = re.compile(r'<A.*NAME="(.+)">.+</A>(.+)', re.IGNORECASE)
  #get he ayas
  m2=re.search(pattern, read_data)

  number_of_ayas = 0
  ayahs_array = []
  for (number, ayah) in re.findall(pattern, read_data):
    clean_ayah=re.sub(r'<.{1,2}>|<font.+>','',ayah.strip('\r').replace('<fontcolor=\\"#000000\\">',"").replace("</BODY>","").replace("<font>","").replace("</font>","").replace("&quot;O",'').replace("&quot;",''))
    ayahs_array.append(clean_ayah)
    number_of_ayas = number_of_ayas + 1

  order = order_dic[int(surah_number)]
  if order<= 86:
    loc="makkah"
  else:
    loc="madinah"

  with open('json/'+str(i)+'.json', 'w') as outFile:
    json.dump({"chapter": surah_number,"name_of_chapter":title,"ayas":ayahs_array, "location":loc,"number_of_verses":number_of_ayas,"order_of_rev": order}, outFile)

