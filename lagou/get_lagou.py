import requests

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,en;q=0.7,en-US;q=0.3",
    "Connection": "keep-alive",
    "Referer": "https: //www.lagou.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0"
}

params = (
    ('labelWrods', ''),
    ('fromSearch', 'true'),
    ('suginput', ''),
)

s = requests.Session()
s.headers.update(headers)

res = s.get('https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88', params=params)

data = {
    'first': 'true',
    'pn': 1,
    'kd': '数据分析师'
}

new_headers = {
    'Origin': 'https://www.lagou.com',
    'X-Anit-Forge-Code': '0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput=',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Anit-Forge-Token': 'None',
}

r = s.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false', data=data, headers=new_headers)

print(r.text)