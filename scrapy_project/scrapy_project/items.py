# -*- coding: utf-8 -*-

import scrapy

class AmhItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    doc = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    id = scrapy.Field()
