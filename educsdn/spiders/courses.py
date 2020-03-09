# -*- coding: utf-8 -*-
import scrapy
from educsdn.items import CoursesItem

class CoursesSpider(scrapy.Spider):
    name = 'courses'
    allowed_domains = ['edu.csdn.net']
    start_urls = ['https://edu.csdn.net/courses/o280/p1']
    # 第一页
    p = 1


    def parse(self, response):
        # 解析课程信息
        # 获取当前请求页面下的所有课程信息
        # dl = response.xpath("//div[@class='course_item acsdnd_item']")
        # # 遍历课程信息并封装到item
        # for dd in dl:
        #     print(dd.xpath("./div[@class='titleInfor'/text()]").extract())
        dl = response.selector.css("div.course_item")
        for dd in dl:
            item = CoursesItem()
            item['title'] = dd.css("span.title::text").extract_first()
            item['url'] = dd.css("a::attr(href)").extract_first()
            item['pic'] = dd.css("img::attr(src)").extract_first()
            item['teacher'] = dd.css("span.lecname::text").extract_first()
            # item['teacher'] = dd.re_first("<p>讲师:(.*?)</p>")

            item['time'] = dd.css("span.course_lessons::text").extract_first()
            # item['time'] = dd.re_first("<em>（[0-9]+）</em>课时")

            item['price'] = dd.css("p.priceinfo i::text").extract_first()
            # item['price'] = dd.re_first("￥([0-9\.]+)")
            # print(item)
            # 将数据送入pipelines
            yield item

        # 跨页提取信息
        self.p += 1
        if self.p < 4:
            next_url = 'https://edu.csdn.net/courses/o280/p'+ str(self.p)
            url = response.urljoin(next_url)
            yield scrapy.Request(url=url,callback=self.parse)

