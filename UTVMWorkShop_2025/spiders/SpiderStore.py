import re
import scrapy

class SpiderStore(scrapy.Spider):
    name = "SpiderStore"
    start_urls = [
        "https://www.amazon.com.mx/s?k=audifonos+inalambricos&crid=2XLY7AEP8IKGT&sprefix=audifonos%2Caps%2C206&ref=nb_sb_ss_mvt-t8-ranker_1_9"
    ]

    def parse(self, response):
        
        html = response.text

        data = self.__get_text_between(
            html = html,
            starts = """ """,
            ends =   """ """
        )
     
        yield{
            'data':data

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
