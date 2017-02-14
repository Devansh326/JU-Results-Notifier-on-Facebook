import facebook
import os
import config

PAGE_ID = os.environ.get('PAGE_ID', config.PAGE_ID)
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)


def post_to_facebook(details):
    message = formatter(details)
    cfg = {
        "page_id"      : PAGE_ID,
        "access_token" : ACCESS_TOKEN
    }

    api = facebook.GraphAPI(cfg['access_token'])
    status = api.put_wall_post(message)
    #print status

def formatter(details):

    message = 'RESULTS OUT\n'
    if details[1]=='Undergraduate (Semester System)':
        message += 'UG '
    elif details[1]=='Postgraduate (Semester System)':
        message += 'PG '

    message += details[6]+'\n'+details[3]+', '+details[4]
    if details[5]!='Regular':
        message += ', Supple'

    message += '\n'+str(details[2])
    print(message)
    return message