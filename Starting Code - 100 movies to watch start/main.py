import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')

all_movies = soup.find_all("h3", {"class":"title"})

movie_titles = [movie.getText() for movie in all_movies]
reversed_movie_titles = movie_titles[::-1]
print(reversed_movie_titles)

with open("movies.txt","w") as my_file:
    for i in range(len(movie_titles) - 1, -1, -1):
        my_file.write(movie_titles[i] + "\n")