# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import ArticleItem

class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.xpath('//div[@class="article"]/h1/text()').get()
        avatar = response.xpath('//div[@class="author"]/a/img/@src').get()
        author = response.xpath('//div[@class="info"]/span/a/text()').get()
        pub_time = response.xpath('//div[@class="meta"]/span[@class="publish-time"]/text()').get()
        url = response.url
        url1 = url.split('?')[0]
        article_id = url1.split('/')[-1]
        content = response.xpath('//div[@class="show-content-free"]').get()
        word_count = response.xpath('//span[@class="wordage"]/text()').get()
        read_count = response.xpath('//span[@class="views-count"]/text()').get()
        like_count = response.xpath('//span[@class="likes-count"]/text()').get()
        subjects = ''.join(response.xpath('//div[@class="include-collection"]/a/div[@class="name"]/text()').getall())



        item = ArticleItem(
            title=title,
            avatar=avatar,
            author=author,
            pub_time=pub_time,
            article_id=article_id,
            content=content,
            origin_url=response.url,
            subjects=subjects,
            word_count=word_count,
            read_count=read_count,
            like_count=like_count
        )
        yield item


