import scrapy

class GoodReadsSpider(scrapy.Spider):
    #identity
    name="webbing"

    start_urls= [
        'https://www.bing.com/search?q=The+Philadelphia+CS+for+Arts+and+Science+PTA%7CPTO+Pennsylvania+%40*'
    ]
        
    #Response
    def parse(self, response):
        for quote in response.selector.xpath("//li[@class='b_algo']"):
            yield {
                'title':quote.xpath(".//h2/text()").extract(),
                'link':quote.xpath(".//a[@_ctf='rdr_T']").extract()
            }