import requests
r = requests.get('https://www.dcard.tw/api/post/all/176324986')
print('Article loading complete.')

qq = r.json()

print(type(qq)) # Should be a 'list'
print qq['version'][0]['content']
