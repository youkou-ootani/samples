import requests

url = "http://zip.cgis.biz/xml/zip.php"
payload = {"zn": "3590045"}
r = requests.get(url, params=payload)
r.text

url = "http://zip.cgis.biz/csv/zip.php"
r = requests.get(url, params=payload)
r.text
