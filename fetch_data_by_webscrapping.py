import time
import re
import pandas as pd
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
        self.base_url = c.BASE_URL
        self.login_url = c.LOGIN_URL
        self.job_url = c.JOB_URL
        self.login_username_fieldid = c.LOGIN_USERNAME_fieldID
        self.login_password_fieldid = c.LOGIN_PASSWORD_fieldID
        self.login_sumbit_selector = c.LOGIN_SUMBIT_selector
        self.job_class_container_div = c.JOB_CLASS_CONTAINER_DIV
        self.job_li = c.JOBS_LI
        self.unseen_job_li = c.UNSEEN_JOB_LI
        self.job_skip = c.SKIP_JOB_ENTITY
        self.job_id_entity = c.JOB_ID_ENTITY
        self.skills_link = c.SKILL_LINK_SELECTOR
        self.skill_container_ul_class = c.SKILL_CONTAINER_UL_CLASS
        self.job_ids = []
        self.start_position = 0
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.data_frame = pd.DataFrame()

        self.initialize()

    def initialize(self):
        self.do_login()
        if self.check_CAPTCHA():
            input("Capcha Detected...")
        self.search_web()
        for job in self.job_ids:
            self.get_job_details(job)
        print('complete?')

    def search_web(self):
        while len(self.job_ids) < self.size:
            self.browser.get(self.get_job_url())
            time.sleep(2)
            html_source = self.browser.page_source
            self.get_job_ids(html_source)
            self.start_position = self.start_position + self.job_skip


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
        return f"{self.base_url}{job_title}&location={location}&start={self.start_position}"

    def get_job_ids(self, content):
        soup = BeautifulSoup(content,'lxml')
        job_container = soup.find('div', class_=self.job_class_container_div)
        jobs = job_container.find_all('li', class_=self.job_li)
        unseen_jobs = job_container.find_all('li',class_=self.unseen_job_li)
        jobs = jobs + unseen_jobs
        for job in jobs:
            if len(self.job_ids) >= self.size:
                break
            self.job_ids.append(job.get(self.job_id_entity))

    def get_job_details(self,job_id):
        job_url = f"{self.job_url}{job_id}/"
        self.browser.get(job_url)
        while True:
            try:
                self.browser.find_element(by.CSS_SELECTOR, self.skills_link).click()
                break
            except Exception:
                continue
        self.get_details()

    def get_details(self):
        skill_container = None
        while skill_container is None:
            html_source = self.browser.page_source
            soup = BeautifulSoup(html_source,'lxml')
            skill_container = soup.find('ul',class_=self.skill_container_ul_class)
        print(skill_container)
