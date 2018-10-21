# -*- coding:utf-8 -*-
import scrapy

from chapter.chapterItemLoader import ChapterItemLoader
from tutorial.chapter.chapterItem import ChapterItem


class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    start_urls = [
        'https://www.biqugexsw.com/35_35872/',
    ]

    def parseItem(self, response):
        chapter_item = ChapterItemLoader(item=ChapterItem(), response=response)
        chapter_item.add_xpath('index', '//*[@class="content"]/h1/text()')
        chapter_item.add_xpath('title', '//*[@class="content"]/h1/text()')
        chapter_item.add_xpath('content', '//*[@id="content"]')
        yield chapter_item.load_item()

    def parse(self, response):
        url = response.xpath("//dd/a[@href]//@href").extract()
        title = response.xpath("//dd/a/text()").extract()
        # print len(url)
        # itemUrl = 'https://www.biqugexsw.com/' + url[0]
        # return  scrapy.Request(itemUrl, callback=self.parseItem)
        for (urlitem,titleItem) in zip(url, title):
            itemUrl = 'https://www.biqugexsw.com/'+urlitem
            yield scrapy.Request(itemUrl, callback=self.parseItem)


