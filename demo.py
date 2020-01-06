 import urllib.request
#  r = urlopen('http://python.org')
#  print(r)
#  print(r.read())
# r.status
# r.url
# r.getheaders()

# import requests
# r1 = requests.get('http://python.org')
# print(r1.text)

import urllib.error
try:
	r = urlopen('http://phong.com')
except Exception as e:
	print('error code', e.code)
	print('reason', e.reason)
	print('url', e.url)
