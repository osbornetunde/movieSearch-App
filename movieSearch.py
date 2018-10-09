import requests
import collections

MovieResult = collections.namedtuple(
	'MovieResult',
	"imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres")

def find_movies(search_text):
	url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search_text)

	resp = requests.get(url)
	resp.raise_for_status()

	movie_data = resp.json()
	movies_list = movie_data.get('hits')

	movies = [
		MovieResult(**md)
		for md in movies_list
	]

	movies.sort(key=lambda m: -m.year)

	return movies


# print("Found {} movies for search {}".format(len(movies), search))
# for m in movies:
# 	print("{} -- {}".format(m.year, m.title))
