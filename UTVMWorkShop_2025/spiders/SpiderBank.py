import re
import scrapy

class SpiderBank(scrapy.Spider):
    name = "SpiderBank"
    start_urls = [
        "https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?sector=6&accion=consultarCuadroAnalitico&idCuadro=CA113&locale=es"
    ]

    def parse(self, response):
        html = response.text

        rows = self.__get_text_between(
            html = html,
            starts = """<tr class="cd_tabla_renglon">""",
            ends =   """</tr>"""
        )
        
        for row in rows:
          
            information =  self.__get_text_between(
                html = row,
                starts = """<td valign="bottom">""",
                ends =   """</td>"""
            )
            revenue_information = self.__get_text_between(
                html = row,
                starts = """<td valign="bottom" align="right">""",
                ends =   """</td>"""
            )
           
            yield {
                "Country": information[0],
                "Key": information[1],
                "Divisa": information[2],
                "Dollars": revenue_information[0],
                "MXN": revenue_information[1]
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
