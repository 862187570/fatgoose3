"""
@Description: How to customize your author rule and publish date rule
@Usage:
@Author: xlomg
@Date: 2021/8/29 下午2:45
"""
import requests
from fatgoose3 import FatGoose
from fatgoose3.configuration import PublishDatePattern, AuthorPattern


g = FatGoose()

g.config.known_publish_date_tags = PublishDatePattern(attr="class", value="pub_time", tag="span",
                                                           domain='www.globaltimes.cn',
                                                           time_format='%b %d, %Y %I:%M %p',
                                                           processor=lambda _: _.replace('Published: ', ''))

g.config.known_author_patterns = AuthorPattern(attr="class", value="byline", tag="span",
                                                    domain='www.globaltimes.cn',
                                                    processor=lambda _: _.replace('By', '').strip())

url = 'https://www.globaltimes.cn/page/202106/1227038.shtml'
resp = requests.get(url)
news = g.extract(url=url, raw_html=resp.text)

print(f'news.author: %s\n' % news.authors)
print(f'news.publish_date: %s\n' % news.publish_date)
g.close()

