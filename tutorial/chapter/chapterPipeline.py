# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs


class ChapterPipeline(object):
    def __init__(self):
        self.rootPath = ".\out\大王饶命\\"

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        print "item['title'] " + item['title']
        fileName = self.rootPath + item['title'] + ".txt"
        print "filename" + fileName
        self.file = codecs.open(
            fileName.decode("utf-8"), 'a', encoding='utf-8')
        self.file.write("\n")
        self.file.write(item['title'])
        self.file.write("\n")
        content = item['content']
        content_array = content.split('\r\n')
        print 'content array lenght ' + bytes(len(content_array))
        content = ''.join(content_array[0: len(content_array) - 1])
        content = content.replace('\r\n', ' ')
        self.file.write(content)
        return item
