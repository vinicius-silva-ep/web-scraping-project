import scrapy


class VioninsSpider(scrapy.Spider):
    name = "violins"
    allowed_domains = ["violins.com."]
    start_urls = ["https://www.violins.com.au/collections/beginner-violins"]

    def parse(self, response):
        products = response.css("div.productitem")

        for product in products:
            yield {
                "name": product.css("h2.productitem--title a::text").get().strip(),
            }
