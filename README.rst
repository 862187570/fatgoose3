FatGoose3
=========

经过优化的goose3通用网页提取器

安装
----

``pip install fatgoose3``

例1 最简单的例子
----------------

.. code:: python

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

结果

::

    news.title: Leading Chinese universities go all out for top students - Global Times

    news.author: Global Times

    news.publish_date: None

    news.cleaned_text: A teacher gives a high five to a student outside an examination point at a high school in Guangzhou, South China's Guangdong Province. A total of 10.78 million Chinese students across the country stepped into Gaokao examination rooms on Monday to take their final step toward college. Photo: VCG

    As this year's college entrance exam , the gaokao, enters the final chapter with the release of scores, China's top universities are beginning their most important contest of the year - recruiting the top talents -- and they are going all out to impress the best candidates.As of 6 pm on Thursday, 18 provincial-level regions had unveiled the undergraduate admission bar, signaling the beginning of the college admissions work. Top universities have sent admissions teams to each province to introduce their universities and attract more young talent.Many universities have designed beautifully crafted acceptance letters to attract candidates to apply. Nankai University even included two lotus seeds from Jiaxing, East China's Zhejiang Province, in its admissions letter to commemorate the centennial of the founding of the Communist Party of China (CPC). The First National Congress of CPC was held in Jiaxing in 1921.East China Normal University went with a promotional video consisting entirely of Chinese-style hand-drawn cartoons depicting the story of a child from birth to adulthood. The video shows the child entering East China Normal University and becoming a pillar of the country.The recruiting video of Lanzhou University is almost like a mini-movie, describing a student's four years in the university designing laser radars, and chasing dreams.But none of the other praise-winning videos were as attractive to netizens as the hardcore video from the National University of Defense Technology. The 27-second short clip contains not a word of dialogue, only a number of students wearing pilot uniforms soaring thousands of meters in the air, holding a sign that simply says "Welcome to apply."But to what extent candidates would change their application plans because of the university's publicity is uncertain, a high school teacher who has been teaching for more than 20 years, told the Global Times, because young people nowadays are "very thoughtful in choosing their universities and majors."Compared with previous generations, the 18-year-olds of recent years have significantly more of their own considerations, said the Shanghai-based teacher surnamed Wu."They are no longer just rushing to enroll in a school for its reputation or listening entirely to their parents or teachers," Wu said. "They gather information about colleges from various sources before they fill out their applications, and then consider a variety of factors such as their hobbies, prospects and needs.""When I fill out my application, I take into serious consideration what talents my country needs at the moment," a freshman-to-be surnamed Tian from Chaozhou, South China's Guangdong Province, told the Global Times."I hope to join the high-tech industry such as chips and help my country's scientific progress, so I have chosen basic science as my undergraduate major," Tian said. "Some of my classmates have applied for national defense and aerospace majors, all hoping to contribute their share."In 2020, China launched a new education plan to encourage elite students to study "basic" subjects to improve the country's science and technology capabilities.According to the Strong Base Plan released by the Ministry of Education last year, 36 leading Chinese universities -- including Peking, Tsinghua and Fudan -- will select outstanding applicants who are "willing to serve the country's significant strategic demands," including high-end chip production, artificial intelligence, new materials, and other subjects related to national security, as well as some humanities and social science fields that suffer from shortages of talent.Many of these subjects -- such as mathematics, physics, chemistry and biology -- are unpopular with students who prefer majors such as computer science and finance that will improve their earning potential.This plan is mainly designed to solve the current shortages of scientific researchers in basic disciplines in China, Xiong Bingqi, director of the 21st Century Education Research Institute in Beijing, told the Global Times.Those being admitted now will be key forces for China to realize national rejuvenation, and they will have to overcome all kinds of challenges."Fortunately, we have seen enough young people who have ambitions to be contributors," said Xiong.

    news.infos: {'meta': {'description': '', 'lang': None, 'keywords': '', 'favicon': '/images/gfavicon.ico', 'canonical': 'https://www.globaltimes.cn/page/202106/1227038.shtml', 'encoding': 'utf-8'}, 'image': None, 'domain': 'www.globaltimes.cn', 'title': 'Leading Chinese universities go all out for top students - Global Times', 'cleaned_text': 'A teacher gives a high five to a student outside an examination point at a high school in Guangzhou, South China\'s Guangdong Province. A total of 10.78 million Chinese students across the country stepped into Gaokao examination rooms on Monday to take their final step toward college. Photo: VCG\n\nAs this year\'s college entrance exam , the gaokao, enters the final chapter with the release of scores, China\'s top universities are beginning their most important contest of the year - recruiting the top talents -- and they are going all out to impress the best candidates.As of 6 pm on Thursday, 18 provincial-level regions had unveiled the undergraduate admission bar, signaling the beginning of the college admissions work. Top universities have sent admissions teams to each province to introduce their universities and attract more young talent.Many universities have designed beautifully crafted acceptance letters to attract candidates to apply. Nankai University even included two lotus seeds from Jiaxing, East China\'s Zhejiang Province, in its admissions letter to commemorate the centennial of the founding of the Communist Party of China (CPC). The First National Congress of CPC was held in Jiaxing in 1921.East China Normal University went with a promotional video consisting entirely of Chinese-style hand-drawn cartoons depicting the story of a child from birth to adulthood. The video shows the child entering East China Normal University and becoming a pillar of the country.The recruiting video of Lanzhou University is almost like a mini-movie, describing a student\'s four years in the university designing laser radars, and chasing dreams.But none of the other praise-winning videos were as attractive to netizens as the hardcore video from the National University of Defense Technology. The 27-second short clip contains not a word of dialogue, only a number of students wearing pilot uniforms soaring thousands of meters in the air, holding a sign that simply says "Welcome to apply."But to what extent candidates would change their application plans because of the university\'s publicity is uncertain, a high school teacher who has been teaching for more than 20 years, told the Global Times, because young people nowadays are "very thoughtful in choosing their universities and majors."Compared with previous generations, the 18-year-olds of recent years have significantly more of their own considerations, said the Shanghai-based teacher surnamed Wu."They are no longer just rushing to enroll in a school for its reputation or listening entirely to their parents or teachers," Wu said. "They gather information about colleges from various sources before they fill out their applications, and then consider a variety of factors such as their hobbies, prospects and needs.""When I fill out my application, I take into serious consideration what talents my country needs at the moment," a freshman-to-be surnamed Tian from Chaozhou, South China\'s Guangdong Province, told the Global Times."I hope to join the high-tech industry such as chips and help my country\'s scientific progress, so I have chosen basic science as my undergraduate major," Tian said. "Some of my classmates have applied for national defense and aerospace majors, all hoping to contribute their share."In 2020, China launched a new education plan to encourage elite students to study "basic" subjects to improve the country\'s science and technology capabilities.According to the Strong Base Plan released by the Ministry of Education last year, 36 leading Chinese universities -- including Peking, Tsinghua and Fudan -- will select outstanding applicants who are "willing to serve the country\'s significant strategic demands," including high-end chip production, artificial intelligence, new materials, and other subjects related to national security, as well as some humanities and social science fields that suffer from shortages of talent.Many of these subjects -- such as mathematics, physics, chemistry and biology -- are unpopular with students who prefer majors such as computer science and finance that will improve their earning potential.This plan is mainly designed to solve the current shortages of scientific researchers in basic disciplines in China, Xiong Bingqi, director of the 21st Century Education Research Institute in Beijing, told the Global Times.Those being admitted now will be key forces for China to realize national rejuvenation, and they will have to overcome all kinds of challenges."Fortunately, we have seen enough young people who have ambitions to be contributors," said Xiong.', 'opengraph': {}, 'tags': [], 'tweets': [], 'movies': [], 'links': ['https://www.globaltimes.cn/page/202106/1225653.shtml'], 'authors': 'Global Times', 'publish_date': None}

