
import scrapy
class ChapterItem(scrapy.Item):
    title = scrapy.Field()
    index = scrapy.Field()
    content = scrapy.Field()
