# -*- coding: utf-8 -*-
"""\
This is a python port of "Goose" orignialy licensed to Gravity.com
under one or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.

Python port was written by Xavier Grangier for Recrutae

Gravity.com licenses this file
to you under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from fatgoose3.extractors import BaseExtractor


class AuthorsExtractor(BaseExtractor):

    def extract(self):
        authors = set()

        for known_tag in self.config.known_author_patterns:
            meta_tags = self.parser.getElementsByTag(self.article.doc,
                                                     attr=known_tag.attr,
                                                     value=known_tag.value,
                                                     tag=known_tag.tag)
            if not meta_tags:
                continue

            if known_tag.domain and known_tag.domain == self.article.domain:    # 当有配置特定域名就直接忽略下面的规则
                if known_tag.processor is not None:
                    author = known_tag.processor(meta_tags[0].text_content().strip())
                    return author.split('\n')[0].strip()

            for meta_tag in meta_tags:

                if known_tag.subpattern:
                    name_nodes = self.parser.getElementsByTag(meta_tag,
                                                              attr=known_tag.subpattern.attr,
                                                              value=known_tag.subpattern.value,
                                                              tag=known_tag.subpattern.tag)

                    if len(name_nodes) > 0:
                        names = self.parser.getText(name_nodes[0])
                        for name in names.split(','):
                            authors.add(name.strip())
                else:
                    if known_tag.tag is None:
                        names = self.parser.getAttribute(meta_tag, known_tag.content)
                        if not names:
                            continue

                        for name in names.split(','):
                            authors.add(name.strip())
                    else:
                        names = meta_tag.text_content().strip()
                        for name in names.split(','):
                            authors.add(name.strip())
        return ','.join(list(authors))