例2 如何针对网站做定制化处理
----------------------------

从例1可以看到文章发布时间并没有提取出来，作者提取的也不够准确，我们针对环球时报做定制化处理

.. code:: python

    from fatgoose3 import FatGoose
    from fatgoose3.configuration import PublishDatePattern, AuthorPattern

    UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'

    g = FatGoose()
    g.config.http_headers = {'user-agent': UA}
    g.config.known_publish_date_tags = PublishDatePattern(attr="class", value="pub_time", tag="span",
                                                               domain='www.globaltimes.cn',
                                                               time_format='%b %d, %Y %I:%M %p',
                                                               processor=lambda _: _.replace('Published: ', ''))

    g.config.known_author_patterns = AuthorPattern(attr="class", value="byline", tag="span",
                                                        domain='www.globaltimes.cn',
                                                        processor=lambda _: _.replace('By', '').strip())

    news = g.extract(url='https://www.globaltimes.cn/page/202106/1227038.shtml')

    print(f'news.author: %s\n' % news.authors)
    print(f'news.publish_date: %s\n' % news.publish_date)
    g.close()

结果

::

    news.author: Cui Fandi

    news.publish_date: 2021-06-24 21:21:00

常用设置
--------

fatgoose3如果没有从网页中提取到发布时间，也会尝试从URL中提取出文章时间，如果不希望从url中提取时间，可以设置，此设置默认为
``True``

