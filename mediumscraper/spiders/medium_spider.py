import scrapy

class mediumScraper(scrapy.Spider):
    name = "medium"

    def start_requests(self):
        urls = ['https://medium.com/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.css('a::attr(href)').extract())