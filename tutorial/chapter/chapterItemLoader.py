from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags


def item_filter(value):
    print 'item_filter -------------------------'
    return value.replace(u'\xa0', u' ').replace(u'<br/>', u'\n').replace('        ', '\r\n')


class ChapterItemLoader(ItemLoader):
    default_output_processor = TakeFirst()

    content_in = MapCompose(item_filter, remove_tags)
