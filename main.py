import requests
import re
requests.packages.urllib3.disable_warnings()

POPULARLINK='https://www.dcard.tw/api/forum/all/1/popular'
LINK='https://www.dcard.tw/api/forum/all/1'
post_id=[]
post_link=[]
r = requests.get(LINK)
article = r.json()


"""# See the components
for post in article:
	for typ in post:
		print(typ)
"""

# find every id of article, store to post_id[] 
for post in article:
	post_id.append(post['id'])
#print post_id

for id in post_id:
	r = requests.get('https://www.dcard.tw/api/post/all/'+str(id))
	article = r.json()
	content =  article['version'][0]['content']
	p = re.compile(ur'http:\/\/i?.?imgur.com\/([\w]+)')
	result= re.findall(p,content)
	for i in result:
		post_link.append(i)

# save to file
file=open('output','w')
for each in post_link:
	file.write("http://i.imgur.com/"+str(each)+'\n')
file.close()
quit( post_link)
