import scrapy


class JobdetailsSpider(scrapy.Spider):
    name = "jobdetails"
    allowed_domains = ["careerjet.com"]
    start_urls = ["https://www.careerjet.com/jobs?s=Data+analyst&l=USA"]

    def parse(self, response):
        # Loop through all <article> elements within the specified structure
        for job in response.css('ul.jobs article.job-clicky a[title]'):
            # Extract data from each <article>
            yield {     
                'title': job.css('::text').get(),  # extracting job title 
                'link': job.css('::attr(href)').get(), # extracting job link
                'job_title_attribute': job.css('::attr(title)').get()  # Extracts the 'title' attribute
            }




#search-content > ul > li:nth-child(2) > article > header > h2 > a