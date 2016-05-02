import requests
import re
import Image

requests.packages.urllib3.disable_warnings()

SAVETOFILE = False
POPULARLINK='https://www.dcard.tw/api/forum/all/%d/popular'
LINK='https://www.dcard.tw/api/forum/all/%d'
PAGES=1

post_id=[]
post_link=[]

def get():
	for page in range(1,PAGES+1):
		r = requests.get(POPULARLINK%(page))
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
			r = requests.get('https://www.dcard.tw/api/post/all/'+str(id))
			article = r.json()
			content =  article['version'][0]['content'] # looking into the content
			p = re.compile(ur'(http:\/\/i?.?imgur.com\/[\w]+)')
			result= re.findall(p,content)
			for i in result:
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

