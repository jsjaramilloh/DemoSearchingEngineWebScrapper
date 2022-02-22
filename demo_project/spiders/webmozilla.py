import scrapy

class GoodReadsSpider(scrapy.Spider):
    #identity
    name="webmozilla"

    start_urls= [
        'https://www.google.com/search?client=firefox-b-d&q=The+Philadelphia+CS+for+Arts+and+Science+PTA%7CPTO+Pennsylvania+%40*'
    ]
        
    #Response
    def parse(self, response):
        for quote in response.selector.xpath("//div[@class='yuRUbf']"):
            yield {
                'title': quote.xpath("//h3[@class='LC20lb MBeuO DKV0Md']/text()").extract(),
                'link': quote.xpath("//div[@class='yuRUbf']/a[@href]").extract()
                }