import json
import requests
from bs4 import BeautifulSoup
import config as c


class DataFetcher:
    def __init__(self, job_title, size=20):
        self.job_title = job_title
        self.size = size
        self.headers = c.HEADERS
        self.base_url = c.BASE_URL
        self.cookie = c.COOKIE
        self.job_ids = []
        self.initialize()

    def initialize(self):
        html_content = self.get_html()
        self.get_job_ids(html_content=html_content)

    def get_html(self):
        url = self.base_url
        while True:
            response = requests.get(url=url,headers=self.headers)
            if response.status_code == 200:
                return response.text

    def get_job_ids(self, html_content):
        soup = BeautifulSoup(html_content, 'lxml')
        job_search_list = soup.find('ul',class_='jobs-search__results-list')




# Example usage
df = DataFetcher(job_title='python')