.. code:: python

    g.config.fetch_pubdate_from_url = False

如果需要爬取国外网站，可以设置代理

.. code:: python

    proxies = {
        'http': '127.0.0.1:6789'
    }
    g.config.http_proxies = proxies

如果网站需要代理才能采集, 可以设置cookie

.. code:: python

    g.config.http_headers['cookie'] = 'your cookies'

例3 如何使用 ``proxy`` 和 ``cookie``
------------------------------------

.. code:: python

    from fatgoose3 import FatGoose

    UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'

    g = FatGoose()
    g.config.http_headers = {'user-agent': UA}
    proxies = {
        'http': '127.0.0.1:6789'
    }
    g.config.http_proxies = proxies
    g.config.http_headers['cookie'] = 'bb_geo_info={"country":"HK","region":"Asia","fieldN":"cp"}|1630401938042; pxcts=3e8fbc20-04bd-11ec-8cd2-b3feeb40fb79; _pxvid=3e8e9ca4-04bd-11ec-8917-576c79444c71; _reg-csrf=s%3ASR7J68z_nbtjIVZHKZkaS2B8.GMAKXuiosdCaW15fwDiLF%2BKELfQrEQjmPxjbZc6Nh0I; _user-status=anonymous; agent_id=42c00fe3-a7c6-4fc7-817d-b8408683ad09; session_id=49ad7b47-d543-46af-b3d2-8eea1d0a64cc; session_key=941041c3381825d3821cee5e00003315ab40ef22; gatehouse_id=307e7059-3c1c-42fa-a6a7-fd3258495e6d; bb_geo_info={"countryCode":"HK","country":"HK","field_n":"cp","trackingRegion":"Asia","cacheExpiredTime":1630401938755,"region":"Asia","fieldN":"cp"}|1630401938755; _sp_krux=false; _sp_v1_uid=1:442:9c1d8270-dd33-4d91-bdf0-717556a6dc78; _sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbLKK83J0YlRSkVil4AlqmtrlXSGvrJYAB7rhbDrAAAA; _sp_v1_opt=1:; _sp_v1_csv=null; _sp_v1_lt=1:; ccpaUUID=eeb22a2f-37d2-4216-9b15-6939d9f56d76; dnsDisplayed=true; ccpaApplies=true; signedLspa=false; bbgconsentstring=req1fun1pad1; _gcl_au=1.1.1471559377.1629797140; bdfpc=004.0618011914.1629797140495; _ga=GA1.2.1381061563.1629797142; _fbp=fb.1.1629797142113.1604849760; _rdt_uuid=1629797142167.d0934f60-09ad-4dbb-9e57-ddf07f6c8825; _scid=988ca44c-45bb-449a-b5a7-cc356e1d65ea; _cc_id=5df5e1609ed0920d07d459f0f0f0c5cc; _li_dcdm_c=.bloomberg.com; _lc2_fpi=b1166d620485--01fdvqnqcf5fje5zb1a57ra6y9; _sctr=1|1629734400000; trc_cookie_storage=taboola%2520global%253Auser-id%3Dd5a5f492-ef6c-4fe7-ba35-80eea07d6db4-tuct564d9ac; panoramaId_expiry=1630401975910; panoramaId=3b0a568e58737e94a4996b442b954945a702e8c220d6a76147bd12b84e677fee; _gid=GA1.2.1761810210.1630030612; bb-mini-player-viewed=true; __sppvid=88bd4d61-c2b2-4cb5-8364-d41e1fac087d; _parsely_visitor={%22id%22:%22pid=7f986ae5cfa02dc96e77de37a4221af7%22%2C%22session_count%22:8%2C%22last_session_ts%22:1630070749501}; kw.pv_session=2; _sp_id.3377=3024460b-5e07-452b-a1d4-3809a14c29af.1629797154.6.1630070758.1630052089.dd6c0ad0-7a27-4ebd-a61a-6a95c0b93ed5; _uetsid=d7ccfde006dc11ec947913a07a3316d2; _uetvid=1a32f6a0cffb11ebbd1189ad070ed2ad; _pxff_rf=1; _pxff_fp=1; _px3=b3a94ad338545d5c6fb11bf13a1af67ce50ad23933d4d268e355f832ec5bdded:pqzDpasuqmCAKNUSkda4HKVma0s6zRl8GTofMjKbqK5NqVmI92HA2dpDUsI7TMbeivZS9Sn5uYFCV8brTYBKEw==:1000:+n9iqbbK8dNSPAmdpmxUgJdYjr9JDibqbch/RMi+FkFjXWLwQi+Y7oW8hVMOKpkvDSvFYvo2sd0ZE5Po6JPjlkt9hBzT6VyChWeipQ/aC5IKSiSqGdXf26d8R6ZNqjADQQvyjBCdr1a72xBYxq9YAvHIlEZX8Q+6zND54b+I1z0=; _px2=eyJ0IjoxNjMwMDczODEzNDA4LCJ2IjoiM2U4ZTljYTQtMDRiZC0xMWVjLTg5MTctNTc2Yzc5NDQ0YzcxIiwidSI6ImJhYTI2OGYwLTA3NDAtMTFlYy04MzVkLTkzNDgxMDcxMTQ3YyIsImgiOiI0NTkxOWRjYTliOThkZjM2NjQwZTE1MjJkYzkxYWY3YTExYTBmZjUyNDA1ZmYyZmE1MmRhYmZhOGVhY2I1MTY4In0=; _reg-csrf-token=9tDNmMLv-XbkLgm-FXvgcThkYGhk0ilRUzMA; _last-refresh=2021-8-27%2014%3A11; _sp_v1_data=2:334565:1629797139:0:26:0:26:0:0:_:-1; consentUUID=368aeaa5-6870-4c08-bcb8-33df343899fe; _pxde=274b18718434974d119f2bb978440357ae3e773a68f59ced73483fc2415cbffa:eyJ0aW1lc3RhbXAiOjE2MzAwNzM1MjI3NjgsImZfa2IiOjAsImlwY19pZCI6W119'

    news = g.extract(url='https://www.bloomberg.com/news/articles/2021-08-06/china-s-wild-summer-of-stock-market-shocks-a-timeline')

    print(f'news.title: %s\n' % news.title)
    print(f'news.author: %s\n' % news.authors)
    print(f'news.publish_date: %s\n' % news.publish_date)
    print(f'news.cleaned_text: %s\n' % news.cleaned_text)
    print(f'news.infos: %s\n' % news.infos)
    g.close()

