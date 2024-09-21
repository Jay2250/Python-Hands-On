import scrapy
from typing import Any
from scrapy.http import Response

class BookSpider(scrapy.Spider):
    name = 'multiPageSpider'
    start_urls = ['https://books.toscrape.com/catalogue/category/books/mystery_3/index.html']
    
    
    def parse(self, response):
        #extract the h1 title from the page
        page_title = response.css('h1::text').get()
        #print page_title
        print(f'Page Title :',{page_title})
        
        #extract book informations
        for book in response.css('article.product_pod'):
            title = book.css('h3 a::attr(title)').get()
            url = book.css('h3 a::attr(href)').get()
            
            #yeild book data along with page title
            yield{
                'page_title': page_title, #add the page title to the 
                'url': response.urljoin(url),
                'title': title
            }
            
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)