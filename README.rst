FatGoose3
=========

经过强化的goose3通用网页提取器,
我测试了中英文两种新闻的解析，都有不错的效果

安装
----

``pip install fatgoose3``

虽然FatGoose有自带的下载器，但是并不推荐使用，本例中我们使用经过requests下载好的网页传给\ ``raw_html``\ ，把FatGoose只当作解析器用，这样灵活度更高。
如果想用FatGoose自带的下载器，可以参考\ ``examples``\ 文件夹里的\ ``eg.0.py``

例1 最简单的例子
----------------

中文资讯
~~~~~~~~

.. code:: shell

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

.. code:: text

    news.title: 德公司推出无人机新型防撞单元 能配备多旋翼平台_军事_央视网(cctv.com)

    news.author: 王腾

    news.publish_date: 2015-05-28 00:00:00

    news.cleaned_text: 中新网5月28日电 据中国国防科技信息网报道，针对无人机防撞问题，德国一家公司正在推出一种新的解决方案：无人机防撞单元。据悉，该单元在工作时使用多种不同的传感器，且无需GPS定位信息，能配备到大多数单旋翼或多旋翼平台上。

    无人机已经成为当今社会的一种重要工具，我们难以预估这一新兴产业对未来生活的深远影响。但可以明确的是，除了巨大的经济潜力，小型、灵活的无人机同时带来了一种实际的隐患：旋翼机在飞行过程中，若叶片碰触其他物体或正常运转受到阻碍，可能导致其坠落。举例说明这一问题的严峻形势，统计表明平均每月至少有25起涉及无人机与飞机几乎发生碰撞的飞行事件。

    为了尽快解决这一问题，而不是寻求一种“十全十美”的解决方案，德国AEVO股份有限公司已经开发了一种叫做AECAS的电子单元。该单元能够接收障碍物信息和无人机操控信息，并基于这些信息独立地生成一套修正命令，从而避免无人机与障碍物发生碰撞。在整个过程中，AECAS单元可以从系统中直接相连的传感器获取障碍物信息或接收指定标准格式的障碍物信息。在后一种模式下，无人机操作员无需选择适用的传感器、考虑其所处的方位及如何使用其获取的信息。

    按照设计，AECAS单元与GPS定位系统完全独立。在不依靠GPS信息的情况下，ECAS团队开发了一种新的基于深度的SLAM技术来获取无人机的飞行速度，并利用障碍物的相对位置信息来确定避让策略。

    基于AECAS单元，可以实现以下3种级别的防撞能力： EDC-紧急状态下的间距控制：保持无人机与障碍物之间的最小间距(可使用AECAS100和AECAS2000单元)；

    ABS-自动减速监控：在无人机与障碍物靠近的过程中逐渐减速(可使用AECAS2000单元)；

    AECAS100单元的成本为税前249欧元，可以在网上预订。改进型AECAS2000单元将于今年夏天开始接受预订。

    news.infos: {'meta': {'description': '按照设计，AECAS单元与GPS定位系统完全独立。在不依靠GPS信息的情况下，ECAS团队开发了一种新的基于深度的SLAM技术来获取无人机的飞行速度，并利用障碍物的相对位置信息来确定避让策略。', 'lang': None, 'keywords': '无人机 防撞单元 多旋翼平台', 'favicon': '', 'canonical': 'http://military.cntv.cn/2015/05/28/ARTI1432794380285200.shtml', 'encoding': 'utf-8'}, 'image': None, 'domain': 'military.cntv.cn', 'title': '德公司推出无人机新型防撞单元 能配备多旋翼平台_军事_央视网(cctv.com)', 'cleaned_text': '中新网5月28日电 据中国国防科技信息网报道，针对无人机防撞问题，德国一家公司正在推出一种新的解决方案：无人机防撞单元。据悉，该单元在工作时使用多种不同的传感器，且无需GPS定位信息，能配备到大多数单旋翼或多旋翼平台上。\n\n无人机已经成为当今社会的一种重要工具，我们难以预估这一新兴产业对未来生活的深远影响。但可以明确的是，除了巨大的经济潜力，小型、灵活的无人机同时带来了一种实际的隐患：旋翼机在飞行过程中，若叶片碰触其他物体或正常运转受到阻碍，可能导致其坠落。举例说明这一问题的严峻形势，统计表明平均每月至少有25起涉及无人机与飞机几乎发生碰撞的飞行事件。\n\n为了尽快解决这一问题，而不是寻求一种“十全十美”的解决方案，德国AEVO股份有限公司已经开发了一种叫做AECAS的电子单元。该单元能够接收障碍物信息和无人机操控信息，并基于这些信息独立地生成一套修正命令，从而避免无人机与障碍物发生碰撞。在整个过程中，AECAS单元可以从系统中直接相连的传感器获取障碍物信息或接收指定标准格式的障碍物信息。在后一种模式下，无人机操作员无需选择适用的传感器、考虑其所处的方位及如何使用其获取的信息。\n\n按照设计，AECAS单元与GPS定位系统完全独立。在不依靠GPS信息的情况下，ECAS团队开发了一种新的基于深度的SLAM技术来获取无人机的飞行速度，并利用障碍物的相对位置信息来确定避让策略。\n\n基于AECAS单元，可以实现以下3种级别的防撞能力： EDC-紧急状态下的间距控制：保持无人机与障碍物之间的最小间距(可使用AECAS100和AECAS2000单元)；\n\nABS-自动减速监控：在无人机与障碍物靠近的过程中逐渐减速(可使用AECAS2000单元)；\n\nAECAS100单元的成本为税前249欧元，可以在网上预订。改进型AECAS2000单元将于今年夏天开始接受预订。', 'opengraph': {}, 'tags': [], 'tweets': [], 'movies': [], 'links': ['http://military.cntv.cn/list/world/', 'http://www.chinanews.com/mil/2015/05-28/7307057.shtml', '#pinglun', 'javascript:;', 'javascript:;', '#', '#', '#', '#', '#'], 'authors': '王腾', 'publish_date': '2015-05-28 00:00:00'}

英文资讯
~~~~~~~~

.. code:: python

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

.. code:: text

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

.. code:: text

    news.author: Cui Fandi

    news.publish_date: 2021-06-24 21:21:00

常用设置
--------

fatgoose3如果没有从网页中提取到发布时间，也会尝试从URL中提取出文章时间，如果不希望从url中提取时间，此设置默认为
``True``\ ，如果需要关闭，可如下设置

.. code:: python

    g.config.fetch_pubdate_from_url = False
