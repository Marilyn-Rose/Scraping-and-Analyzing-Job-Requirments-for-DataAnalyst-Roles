import scrapy


class JobSpiderSpider(scrapy.Spider):
    name = "job_spider"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
