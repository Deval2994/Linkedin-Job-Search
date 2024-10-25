import time
import requests
from bs4 import BeautifulSoup
import config as c
from selenium import webdriver
import confidential


class DataFetcher():
    def __init__(self, user_name, password, job_title, size):
        self.job_title = job_title
        self.size = size
        self.headers = c.HEADERS
        self.payload = c.PAYLOAD
        self.base_url = c.BASE_URL
        self.login_url = c.LOGIN_URL
        self.job_class_container = c.JOB_CLASS_CONTAINER
        self.user_name = user_name
        self.password = password
        self.session = requests.Session()  # Use the same session for all requests

        self.initialize()

    def initialize(self):
        payload_data = self.get_payload_data(username_=self.user_name, password_=self.password,)
        print(payload_data)
        cookie = self.get_cookie()
        if payload_data:
            self.linkedin_login(payload_=payload_data, cookie_=cookie)

    def get_cookie(self):
        response = self.session.get(self.login_url)
        # Check if the request was successful
        if response.status_code == 200:
            # Extract cookies from the response
            cookies = response.cookies.get_dict()

            # Convert cookies to the format required for headers
            cookie_header = '; '.join([f'{key}={value}' for key, value in cookies.items()])
            return cookie_header
        else:
            print("Failed to retrieve the login page. Status code:", response.status_code)
            return None

    def get_payload_data(self, username_,password_):
        response = self.session.get(self.login_url)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract necessary tokens and parameters
            loginCsrfParam = soup.find('input', {'name': 'loginCsrfParam'})['value']
            csrfToken = soup.find('input', {'name': 'csrfToken'})['value']
            sIdString = soup.find('input', {'name': 'sIdString'})['value']
            parentPageKey = soup.find('input', {'name': 'parentPageKey'})['value']
            pageInstance = soup.find('input', {'name': 'pageInstance'})['value']
            apfc = soup.find('input', {'name': 'apfc'})['value']

            return {
                'session_key' : username_,
                'session_password' : password_,
                'loginCsrfParam': loginCsrfParam,
                'csrfToken': csrfToken,
                'sIdString': sIdString,
                'parentPageKey': parentPageKey,
                'pageInstance': pageInstance,
                'apfc': apfc
            }
        else:
            print("Failed to retrieve the login page. Status code:", response.status_code)
            return None

    def linkedin_login(self, payload_, cookie_):
        payload = self.payload
        headers = self.headers
        payload.update(payload_)
        headers.update(cookie_)
        login_response = self.session.post(url=self.login_url, data=payload, headers=headers)

        if login_response.status_code == 200 and "successful" in login_response.text.lower():
            print("Login successful!")
        else:
            print("Login failed. Response:", login_response.text)

    def get_html(self):
        pass

    def get_job_containers(self, webpage, classid):
        pass

    def get_skills(self, job_container, skillsid):
        pass

    def get_additional_details(self):
        pass


username = confidential.USERNAME
password = confidential.PASSWORD
# Example usage
DataFetcher(user_name=username, password=password, job_title='Machine Learning', size=0)
