# -*- coding: utf-8 -*-

import scrapy

from datetime import datetime

import pytz
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapenews.items import ScrapenewsItem
from .iol import IOLSpider

SAST = pytz.timezone('Africa/Johannesburg')

BASE_URL = 'http://www.iol.co.za/mercury'


class NatalMercurySpider(CrawlSpider):
    name = 'natalmercury'
    allowed_domains = ['www.iol.co.za']
    # categories = ['news', 'world', 'environment', 'business', 'sport',
    #               'goodlife', 'network', 'opinion']
    # start_urls = ['{}/{}'.format(BASE_URL, category)
    #               for category in categories]

    start_urls =['{}/{}'.format(BASE_URL, 'news')]

    rules = (
            # Rule(LinkExtractor(allow=(r'(\w+[-]{0,1})+-\d+$',)), 'parse'),
            # Rule(LinkExtractor(allow=(r'(\w+[-]{0,1})+-\d+$',)), 'parse'),
            Rule(LinkExtractor(allow=(r'/mercury/news/(\w+[-]{0,1})+-\d+$',)), 'parse'),
            )

    def parse(self, response):
        title = response.xpath('//header/h1/text()').extract_first()
        print title
        import lxml

        print '********************'
        print response.xpath('//article[contains(@class,"main-feature")]/a/@href').extract()
        url = response.xpath('//article[contains(@class,"main-feature")]/a/@href').extract()[0]

        yield scrapy.Request(BASE_URL + url, self.parse)



        # print response.body

#         self.logger.info('%s %s', response.url, title)
#         article_body = response.xpath('//div[@itemprop="articleBody"]')
#         if article_body:
#             body_html = article_body.extract_first()
#             byline = response.xpath('//span[@itemprop="author"]/strong/text()').extract_first()
#             publication_date_str = response.xpath('//span[@itemprop="datePublished"]/@content').extract_first()

#             publication_date = datetime.strptime(publication_date_str, '%Y-%m-%dT%H:%M')
#             publication_date = SAST.localize(publication_date)

#             item = ScrapenewsItem()
#             item['body_html'] = body_html
#             item['title'] = title
#             item['byline'] = byline
#             item['published_at'] = publication_date.isoformat()
#             item['retrieved_at'] = datetime.utcnow().isoformat()
#             item['url'] = response.url
#             item['file_name'] = response.url.split('/')[-1]
#             item['spider_name'] = self.name

#             item['publication_name'] = self.publication_name

#             yield item
