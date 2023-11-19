import os

# os.environ['SPOTIPY_CLIENT_ID'] = 'username'
# os.environ['SPOTIPY_REDIRECT_URI'] = "http://example.com"

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')

print(SPOTIPY_CLIENT_ID)
print(SPOTIPY_CLIENT_SECRET)