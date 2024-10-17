import scrapy

# Defining the Spider Class
class JobSpider(scrapy.Spider):
    
    name = 'job_spider'  # spider name
    allowed_domains = ["www.glassdoor.com"]
    start_urls = ['https://www.glassdoor.com/Job/index.htm']
    
    # constructor method (initialize instance attributes)
    def parse(self, response):
        # The parsing logic
        job_title = response.css()
    
