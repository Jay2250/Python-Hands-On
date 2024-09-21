# import scrapy
# from typing import Any
# from scrapy.http import Response

# class BookSpider(scrapy.Spider):
#     name = 'hrefPageSpider'
#     start_urls = ['https://books.tosrape.com']
    
    
#     def parse(self, response):
#         #extract the h1 title from the page
#         links = response.css('a::attr(href)').get()
#         #print page_title
#         print(f'Page Title :',{links})
        
        
        
#         #extract book informations
#         for book in response.css('article.product_pod'):
            
#             links = book.css('a::attr(href)').getall()
            
#             #yeild book data along with page title
#             yield{
#                 'links': links, #add the page title to the 

#             }
            
from typing import Any
import scrapy
from scrapy.http import Response
class BookSpider(scrapy.Spider):
    name = 'hrefPageSpider'
    start_urls = ['https://books.toscrape.com/']
    
    
    def parse(self, response):
        #extract the h1 title from the page
        page_title = response.css('h1::text').get()
        #print page_title
        print(f'Page Title :',{page_title})
        
        #extract book informations
        for book in response.css('article.product_pod'):
            url = book.css('h3 a::attr(href)').get()
            
            #yeild book data along with page title
            yield{ 
                'url': response.urljoin(url),
            }