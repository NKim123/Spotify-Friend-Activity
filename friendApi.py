import requests
import json

#retrieves the web access token using the special spotify cookie
def getWebAccessToken(cookie):
    res = requests.get('https://open.spotify.com/get_access_token?reason=transport&productType=web_player', cookies={'sp_dc':cookie}).json() # gets the elevated web access token
    return res['accessToken'] # Return the json object

# retrieves the friend activity using the web access token
def getFriendActivity(webAccessToken):
    res = requests.get('https://guc-spclient.spotify.com/presence-view/v1/buddylist', headers={'Authorization': f'Bearer {webAccessToken}'}) # Gets the list of friend's activity
    return res.json() # Return the json object
