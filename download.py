import urllib3, sys
http = urllib3.PoolManager()
r = http.request('GET', 'https://thomascaneday.com/')
htmlSource = r.data

print(htmlSource)
# while 1:
#     buf = htmlSource.read(2048)
#     if not len(buf):
#         break
#     sys.stdout.write(buf)