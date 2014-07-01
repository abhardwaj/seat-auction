import httplib, urllib, json

def http_post(url, params, auth):
  conn = httplib.HTTPSConnection("www.google.com")
  headers = {"Content-type": "application/x-www-form-urlencoded",
      "Accept": "text/plain", "Authorization": "GoogleLogin auth="+auth}
  params = urllib.urlencode(params)
  conn.request("POST", url, params, headers)  
  res = conn.getresponse().read()
  return json.loads(res)
