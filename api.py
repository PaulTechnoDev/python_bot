import requests
import os
from dotenv import load_dotenv

load_dotenv()

def getTwitchusers(params):
    body = {
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
        "grant_type": 'client_credentials'
    }
    auth = requests.post('https://id.twitch.tv/oauth2/token', body)
    keys = auth.json()
    API_HEADERS = {
        'Client-ID': body.__getitem__('client_id'),
        'Authorization': 'Bearer ' + keys['access_token'],
    }
    streamers = []
    url = 'https://api.twitch.tv/helix/streams'
    try:
        req = requests.Session().get(url, params=params, headers=API_HEADERS)
        jsondata = req.json()
        for item in jsondata['data']:
            type = item['type']
            if type == 'live':
                streamers.append(item['user_name'] + ' : https://www.twitch.tv/' + item['user_login'])
        print(streamers)
        if not streamers:
            return ['В данный момент стримов не найдено']
        else:
            return streamers

    except Exception as e:
        print("Error checking user: ", e)
        return []


def getGGusers(users):
    url = f'https://goodgame.ru/api/getchannelstatus?id={users}&fmt=json'
    streamers = []
    try:
        req = requests.Session().get(url)
        jsondata = req.json()
        print(jsondata)

        for key, value in jsondata.items():
            status = value['status']
            if status == 'Live':
                streamers.append(value['key'] + ' : https://goodgame.ru/channel/' + value['key'])
        return streamers
    except Exception as e:
        print("Error checking user: ", e)
        return []

# def getTrovoUsers():
#     url = 'https://trovo.live/s/gantver1'
#     try:
#         req = requests.Session().get(url)
#         jsondata = req.json()
#         print(jsondata)
#     except Exception as e:
#         print("Error checking user: ", e)
#         return []
# getTrovoUsers()