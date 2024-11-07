import scrapy


class FiddlershopSpider(scrapy.Spider):
    name = "fiddlershop"
    allowed_domains = ["fiddlershop.com"]
    start_urls = ["https://fiddlershop.com/collections/violins"]

    def parse(self, response):
        products = response.css('div.product-item__info  ')

        for product in products:

            'name' = response.css('a.product-item-meta__title::text').get()
        
