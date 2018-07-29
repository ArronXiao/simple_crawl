# -*- coding:utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

from chapter.chapterItemLoader import ChapterItemLoader
from tutorial.chapter.chapterItem import ChapterItem


class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    start_urls = [
        'http://www.biqugexsw.com/35_35872/13213749.html',
    ]

    def parse2(self, response):
        chapter_item = ChapterItemLoader(item=ChapterItem(), response=response)
        chapter_item.add_xpath('index', '//*[@class="content"]/h1/text()')
        chapter_item.add_xpath('title', '//*[@class="content"]/h1/text()')
        chapter_item.add_xpath('content', '//*[@id="content"]')
        return chapter_item.load_item()

    def parse(self, response):
        # chapter_item = ChapterItem()
        # chapter_item['index'] = response.xpath('//*[@class="content"]/h1/text()').extract()[0]
        # chapter_item['title'] = response.xpath('//*[@class="content"]/h1/text()').extract()[0]
        # chapter_item['content'] = response.xpath('//*[@id="content"]').extract()[0].replace(u'\xa0', u' ').replace(u'<br>',u'\n')
        # return chapter_item
        return self.parse2(response)

