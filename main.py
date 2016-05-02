import crawler

links = crawler.get()


f = open("output.html","w")

for link in links:
	f.write("<img src=\""+link+"\">")

	
