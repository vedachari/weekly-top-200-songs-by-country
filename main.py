import sys
import spotipy
import spotipy.util as util
from playlistgenerator import get_playlist_by_country_and_length
from decouple import config
import os

scope = 'user-library-read'

print(len(sys.argv))
if len(sys.argv) == 3:
    username = sys.argv[1]
    country = sys.argv[2]
elif len(sys.argv)==4:
    username = sys.argv[1]
    country = sys.argv[2] +" "+ sys.argv[3]
elif len(sys.argv)==5:
    username = sys.argv[1]
    country = sys.argv[2] +" "+ sys.argv[3] +" "+ sys.argv[4] 
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()
# Set your Spotify API credentials ()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
client_id = config('CLIENT_ID') #client id
client_secret = config('CLIENT_SECRET') #client secret
redirect_uri = config('REDIRECT_URI') #set to flight buddy website

token = 'Bearer '+util.prompt_for_user_token(username,
                                   scope,
                                   client_id=client_id,
                                   client_secret=client_secret,
                                   redirect_uri=redirect_uri)
print(username)
print(country)
get_playlist_by_country_and_length(country.lower(), token)