结果
~~~~

::

    news.title: China’s Summer of Stock Market Turbulence: A Timeline

    news.author: Olivia Tam

    news.publish_date: 2021-08-06T09:43:01.132Z

    news.cleaned_text: China’s overhaul of tutoring companies ignited a volatile few weeks for stock markets both onshore and in Hong Kong this summer, leaving investors on edge.

    Traders are looking out for what regulators may target next as Beijing tightens its grip on a range of sectors from private education to digital gaming, e-cigarettes, property and insurance.

    news.infos: {'meta': {'description': 'China’s overhaul of tutoring companies ignited a volatile few weeks for stock markets both onshore and in Hong Kong this summer, leaving investors on edge.', 'lang': 'en', 'keywords': 'China,Bear Market,HANG SENG INDEX,Hong Kong,HUBEI TECH SEMICONDUCTORS-A,Stocks,Media,TENCENT HOLDINGS LTD,ALIBABA PICTURES GROUP LTD,Music Streaming,technology,markets', 'favicon': 'https://assets.bwbx.io/s3/javelin/public/javelin/images/favicon-black-63fe5249d3.png', 'canonical': 'https://www.bloomberg.com/news/articles/2021-08-06/china-s-wild-summer-of-stock-market-shocks-a-timeline', 'encoding': 'utf-8'}, 'image': None, 'domain': 'www.bloomberg.com', 'title': 'China’s Summer of Stock Market Turbulence: A Timeline', 'cleaned_text': 'China’s overhaul of tutoring companies ignited a volatile few weeks for stock markets both onshore and in Hong Kong this summer, leaving investors on edge.\n\nTraders are looking out for what regulators may target next as Beijing tightens its grip on a range of sectors from private education to digital gaming, e-cigarettes, property and insurance.', 'opengraph': {'description': 'China’s overhaul of tutoring companies ignited a volatile few weeks for stock markets both onshore and in Hong Kong this summer, leaving investors on edge.', 'image': 'https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iFIfqCVqmk0s/v1/1200x900.jpg', 'site_name': 'Bloomberg.com', 'title': 'China’s Summer of Stock Market Turbulence: A Timeline', 'type': 'article', 'url': 'https://www.bloomberg.com/news/articles/2021-08-06/china-s-wild-summer-of-stock-market-shocks-a-timeline', 'article:opinion': 'false', 'article:content_tier': 'metered'}, 'tags': [], 'tweets': [], 'movies': [], 'links': ['https://www.bloomberg.com/news/articles/2021-07-25/china-to-overhaul-private-education-sector-hijacked-by-capital'], 'authors': 'Olivia Tam', 'publish_date': '2021-08-06T09:43:01.132Z'}
