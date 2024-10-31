LOGIN_URL = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
# https://www.linkedin.com/jobs/search/?currentJobId=4061298276&keywords=machine%20learning&location=United%20States
BASE_URL = 'https://www.linkedin.com/jobs/search/?keywords='
LOGIN_USERNAME_fieldID = 'username'
LOGIN_PASSWORD_fieldID = 'password'
LOGIN_SUMBIT_selector = '#organic-div > form > div.login__form_action_container > button'
JOBS_LI = 'ember-view jobs-search-results__list-item occludable-update p0 relative scaffold-layout__list-item'
UNSEEN_JOB_LI = 'ember-view jobs-search-results__job-card-search--generic-occludable-area jobs-search-results__list-item occludable-update p0 relative scaffold-layout__list-item'
JOB_CLASS_CONTAINER_DIV = 'jobs-search-results-list'
JOB_ID_ENTITY = 'data-occludable-job-id'
SKIP_JOB_ENTITY = 25
JOB_URL = 'https://www.linkedin.com/jobs/view/'
SKILL_LINK_SELECTOR = '#how-you-match-card-container > section:nth-child(2) > div > div.pt5 > div:nth-child(3) > div > a'
SKILL_CONTAINER_UL_CLASS = 'job-details-skill-match-status-list'