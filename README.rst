FatGoose3
=========

经过强化的goose3通用网页提取器

安装
----

``pip install fatgoose3``

例1 最简单的例子
----------------

虽然FatGoose有自带的下载器，但是并不推荐使用，本例中我们使用经过requests下载好的网页传给\ ``raw_html``\ ，把FatGoose只当作解析器用，这样灵活度更高。

如果想用FatGoose自带的下载器，可以参考\ ``examples``\ 文件夹里的\ ``eg.3.py``

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

结果

::

    news.author: Cui Fandi

    news.publish_date: 2021-06-24 21:21:00

常用设置
--------

fatgoose3如果没有从网页中提取到发布时间，也会尝试从URL中提取出文章时间，如果不希望从url中提取时间，此设置默认为
``True``\ ，如果需要关闭，可如下设置

.. code:: python

    g.config.fetch_pubdate_from_url = False
