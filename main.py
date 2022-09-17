import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
movies = [title.getText() for title in soup.find_all(name="h3", class_="title")]
with open("movies.txt", "w") as file:
    for movie in reversed(movies):
        file.write(f"{movie}\n")
