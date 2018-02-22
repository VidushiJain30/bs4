import requests

with requests.Session() as c:
	url='http://www.noobmovies.com/accounts/login/?next=/'
	USERNAME='test_user'
	PASSWORD='test123'
	c.get(url)
	csrftoken=c.cookies['csrftoken']
	login_data=dict(csrfmiddlewaretoken=csrftoken, username=USERNAME, password=PASSWORD, next='/')
	c.post(url, data=login_data,headers={"Referer": "http://www.noobmovies.com/"})
	page=c.get('http://www.noobmovies.com/user/profile/0/')
	print (page.content)
