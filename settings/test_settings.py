
from pysis.settings.settings import *

DEBUG = False

INSTALLED_APPS = list(INSTALLED_APPS)
# django-sane-testing is throwing errors when south is enabled. So disable south
INSTALLED_APPS.remove('south')

TEST_USERNAME = '09mca099'
TEST_USER_PASSWORD = 'p'

LOGIN_URL = '/admin/'

PUBLIC_URLS = [
    '/',

    '/password/reset',
    '/password/reset/done',
    '/password/reset/complete',
]

PRIVATE_URLS = [
    #'/admin',
    #'/browse',
    '/myprofile',
    '/students',
    #'/attendance',
    #'/library',
    #'/marks',

    '/myprofile/general',
    '/myprofile/personal',
    '/myprofile/family',
    '/myprofile/contact',
    '/myprofile/education',
    '/myprofile/misc',
    '/myprofile/general/edit',
    '/myprofile/personal/edit',
    '/myprofile/family/edit',
    '/myprofile/contact/edit',
    '/myprofile/education/edit',
    '/myprofile/misc/edit',

    '/myprofile/avatar/change',
    '/myprofile/avatar/delete',

    '/students/search/?q=all',
    '/students/search/?q=ram',
    '/students/search/?q=somejunk',

    '/students/browse',
    '/students/browse/MCA',
    '/students/browse/MCA/2009',

    '/students/browse/myclassmates',
    '/students/browse/myjuniors',
    '/students/browse/myseniors',
    '/students/browse/somejunk',

    '/students/display/09mca099',

    #'/password_change',
]


URLS_TO_TEST = PUBLIC_URLS + PRIVATE_URLS

# Test urls ending with / also
URLS_TO_TEST += [url + '/' for url in URLS_TO_TEST]
PUBLIC_URLS  += [url + '/' for url in PUBLIC_URLS]
PRIVATE_URLS  += [url + '/' for url in PRIVATE_URLS]
