"""
@Description: simplest example
@Usage: 
@Author: xlomg
@Date: 2021/8/29 下午2:33
"""
import requests
from fatgoose3 import FatGoose

g = FatGoose()
url = 'https://www.globaltimes.cn/page/202106/1227038.shtml'
resp = requests.get(url)
news = g.extract(url=url, raw_html=resp.text)

print(f'news.title: %s\n' % news.title)
print(f'news.author: %s\n' % news.authors)
print(f'news.publish_date: %s\n' % news.publish_date)
print(f'news.cleaned_text: %s\n' % news.cleaned_text)
print(f'news.infos: %s\n' % news.infos)
g.close()
