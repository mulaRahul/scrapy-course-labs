import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    start_urls = ['http://quotes.toscrape.com/tableful/']

    def parse(self, response):
        pass
