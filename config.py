"""
Description: This file contain the information of web source which later used in automation (selenium) and
             web scrapping (BeautifulSoup) for extracting the data.
"""

LOGIN_URL = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
BASE_URL = 'https://www.linkedin.com/jobs/search/?keywords='
LOGIN_USERNAME_fieldID = 'username'
LOGIN_PASSWORD_fieldID = 'password'
LOGIN_SUMBIT_selector = '#organic-div > form > div.login__form_action_container > button'
JOBS_LI = 'ember-view jobs-search-results__list-item occludable-update p0 relative scaffold-layout__list-item'
UNSEEN_JOB_LI = 'ember-view jobs-search-results__job-card-search--generic-occludable-area jobs-search-results__list-item occludable-update p0 relative scaffold-layout__list-item'
UNSEEN_JOB_LI_FULLPATH = '#/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[8]'
JOB_CLASS_CONTAINER_DIV = 'jobs-search-results-list'
JOB_ID_ENTITY = 'data-occludable-job-id'
SKIP_JOB_ENTITY = 25
JOB_URL = 'https://www.linkedin.com/jobs/search/?keywords=Machine%20Learning&currentJobId='
SKILL_TEXT_A = 'app-aware-link job-details-how-you-match__skills-item-subtitle t-14 overflow-hidden'
SKILL_TEXT_A_FULLPATH = '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[6]/section[1]/div/h2'
SKILL_TEXT_BTN_FULLPATH = '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/button/div[3]'
SKILL_CONTAINER_UL = 'list-style-none mt2'
SKILLS_TEXT_CLASS = 'text-body-small'
CLOSE_SKILL_BTN = '/html/body/div[4]/div/div/button'
SKILL_TEXT_A_2 = 'app-aware-link job-details-how-you-match__skills-section-descriptive-skill t-14'
JOB_POSITION_H1_CLASS = 't-24 t-bold inline'
JOB_TYPE_SPAN_CLASS = 'ui-label ui-label--accent-3 text-body-small'
JOB_TYPE_SPAN_CLASS_2 = 'job-details-jobs-unified-top-card__job-insight-view-model-secondary'
COMPANY_NAME_DIV_CLASS = 'job-details-jobs-unified-top-card__company-name'
COMPANY_NAME_TEXT_CLASS = 'app-aware-link'
JOB_LINK_FULLPATH = '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[6]/div/div/div/button'
JOB_LINK_LOCATION_POPUP_ID = 'jobs-apply-header'
EASY_APPLY_SPAN_FULLPATH = '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[5]/div/div/div/button/span'
CONTINUE_APPLYING_FULLPATH = '/html/body/div[4]/div/div/div[3]/div/div/button'
APPLY_BTN_FULLPATH = '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[5]/div/div/div/button/span'