import facebook
import os
import config

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)


api = facebook.GraphAPI(ACCESS_TOKEN)
posts = api.get_connections(id='me', connection_name='posts')

for post in posts['data']:
    print(post['id'])
    api.delete_object(id=post['id'])


