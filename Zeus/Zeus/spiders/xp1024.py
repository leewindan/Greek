# -*- coding: utf-8 -*-

import scrapy


class Xp1024Spider(scrapy.Spider):
    name = 'xp1024'
    allowed_domains = ['se.gn79.xyz/pw/index.php']
    start_urls = ['http://se.gn79.xyz/pw/index.php/']

    def parse(self, response):
        title = response.xpath('//html/head/title/text()')
        print(title)
