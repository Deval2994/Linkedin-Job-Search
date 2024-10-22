import requests
from bs4 import BeautifulSoup
import config as c


class DataFetcher():
    def __init__(self, job_title, size):
        self.job_title = job_title
        self.size = size
        self.headers = c.HEADERS
        self.base_url = c.BASE_URL
        self.job_class_container = c.JOB_CLASS_CONTAINER
        self.initialize()

    def initialize(self):
        webpage_code = self.get_html()
        job_class_container = self.get_job_containers(webpage=webpage_code, classid=self.job_class_container)

    def get_html(self):
        job_title = '+'.join(self.job_title.split())
        url = f'{self.base_url}+{job_title}'
        while True:
            response = requests.get(url=url, headers=self.headers)
            if str(response)[11:14] == "200":
                return response.text

    def get_job_containers(self, webpage, classid):
        container_class = classid
        soup = BeautifulSoup(webpage, 'lxml')
        return soup.find_all('ul', class_=container_class)

    def get_skills(self):
        pass

    def get_additional_details(self):
        pass
