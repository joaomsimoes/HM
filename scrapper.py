import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup


url = 'https://www2.hm.com/en_gb/men/shop-by-product/view-all.html?sort=stock&image-size=large&image=stillLife&offset=0&page-size=2414'
hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
req = urllib.request.Request(url, headers=hdr)
html = urlopen(req, timeout=5)

bs = BeautifulSoup(html, 'html.parser')

for i, image in enumerate(bs.find_all('img')[1:]):
    try:
        urllib.request.urlretrieve('https://'+image['data-src'][2:], f"F:/HM/images/images{i}.jpg")
    except:
        pass
