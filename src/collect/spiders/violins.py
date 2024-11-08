import scrapy


class ViolinSpider(scrapy.Spider):
    name = "violins"
    allowed_domains = ["violins.com.au"]
    head_url = "https://www.violins.com.au"
    start_urls = ["https://www.violins.com.au/collections/beginner-violins"]
    page_count = 1
    max_pages = 10

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

        next_page = response.css("li.pagination--next a::attr(href)").get()

        if self.page_count < self.max_pages:
            next_page = self.head_url + next_page
            if next_page:
                self.page_count += 1
                yield scrapy.Request(url=next_page, callback=self.parse)
                print(next_page)
