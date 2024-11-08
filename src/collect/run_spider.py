import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from collect.spiders.violins import ViolinSpider


def run_spider():

    process = CrawlerProcess(get_project_settings())

    # Setting the output
    process.settings.set("FEED_FORMAT", "json")  # JSON format
    process.settings.set("FEED_URI", "../../data/data.json")  # Path for saving the data

    # Starts spider
    process.crawl(ViolinSpider)

    process.start()
