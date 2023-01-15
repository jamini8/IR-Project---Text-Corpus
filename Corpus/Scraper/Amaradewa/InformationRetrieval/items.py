# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SongItem(scrapy.Item):
    Title = scrapy.Field()
    Singer = scrapy.Field()
    Composer = scrapy.Field()
    Lyricist = scrapy.Field()
    # story = scrapy.Field()
    image = scrapy.Field()