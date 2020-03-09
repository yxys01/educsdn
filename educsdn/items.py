# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CoursesItem(scrapy.Item):
    '''课程信息item类：课程标题、url地址、图片、讲师、总课时、价格'''
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    pic = scrapy.Field()
    teacher = scrapy.Field()
    time = scrapy.Field()
    price = scrapy.Field()

