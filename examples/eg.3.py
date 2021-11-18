"""
@Description: How to use proxy and cookies
@Usage: 
@Author: xlomg
@Date: 2021/8/29 下午3:16
"""

import requests
from fatgoose3 import FatGoose
from fatgoose3.text import StopWordsChinese

g = FatGoose()
g.config.use_meta_language = False
g.config.target_language = 'zh'
g.config.stopwords_class = StopWordsChinese

url = "http://military.cntv.cn/2015/05/28/ARTI1432794380285200.shtml"
resp = requests.get(url)
resp.encoding = 'utf8'
news = g.extract(url=url, raw_html=resp.text)

print(f'news.title: %s\n' % news.title)
print(f'news.author: %s\n' % news.authors)
print(f'news.publish_date: %s\n' % news.publish_date)
print(f'news.cleaned_text: %s\n' % news.cleaned_text)
print(f'news.infos: %s\n' % news.infos)
g.close()
