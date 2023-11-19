import requests
import pprint
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

client_id = "2eedfc5090674209b964ca7ea95f2b2b"
client_secret = "ee935f09a03c4dbcbd25174d45fce336"

print("What year would you like to use? Type the date in this format YYYY-MM-DD:")
#date = input()
date = "2000-08-12"
year = date.split("-")[0]
print(year)

URL = f"https://www.billboard.com/charts/hot-100/{date}"
print(URL)

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

song_titles = soup.select("li ul li h3#title-of-a-story")

song_names = [song.getText().strip() for song in song_titles]

print(song_names)

# authenticate with spotipy
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private"))
user_id = sp.current_user()["id"]

song_uris = []
for song in song_names:
    result = sp.search(q='track:' + song + ' year:' + year, type='track')
    try:
        item = result['tracks']['items'][0]['uri']
        print(item)
        song_uris.append(item)
    except IndexError:
        print("song not found in Spotify. skipped")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist['id'],song_uris)