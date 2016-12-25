import httplib2
h = httplib2.Http()
resp, content = h.request("http://127.0.0.1:5001/audio")
print(content)
