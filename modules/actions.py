import json
import os
import config
from facebook_handler import post_to_facebook

SITE_ROOT = os.environ.get('SITE_ROOT', config.SITE_ROOT)
RESULTS_PATH = os.path.join(SITE_ROOT, "PUBLISHED_RESULTS.json")
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)

def take_action(details,setup):
    with open(RESULTS_PATH, 'r') as fp:
        results = json.load(fp)

    action_flag = True
    for result in results:
        if match(result, details):
            action_flag = False
            break

    if action_flag:
        try:
            if setup==False:
                post_to_facebook(details)
            register_results(details)
        except:
            print("FB API ERROR")


    return

def match(resultFields, details):
    #print("result", resultFields)
    matchBool = True
    try:
        for i in xrange(len(details)):
            if details[i]!=resultFields[i]:
                matchBool = False
    except:
        print("INDEX ERROR", details, resultFields)

    return matchBool

def register_results(details):
    #print('registering details: ',details)
    with open(RESULTS_PATH, 'r') as fp:
        results = json.load(fp)

    new_result = []
    for detail in details:
        new_result.append(detail)

    results.append(new_result)

    with open(RESULTS_PATH, 'w') as fp:
        json.dump(results, fp, indent=-1)

    return