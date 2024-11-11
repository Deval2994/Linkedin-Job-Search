"""
Description: This Python script automates job scraping from a website using Selenium and BeautifulSoup.
             It logs into the website with provided credentials, searches for job listings based on the user's
             input (job title, location, etc.), and extracts job details like company name, position, job type, skills,
             and application links. The data is stored in a Pandas DataFrame and can be further processed or exported.
             The script handles CAPTCHA, pagination, and even extracts skills by interacting with elements on the page.
"""

import re
import time
import pandas as pd
from bs4 import BeautifulSoup
import config as c
from selenium import webdriver
from selenium.webdriver.common.by import By as by


class DataFetcher:
    # Constructor to initialize essential variables such as login credentials, job search details, and setup the WebDriver for browser automation.
    def __init__(self, username, password, job_title, job_location='United States', size=50):
        self.username = username
        self.password = password
        self.job_title = job_title
        self.job_location = job_location
        self.size = size

        # Retrieve configurations from config.py for URLs, field IDs, selectors, etc.
        self.base_url = c.BASE_URL
        self.login_url = c.LOGIN_URL
        self.job_url = c.JOB_URL
        self.login_username_fieldid = c.LOGIN_USERNAME_fieldID
        self.login_password_fieldid = c.LOGIN_PASSWORD_fieldID
        self.login_sumbit_selector = c.LOGIN_SUMBIT_selector
        self.job_class_container_div = c.JOB_CLASS_CONTAINER_DIV
        self.job_li = c.JOBS_LI
        self.unseen_job_li = c.UNSEEN_JOB_LI
        self.unseen_job_li_fullpath = c.UNSEEN_JOB_LI_FULLPATH
        self.job_skip = c.SKIP_JOB_ENTITY
        self.job_id_entity = c.JOB_ID_ENTITY
        self.skill_text_a = c.SKILL_TEXT_A
        self.skill_text_a_2 = c.SKILL_TEXT_A_2
        self.skill_text_btn_fullpath = c.SKILL_TEXT_BTN_FULLPATH
        self.skill_container_ul = c.SKILL_CONTAINER_UL
        self.skill_text_class = c.SKILLS_TEXT_CLASS
        self.close_skill_btn = c.CLOSE_SKILL_BTN
        self.skill_text_a_fullpath = c.SKILL_TEXT_A_FULLPATH
        self.job_position_h1_class = c.JOB_POSITION_H1_CLASS
        self.job_type_span_class = c.JOB_TYPE_SPAN_CLASS
        self.job_type_span_class_2 = c.JOB_TYPE_SPAN_CLASS_2
        self.company_name_div_class = c.COMPANY_NAME_DIV_CLASS
        self.company_name_text_class = c.COMPANY_NAME_TEXT_CLASS
        self.job_link_fullpath = c.JOB_LINK_FULLPATH
        self.job_link_location_popup_id = c.JOB_LINK_LOCATION_POPUP_ID
        self.easy_apply_span = c.EASY_APPLY_SPAN_FULLPATH
        self.apply_btn_full_path = c.APPLY_BTN_FULLPATH
        self.continue_applying = c.CONTINUE_APPLYING_FULLPATH

        self.job_ids = []  # Store the fetched job IDs.
        self.start_position = 0  # Keep track of pagination position for job search results.

        # Initialize WebDriver for browser automation using Chrome.
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()

        # Define the structure of the DataFrame to store job details.
        columns = ['Company Name', 'Position', 'Job Type', 'Skills', 'Job Link', 'Job Id']
        self.data_frame = pd.DataFrame(columns=columns)

        self.initialize()

    def initialize(self):  # Main function to start login, handle CAPTCHA, and fetch job details.
        self.do_login()  # Perform login process.
        while self.check_CAPTCHA():  # Loop until CAPTCHA verification is cleared.
            continue
        self.search_web()  # Start job search.
        for job in self.job_ids:  # Fetch details for each job ID.
            print(job)
            self.get_job_details(job)

    def search_web(self):  # Function to perform job search based on given criteria.
        while len(self.job_ids) < self.size:  # Continue fetching job IDs until required size is reached.
            self.browser.get(self.get_job_url())  # Fetch new page of job listings.
            time.sleep(2)
            html_source = self.browser.page_source
            self.get_job_ids(html_source)  # Extract job IDs from the HTML content.
            self.start_position = self.start_position + self.job_skip  # For pagination

    def do_login(self):  # Function to log into the website using the provided credentials.
        self.browser.get(self.login_url)
        while True:
            try:
                self.browser.find_element(by.ID, self.login_username_fieldid).send_keys(self.username)
                self.browser.find_element(by.ID, self.login_password_fieldid).send_keys(self.password)
                self.browser.find_element(by.CSS_SELECTOR, self.login_sumbit_selector).click()
                break
            except Exception:
                continue

    def check_CAPTCHA(self):  # Function to check if CAPTCHA is present on the page.
        if re.search('Verification', self.browser.title):  # Check if the title contains 'Verification'.
            return True
        return False

    def get_job_url(self):  # Function to generate the job search URL based on job title and location.
        job_title = '+'.join(self.job_title.split())
        location = '+'.join(self.job_location.split())
        return f"{self.base_url}{job_title}&location={location}&start={self.start_position}"

    def get_job_ids(self, content):  # Function to extract job IDs from the page content using BeautifulSoup.
        soup = BeautifulSoup(content, 'lxml')
        job_container = soup.find('div', class_=self.job_class_container_div)
        jobs = job_container.find_all('li', class_=self.job_li)
        unseen_jobs = job_container.find_all('li', class_=self.unseen_job_li)
        jobs = jobs + unseen_jobs  # Combine both seen and unseen jobs.
        for job in jobs:
            if len(self.job_ids) >= self.size:  # Stop if enough job IDs are collected.
                break
            self.job_ids.append(job.get(self.job_id_entity))

    def get_job_details(self, job_id):  # Function to fetch job details like position, job type, company name, skills, and apply link.
        job_url = f"{self.job_url}{job_id}"  # Build job-specific URL.
        self.browser.get(job_url)
        time.sleep(2)
        html_source = self.browser.page_source
        bs = BeautifulSoup(html_source, 'lxml')

        # Extract job details from the page.
        position = self.get_position(bs)
        job_type = self.get_job_type(bs)
        company_name = self.get_company_name(bs)
        skills = self.get_skills()
        apply_link = self.get_apply_link(job_id,bs)

        # Add the extracted details as a new row in the DataFrame.
        new_row = pd.DataFrame([{
            'Company Name': company_name,
            'Position': position,
            'Job Type': job_type,
            'Skills': skills,
            'Job Link': apply_link,
            'Job Id': job_id
        }])

        self.data_frame = pd.concat([self.data_frame, new_row], ignore_index=True)

    def get_company_name(self, soup):  # Function to extract company name from the page using BeautifulSoup.
        name_element = soup.find('div', class_=self.company_name_div_class).find('a',class_=self.company_name_text_class)
        return name_element.getText()

    def get_apply_link(self, job_id, soup):  # Function to get the application link for a job. If "Easy Apply" is available, the LinkedIn job URL is used.

        container = soup.find('div', class_='jobs-apply-button--top-card')
        btn_text = container.find('span', class_='artdeco-button__text').getText().strip()

        if btn_text == 'Easy Apply':  # Check whether application is on company site or on LinkedIn.
            return f"https://www.linkedin.com/jobs/view/{job_id}/"

        # Click the apply button if it's not 'Easy Apply'
        while True:
            try:
                self.browser.find_element(by.XPATH, self.apply_btn_full_path).click()
                break
            except Exception:
                continue

        # Try to click on continue applying button if it's available
        try:
            self.browser.find_element(by.XPATH, self.continue_applying).click()
        except Exception:
            pass

        # Refresh the page and switch to the job application window
        self.browser.refresh()
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.refresh()

        # Get the job URL and return it
        job_url = self.browser.current_url
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

        return job_url

    def get_skills(self):  # Function to extract skills required for a job by clicking and scraping the skills section.
        skills_list = ''

        # Click the button to reveal skills
        try:
            self.browser.find_element(by.XPATH, self.skill_text_btn_fullpath).click()
        except Exception:
            return 'Please check on website; Skills not found'

        time.sleep(1)

        soup = BeautifulSoup(self.browser.page_source, 'lxml')

        self.browser.find_element(by.XPATH,self.close_skill_btn).click()
        try:
            # Locate the skills container
            skills_container = soup.find_all('ul', class_=self.skill_container_ul)[1]
            combined_skills_list = skills_container.find_all('span', class_=self.skill_text_class)

            # Loop through and collect each skill
            for skills in combined_skills_list:
                skills_list += '; ' + skills.getText().strip()

            # Clean the list and return it
            return skills_list.replace('and ', '')[2:]
        except Exception:
            return 'Please check on website; Unexpected error occurs'


    def get_position(self, soup):  # Function to extract job position from the page.
        job_position = soup.find('h1', class_=self.job_position_h1_class)
        return job_position.getText()

    def get_job_type(self, soup):  # Function to extract job type (full-time, part-time, etc.) from the page.
        job_type = ''
        job_type_element = soup.find_all('span', class_=[self.job_type_span_class, self.job_type_span_class_2])

        for element in job_type_element:
            each_element = element.find_all('span', {'aria-hidden': 'true'})
            for job in each_element:
                if job is not None and job.text not in job_type:
                    job_type = job_type + '; ' + job.text.strip()

        return job_type[2:]
