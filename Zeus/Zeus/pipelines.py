# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import scrapy
import os
from scrapy.pipelines.images import ImagesPipeline
from . import settings
from faker import Factory

f = Factory.create()


class ZeusPipeline:
    def process_item(self, item, spider):
        return item


class ZeusImageSavePipeline(ImagesPipeline):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': f.user_agent()
    }

    def get_media_requests(self, item, info):
        # urls = ItemAdapter(item).get(self.images_urls_field, [])
        # for url in urls:
        #     print(url)
        #     self.headers['referer'] = url
        #     yield scrapy.Request(url, headers=self.headers)
        for image_url in item["image_urls"]:
            yield scrapy.Request(url=image_url,
                                 headers=self.headers,
                                 meta={"item": item})

    def file_path(self, request, response=None, info=None, *, item=None):
        # 这个方法是在图片将要被存储的时候调用，来获取这个图片存储的路径
        title = item.get('title')
        image_store = settings.IMAGES_STORE
        title_path = os.path.join(image_store, title)

        if not os.path.exists(title_path):
            print(title_path)
            os.makedirs(title_path)

        image_name = request.url.split('/')[-1]
        # 下面的参数title,使用的是相对路径，没有使用绝对路径
        image_path = os.path.join(title, image_name)

        return image_path
