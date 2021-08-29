"""
@Description: simplest example
@Usage: 
@Author: xlomg
@Date: 2021/8/29 下午2:33
"""

from fatgoose3 import FatGoose

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'

g = FatGoose()
g.config.http_headers = {'user-agent': UA}
news = g.extract(url='https://www.globaltimes.cn/page/202106/1227038.shtml')
print(f'news.title: %s\n' % news.title)
print(f'news.author: %s\n' % news.authors)
print(f'news.publish_date: %s\n' % news.publish_date)
print(f'news.cleaned_text: %s\n' % news.cleaned_text)
print(f'news.infos: %s\n' % news.infos)
g.close()
