# -*- coding: utf-8 -*-

import scrapy
from faker import Factory
from ..items import ZeusItem

f = Factory.create()


class WangyouzipaiSpider(scrapy.Spider):
    name = 'wangyouzipai'
    allowed_domains = ['se.gn79.xyz']
    start_urls = ['http://se.gn79.xyz/']
    base_url = 'http://se.gn79.xyz/pw'
    start_urls = ['http://se.gn79.xyz/pw/thread.php?fid=15&page=1']

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': f.user_agent()
    }

    # page index 1在parse方法中第一个处理了，所以这里的开始index从2开始
    start_pindex = 1
    last_pindex = 100

    def parse(self, response):
        # with open('./page.html', 'wb') as f:
        #     f.write(response.body)
        # print('function parse')
        yield scrapy.Request(response.url, headers=self.headers, callback=self.parse_list_page)

        last_uri = response.xpath('//div[@class="pages cc"]')[0].xpath('./a/@href')[-1].get()
        last_page_index = int(last_uri.split('=')[-1])
        # 上面是从网页里面获取的last page，这个值太大，下面自己自定义起始网页index
        start_page_index = self.start_pindex
        last_page_index = self.last_pindex

        # 这分部实现，与可以放到下面的函数里，在执行的时候回调自己
        for page_index in range(start_page_index, last_page_index+1):
            # print('Current running on page -> {}'.format(page_index))
            next_url = self.base_url + '/thread.php?fid=15&page=' + str(page_index)
            yield scrapy.Request(next_url, headers=self.headers, callback=self.parse_list_page)

    def parse_list_page(self, response):
        meta = {}
        # print('function parse_list_page')
        pagesone = response.xpath('//span[@class="pagesone"]/text()').get()
        current_page = pagesone.split()[0] + pagesone.split()[1]
        print(current_page)
        # 获取所有大网页中所有网页的uri和网页名称
        lists = response.xpath('//tr[@class="tr3 t_one"]')
        for i in lists:
            # href 每个网页的url
            # title 每个网页的名字
            href = i.xpath('./td[2]/h3/a/@href').get()
            title = i.xpath('./td[2]/h3/a/text()').get()
            meta['title'] = title

            # 去掉非目标的uri
            if href and title:
                if 'html_data' in href:
                    yield scrapy.Request(response.urljoin(href),
                                         headers=self.headers,
                                         meta=meta,
                                         callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        item = ZeusItem()
        # page_title 不带有日期
        # page_title = response.xpath('//html/head/title/text()')
        jpg_url_list = response.xpath('//div[@id="read_tpc"]')

        # page_title从上一个方法获取，带有日期
        page_title = response.meta['title']
        # print('page_title -> {}'.format(page_title))

        title = page_title.split('|')[0]
        url_list = jpg_url_list.xpath('./img/@src').getall()

        # item = ZeusItem(images=title, image_urls=url_list)
        item['title'] = title
        item['image_urls'] = url_list
        yield item

        # for i in jpg_url_list.xpath('./img'):
        #     item['title'] = page_title.get().split('|')[0]
        #     item['url'] = [i.xpath('./@src').get()]
        #     yield item
