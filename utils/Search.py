from bs4 import BeautifulSoup
import requests
import json

from utils.Log import Log

class Search(Log):

    def __init__(self, query: str) -> None:
        self.start_time()
        self._url = f"https://www.google.com.br/search?q={query}&tbs=li:1"
        self._headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}   

    
    def search(self) -> str:
        response = requests.get(self._url, headers=self._headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        elements_search = soup.find_all("div", class_="g")

        return self.extract_value_elements(elements_search)

    
    def extract_value_elements(self, elements: list) -> str:
        values = []
        for i in range(0, 5):
            try:
                title = elements[i].find_all("h3", class_="LC20lb MBeuO DKV0Md")[0].text
                description = elements[i].find_all("div", class_="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf")[0].text
                link = elements[i].find_all("a")[0].get('href')
            except:
                ...
          
            value = {
                "id" : i,
                "Title" : title,
                "Description" : description,
                "Link" : link
            }

            values.append(value)
            
        self.end_time()

        value_time = {
            "Tempo médio de execução" : self.time_result() 
        }

        values.append(value_time)

        return json.dumps(values)
    