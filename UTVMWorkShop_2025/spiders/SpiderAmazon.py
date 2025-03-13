import re
import scrapy

class SpiderAmazon(scrapy.Spider):
    name = "SpiderAmazon"
    start_urls = [
        "https://www.amazon.com.mx/s?k=iphone&crid=3H14COWQX0HVE&sprefix=iphon%2Caps%2C247&ref=nb_sb_ss_mvt-t8-ranker_1_5"
    ]

    def parse(self, response):
        
        html = response.text


        products = self.__get_text_between(
            html = html,
            starts = """<div class="sg-col-inner">""",
            ends =   """</div>"""
        )
        for product in products:
        
            product_name = self.__get_text_between(
                html = product,
                starts = 'alt="',
                ends =   '"'
            )
         
            product_link = self.__get_text_between(
                html = product,
                starts = 'href="',
                ends =   '"'
            )

            yield {
                "ProductName": product_name,
                "ProductLink":product_link
            }
            
    
    def __get_text_between(self,html, starts:str, ends:str)->list:
        """
            This method gets the data in between two string parameters

        Args:
            html (_type_): The text from the website
            starts (str): The start str you want to get match
            ends (str): The start str you want to get match

        Returns:
            A list with all data in between
        """
        pattern = re.escape(starts) + r"(.*?)" + re.escape(ends)
        return re.findall(pattern, html, re.DOTALL)
