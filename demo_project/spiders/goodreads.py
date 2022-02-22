import scrapy

class GoodReadsSpider(scrapy.Spider):
    #identity
    name="goodreads"

    start_urls= [
        'https://www.goodreads.com/quotes?page=1'
    ]

    #Response
    def parse(self, response):
        for quote in response.selector.xpath("//div[@class='quote']"):
            yield {
                'text':quote.xpath(".//div[@class='quoteText']/text()[1]").extract_first(),
                'author':quote.xpath(".//div[@class='quoteText']/child::a").extract_first(),
                'tags':quote.xpath(".//div[@class='greyText smallText left']/a").extract
            }