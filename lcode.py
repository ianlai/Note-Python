import requests
from bs4 import BeautifulSoup
import browsercookie
import json
import ssl
import pprint
PPRINT = pprint.PrettyPrinter(indent=4)

DIFFICULTY_TYPES = ['Easy']

COOKIE_PATH = '/Users/01204086/Library/Application Support/Google/Chrome/Profile 1/Cookies'
WEBSITE_URL = 'https://leetcode.com'
API_URL = 'https://leetcode.com/api/problems/all/'

def GetCookie(website_url, cookie_path):
    myNeedDomainDict = {}
    targetDomain = website_url.split('/')[-1]
    for _ in browsercookie.chrome([cookie_path]):
        if targetDomain in _.domain:
            myNeedDomainDict[_.name] = _.value
    return myNeedDomainDict

if __name__ == '__main__':
    with requests.Session() as s:
        s.cookies.update(requests.utils.cookiejar_from_dict(GetCookie(WEBSITE_URL, COOKIE_PATH)))
        r = s.get(API_URL)
        #print("### header:", "\n", r.headers)
        my_result = json.loads(r.text)
    print('User Name:' , my_result['user_name'])
    my_statistic_data = {key: my_result[key] for key in ['ac_easy', 'ac_hard', 'ac_medium', 'num_solved']}

    count_easy   = 0
    count_medium = 0
    count_hard   = 0
    for q in my_result['stat_status_pairs']:
        if q['difficulty']['level'] == 1:
            count_easy += 1
        if q['difficulty']['level'] == 2:
            count_medium += 1
        if q['difficulty']['level'] == 3:
            count_hard += 1
    print('Solved / Total (Easy)  :' , my_result['ac_easy']   , '/', count_easy)
    print('Solved / Total (Medium):' , my_result['ac_medium'] , '/', count_medium)
    print('Solved / Total (Hard)  :' , my_result['ac_hard']   , '/', count_hard)
    print('Solved / Total (All)   :' , my_result['num_solved'], '/', my_result['num_total'])
    
            #print(q['stat']['question_id'], q['stat']['question__title'])