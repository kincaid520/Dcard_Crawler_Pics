import requests
import re
import Image

requests.packages.urllib3.disable_warnings()

SAVETOFILE = False
POPULARLINK='https://www.dcard.tw/api/forum/%s/%d/popular'
NORMALLINK='https://www.dcard.tw/api/forum/%s/%d'
LINK=NORMALLINK
PAGES=3
FORUM="all"

post_id=[]
post_link=[]

def get(PAGES=PAGES, FORUM=FORUM, POPULAR=False):
	if POPULAR:
		LINK = POPULARLINK
	for page in range( 1, int(PAGES)+1 ):
		print("Scaning page %d"%page)
		r = requests.get( LINK%(FORUM, page) )
		article = r.json()


		"""# See the components
		for post in article:
			for typ in post:
				print(typ)
		"""

		# find every id of article, store to post_id[] 
		for post in article:
			post_id.append(post['id'])
	

		# find every link in every article
		for id in post_id:
			print(">Searching in ID %d"%id)
			r = requests.get('https://www.dcard.tw/api/post/all/'+str(id))# this website is fixed
			article = r.json()
			content =  article['version'][0]['content'] # looking into the content
			p = re.compile(ur'(http:\/\/i?.?imgur.com\/[\w]+)')
			result= re.findall(p,content)
			for i in result:
				print("  Capturing picture from %s"%i)
				second_r = requests.get(i)
				second_content = second_r.content
				second_p = re.compile(ur'(http:\/\/i?.?imgur.com\/\w+\.[jpeng]+)')
				res_pic = re.findall(second_p, second_content)
				post_link.append(res_pic[0])

		# save to file
		if SAVETOFILE:
			file=open('output','w')
			for each in post_link:
				file.write(str(each)+'\n')
			file.close()

	return post_link

