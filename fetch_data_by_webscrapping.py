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
        self.job_class_container_ul = c.JOB_CLASS_CONTAINER_UL
        self.info_container_div = c.INFO_CONTAINER_DIV
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
        job_search_list = soup.find('ul',class_=self.job_class_container_ul)
        container = job_search_list.find_all('div', class_=self.info_container_div)
        for element in container:
            job_entity = element.get('data-entity-urn')
            ur, li, ab, id = job_entity.split(':')
            self.job_ids.append(id)


df = DataFetcher(job_title='python')
