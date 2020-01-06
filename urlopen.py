from urllib.request import urlopen

r = urlopen('http://facebook.com')
#print(r.read())
print(r.headers)
print(r.status)
print(r.url)