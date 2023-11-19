import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

# spotipy = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="http://example.com",
#         client_id=os.getenv('SPOTIPY_CLIENT_ID'),
#         client_secret=os.environ.get('SPOTIPY_CLIENT_SECRET'),
#         show_dialog=True,
#         cache_path="token.txt",
#         username="tezoriv"
#     )
# )

spotipy = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private"))
user_id = spotipy.current_user()["id"]

# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
#
# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])
#
# for album in albums:
#     print(album['name'])

