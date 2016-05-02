from sys import argv
import crawler
import re

WEBPICWIDTH="320"
page = 1
forum = 'all'
popular = False
inp=""

for each in argv:
	inp = inp+each+' '

p = re.compile(ur' (\d+)')
temp = re.findall(p, inp)
if not temp==[]:
	page = temp[0]

p = re.compile(ur' (popular)')
temp = re.findall(p, inp)
if not temp==[]:
	popular = True

p = re.compile(ur' ([a-zA-Z]+)')
temp = re.findall(p, inp)
if not temp==[]:
	for tag in temp:
		if not tag=='popular':
			forum = tag
			break

links = crawler.get(page, forum, popular)

f = open("output.html","w")
for link in links:
	f.write("<img width=\"%s\" src=\"%s\">"%(WEBPICWIDTH,link))	
