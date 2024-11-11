import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from collect.spiders.violins import ViolinSpider


def run_spider():

    process = CrawlerProcess(get_project_settings())

    # Starts spider
    spider = ViolinSpider()
    process.crawl(ViolinSpider)

    process.start()

    # After the collect process, it creates a dataframe
    data = spider.collected_data

    return data
