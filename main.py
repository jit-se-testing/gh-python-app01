import urllib3            # USED

http = urllib3.PoolManager()
resp = http.request("GET", "http://example.com")
print(resp.status)
