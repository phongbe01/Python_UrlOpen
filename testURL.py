import urllib.request
try:
	r = urllib.urlopen('http://facebook.com')

except Exception as e:
	print('error code', e.code)
	print('reason', e.reason)
	print('url', e.url)