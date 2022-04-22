from friendApi import getWebAccessToken, getFriendActivity
from dotenv import load_dotenv
import threading
import datetime
import os


load_dotenv()

def main():
    threading.Timer(300.0, main).start()
    token = os.getenv('SPOTIFY_TOKEN')
    accessToken = getWebAccessToken(token)
    friendActivity = getFriendActivity(accessToken)

    # printing friend activity
    for (i, friend) in enumerate(friendActivity['friends']):
        print(f'{i+1}. {friend["user"]["name"]} at {(datetime.datetime.fromtimestamp(int(friend["timestamp"])/1000)).strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'\t{friend["track"]["name"]} by {friend["track"]["artist"]["name"]}')
        print(f'\tLink: https://open.spotify.com/track/{friend["track"]["uri"][14:]}')
        print('\n')

main()