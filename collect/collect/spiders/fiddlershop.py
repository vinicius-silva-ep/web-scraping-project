import scrapy


class FiddlershopSpider(scrapy.Spider):
    name = "fiddlershop"
    allowed_domains = ["fiddlershop.com"]
    start_urls = ["https://fiddlershop.com/collections/violins"]

    def parse(self, response):
        products = response.css("div.product-item-meta")

        for product in products:
            yield {
                "name": product.css("a.product-item-meta__title::text").get(),
                "price": product.css("span.price::text").getall()[-1].strip(),
                "data_rating": product.css(
                    "span.stamped-badge-caption::attr(data-rating)"
                ).get(),
            }
