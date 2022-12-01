import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    start_urls = ['http://quotes.toscrape.com/js']

    def parse(self, response):
        pass
