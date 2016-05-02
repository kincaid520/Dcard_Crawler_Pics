import crawler
WEBPICWIDTH="320"
links = crawler.get()

f = open("output.html","w")

for link in links:
	f.write("<img width=\""+WEBPICWIDTH+"\" src=\""+link+"\">")

	
