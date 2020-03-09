import requests
import json
from bs4 import BeautifulSoup
import random


class RandMovieFinder:

    def get_random_movies(self, genre, num_results):
        movie_pages = self.crawl(genre)
        return self.get_movie_info(num_results, movie_pages)

    # crawl reelgood.com to get movies for a certain genre
    def crawl(self, genre):
        url = f'https://reelgood.com/movies/genre/{genre}'

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        tds = soup.find_all('td', {'class': 'css-1u7zfla e126mwsw1'})
        movie_pages = []

        for t in tds:
            meta = t.find('meta', {'itemprop': 'url'})
            movie_pages.append(meta['content'] + '?amp=true')

        return movie_pages

    def get_movie_info(self, num_results, movie_pages):
        rand_movie_pages = []
        for i in range(num_results):
            rand_movie = random.choice(movie_pages)
            rand_movie_pages.append(rand_movie)
            movie_pages.remove(rand_movie)

        movies = []
        for m in rand_movie_pages:
            r = requests.get(m)
            soup = BeautifulSoup(r.text, 'html.parser')

            # find movie name
            name = soup.find('h1', {'class': 'css-of585f e14injhv7', 'itemprop': 'name'}).text

            # find movie description
            description = soup.find('div', {'class': 'css-1aduz4h ebs2my00'}).find('p').text

            # find movie image
            image = soup.find('div', {'class': 'css-bi0qa e126mwsw1'}).find('img')['src']

            movies.append({
                'name': name, 
                'description': description, 
                'image': image
            })

        return movies

# rmv = RandMovieFinder()
# movies = rmv.get_random_movies('alien', 10)
# print(movies)
