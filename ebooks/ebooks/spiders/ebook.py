import scrapy

BASE_URL = 'https://books.toscrape.com/'

class EbookSpider(scrapy.Spider):
    name = 'ebook'
    start_urls = [BASE_URL]

    def parse(self, response):
        ebooks = response.css("article.product_pod")
        
        for ebook in ebooks:
            loader = ItemLoader(item=EbookItem(), selector=ebook)
            
            loader.add_css("title", "h1::text")
            loader.add_css("price", "p.price_color::text")
            
            yield loader.load_item()
