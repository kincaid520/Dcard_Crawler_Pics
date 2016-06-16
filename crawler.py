import requests
import re

requests.packages.urllib3.disable_warnings()

SAVETOFILE = False
POSTLINK='https://www.dcard.tw/f/%s/p/%s'
#POPULARLINK='https://www.dcard.tw/_api/%sposts?popular=true'
#NORMALLINK='https://www.dcard.tw/_api/%sposts?popular=false'
APILINK='https://www.dcard.tw/_api/%sposts?'
PAGES=3
FORUM="all"

post_id=[]
post_link=[]

def get(PAGES=PAGES, FORUM=FORUM, POPULAR=False):
	#LINK=NORMALLINK
	if POPULAR:
		LINK = APILINK+"popular=true"
	else:
		LINK = APILINK+"popular=false"
	print( "Forum: %s, Popular: %s, Pages: %s" %(FORUM, POPULAR, PAGES) )

	#for page in range( 1, int(PAGES)+1 ):
	#	print("Scaning page %d"%page)
	#	r = requests.get( LINK%(FORUM, page) )
	#	article = r.json()

	## find all post id.
	if FORUM!="all":
		FORUM = "forums/"+FORUM+"/"
	else:
		FORUM = ""

	## page function
	for page in range( 1, int(PAGES)+1 ):
		print("Scaning page %d"%page)

		if page ==1:
			r = requests.get( LINK%(FORUM) )
		else:
			r = requests.get( LINK%(FORUM) + '&before=' + str(post_id[len(post_id)-1]) ) ##add the last id
		article = r.json()
	
		## check the api 
		#print(LINK%(FORUM))

		## See the components
		#for post in article:
		#	for typ in post:
		#		print(typ)

		## find every id of article, store to post_id[] 
		for post in article:
			post_id.append(post['id'])
	
	## find every link in every article
	for id in post_id:
		print(">Searching in ID %d"%id)
		r = requests.get('https://www.dcard.tw/_api/posts/'+str(id)+'?')# this website is fixed
		article = r.json()
		content =  article['content'] # looking into the content
		forumAlias = article['forumAlias'] # looking into the forumAlias
		p = re.compile(ur'(http:\/\/i?.?imgur.com\/[\w]+)')
		result= re.findall(p,content)
		for i in result:
			print("  Capturing picture from %s"%i)
			second_r = requests.get(i)
			second_content = second_r.content
			second_p = re.compile(ur'(http:\/\/i?.?imgur.com\/\w+\.[jpeng]+)')
			res_pic = re.findall(second_p, second_content)
			post_link.append([POSTLINK%(forumAlias, str(id)), res_pic[0]] )

	## save to file
	if SAVETOFILE:
		file=open('output','w')
		for each in post_link:
			file.write(str(each)+'\n')
		file.close()

	return post_link

