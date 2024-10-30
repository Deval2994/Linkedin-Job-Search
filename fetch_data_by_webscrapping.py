import time
import re
import requests
from bs4 import BeautifulSoup
import config as c
from selenium import webdriver
from selenium.webdriver.common.by import By as by


class DataFetcher:
    def __init__(self,username, password, job_title, job_location='United States', size=50):
        self.username = username
        self.password = password
        self.job_title = job_title
        self.job_location = job_location
        self.size = size
        # From config.py
        self.job_url = c.JOB_URL
        self.login_url = c.LOGIN_URL
        self.login_username_fieldid = c.LOGIN_USERNAME_fieldID
        self.login_password_fieldid = c.LOGIN_PASSWORD_fieldID
        self.login_sumbit_selector = c.LOGIN_SUMBIT_selector
        self.job_class_container_div = c.JOB_CLASS_CONTAINER_DIV
        self.job_list = c.JOBS_LIST
        self.unseen_job_list = c.UNSEEN_JOB_LIST
        self.job_skip = c.SKIP_JOB_ENTITY
        self.job_id_entity = c.JOB_ID_ENTITY
        self.job_ids = []
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()

        self.initialize()

    def initialize(self):
        self.do_login()
        if self.check_CAPTCHA():
            input("Capcha Detected...")
        job_url = self.get_job_url()
        self.browser.get(job_url)
        time.sleep(3)
        # container = self.browser.find_element("class name", "jobs-search-results-list")
        # self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", container)
        # time.sleep(13)
        html_source = self.browser.page_source
        self.get_job_ids(html_source,self.job_skip)

    def do_login(self):
        self.browser.get(self.login_url)
        try:
            self.browser.find_element(by.ID, self.login_username_fieldid).send_keys(self.username)
            self.browser.find_element(by.ID, self.login_password_fieldid).send_keys(self.password)
            self.browser.find_element(by.CSS_SELECTOR, self.login_sumbit_selector).click()
        except Exception:
            print('error occurred')


    def check_CAPTCHA(self):
        if re.search('Verification',self.browser.title):
            return True
        return False

    def get_job_url(self):
        job_title = '+'.join(self.job_title.split())
        location = '+'.join(self.job_location.split())
        return f"{self.job_url}{job_title}&location={location}"

    def get_job_ids(self, content,skip):
        soup = BeautifulSoup(content,'lxml')
        job_container = soup.find('div', class_=self.job_class_container_div)
        print(job_container)
        jobs = job_container.find_all('li', class_=self.job_list)
        unseen_jobs = job_container.find_all('li',class_=self.unseen_job_list)
        all_jobs = jobs + unseen_jobs
        for job in all_jobs:
            print(job.get(self.job_id_entity))
        print(len(all_jobs))