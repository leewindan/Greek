# -*- coding: utf-8 -*-

import scrapy
from faker import Factory
from ..items import ZeusItem

f = Factory.create()


class Xp1024Spider(scrapy.Spider):
    name = 'xp1024'
    allowed_domains = ['se.gn79.xyz']
    base_url = 'http://se.gn79.xyz/pw'
    start_urls = ['http://se.gn79.xyz/pw/thread.php?fid=15']

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': f.user_agent()
    }

    def parse(self, response):
        # title = response.xpath('//html/head/title/text()')
        # print(title)
        # with open('./page.html', 'wb') as f:
        #     f.write(response.body)
        print('function parse')
        print(response.url)
        yield scrapy.Request(response.url, headers=self.headers, callback=self.parse_list_page)

        # for page in response.xpath('//div[@class="pages cc"]'):
        #     print(page.xpath('./a[2]').get())

    def parse_list_page(self, response):
        print('function parse_list_page')
        # 获取所有大网页中所有网页的uri和网页名称
        lists = response.xpath('//tr[@class="tr3 t_one"]')
        for i in lists:
            href = i.xpath('./td[2]/h3/a/@href').get()
            text = i.xpath('./td[2]/h3/a/text()').get()
            # print('html_data' in href)
            # 去掉非目标的uri
            if href and text:
                if 'html_data' in href:
                    yield scrapy.Request(response.urljoin(href),
                                         headers=self.headers, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        item = ZeusItem()
        title = response.xpath('//html/head/title/text()')
        print(title)
        jpg_url_list = response.xpath('//div[@id="read_tpc"]')
        print(jpg_url_list)
        for i in jpg_url_list.xpath('./img'):
            # print(i.xpath('./@src'))
            item['url'] = i.xpath('./@src').get()

