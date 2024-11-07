# import scrapy


# class FiddlershopSpider(scrapy.Spider):
#     name = "fiddlershop"
#     allowed_domains = ["fiddlershop.com"]
#     start_urls = ["https://fiddlershop.com/collections/violins"]

#     def parse(self, response):
#         products = response.css("div.product-item-meta")

#         for product in products:
#             yield {
#                 "name": product.css("a.product-item-meta__title::text").get(),
#                 "price": product.css("span.price::text").getall()[-1].strip(),
#                 "data_rating": product.css(
#                     "span.stamped-badge::attr(data-rating)"
#                 ).get(),
#                 "data_reviews": product.css(
#                     "span.stamped-badge-caption::attr(data-reviews)"
#                 ).get(),
#             }

import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.selector import Selector


class FiddlershopSpider(scrapy.Spider):
    name = "fiddlershop"
    allowed_domains = ["fiddlershop.com"]
    start_urls = ["https://fiddlershop.com/collections/violins"]

    def __init__(self, *args, **kwargs):
        super(FiddlershopSpider, self).__init__(*args, **kwargs)
        options = Options()
        options.add_argument("--headless")  # Executa em segundo plano
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)

    def parse(self, response):
        self.driver.get(response.url)

        # Espera o carregamento dos produtos e do elemento stamped-badge
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div.product-item-meta")
            )
        )

        sel = Selector(text=self.driver.page_source)
        products = sel.css("div.product-item-meta")

        for product in products:
            name = product.css("a.product-item-meta__title::text").get()
            price = product.css("span.price::text").getall()[-1].strip()
            data_rating = product.css("span.stamped-badge::attr(data-rating)").get()
            data_reviews = product.css(
                "span.stamped-badge-caption::attr(data-reviews)"
            ).get()

            # Extraindo a quantidade de tamanhos disponíveis
            size_info = product.css("div.size-info span::text").get()
            # Manipulando o texto para capturar a quantidade (remover texto extra)
            size_available = size_info.split()[0] if size_info else "0"

            yield {
                "name": name,
                "price": price,
                "data_rating": data_rating,
                "data_reviews": data_reviews,
                "size_available": size_available,
            }

    def closed(self, reason):
        self.driver.quit()
