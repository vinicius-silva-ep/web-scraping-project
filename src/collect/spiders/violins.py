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
                "price": product.css("span.money::text").get().strip(),
                "average_rating": product.css("div.jdgm-prev-badge").attrib[
                    "data-average-rating"
                ],
                "number_of_reviews": product.css("div.jdgm-prev-badge").attrib[
                    "data-number-of-reviews"
                ],
                "stock": product.css(
                    "span.product-stock-level__text div.product-stock-level__badge-text::text"
                )
                .get()
                .strip(),
                "description": product.css("div.productitem--description p::text")
                .get()
                .strip(),
                "image": product.css("img.productitem--image-primary").attrib["src"],
            }
