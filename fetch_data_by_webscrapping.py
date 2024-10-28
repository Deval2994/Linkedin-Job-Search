import json
import time

import requests
from bs4 import BeautifulSoup
import config as c


class DataFetcher:
    def __init__(self, job_title, job_location='United States', size=20):
        self.job_title = job_title
        self.size = size
        self.headers = c.HEADERS
        self.cookie = c.COOKIE
        self.base_url = c.BASE_URL
        self.job_posting_url = c.job_posting_url
        self.job_class_container_ul = c.JOB_CLASS_CONTAINER_UL
        self.info_container_div = c.INFO_CONTAINER_DIV
        self.job_location = job_location
        self.job_ids = []
        # self.initialize()
        self.tester_method()

    def tester_method(self):
        session = requests.Session()
        job_title = '+'.join(self.job_title.split())
        location = '+'.join(self.job_location.split())
        job_url = f"{self.base_url}{job_title}&location={location}&geoId=101174742&trk=public_jobs_jobs-search-bar_search-submit&original_referer="
        # Make a request to the target URL
        i = 1
        while True:
            response = session.get(job_url, headers=self.headers,cookies=self.cookie)
            # Print the cookies used in the session
            print(response.status_code)
            if response.status_code == 200:
                for cookie in session.cookies:
                    print(f'{i}{cookie.name}: {cookie.value}')
                    i += 1
                break

    def initialize(self):
        html_content = self.get_html()
        self.get_job_ids(html_content=html_content)

    def get_html(self):
        job_title = '+'.join(self.job_title.split())
        location = '+'.join(self.job_location.split())
        job_url = f"{self.base_url}{job_title}&location={location}&geoId=101174742&trk=public_jobs_jobs-search-bar_search-submit&original_referer="
        print(job_url)
        while True:
            response = requests.get(url=job_url, headers=self.headers)
            if response.status_code == 200:
                return response.text

    def abcd(self):
        pass

    def get_job_ids(self, html_content):
        soup = BeautifulSoup(html_content, 'lxml')
        job_search_list = soup.find('ul', class_=self.job_class_container_ul)
        container = job_search_list.find_all('div', class_=self.info_container_div)
        for element in container:
            job_entity = element.get('data-entity-urn')
            ur, li, ab, id = job_entity.split(':')
            self.job_ids.append(id)
            print(id)


df = DataFetcher(job_title='python', job_location='Canada')
