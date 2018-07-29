
import scrapy
class ChapterItem(scrapy.Item):
    index = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
