import requests
import collections

MovieResult = collections.namedtuple(
	'MovieResult',
	"imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres")

search = input("What movie do you want to search for? ")
url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search)

resp = requests.get(url)
resp.raise_for_status()

movie_data = resp.json()
movies_list = movie_data.get('hits')

movies = []
for md in movies_list:
	m = MovieResult(
		imdb_code=md.get('imdb_code'),
		title=md.get('title'),
		duration= md.get('duration'),
		director = md.get('director'),
		year=md.get('year'),
		rating = md.get('rating'),
		imdb_score = md.get('imdb_score'),
		keywords = md.get('keywords'),
		genres = md.get('genres')
	)
	movies.append(m)

print("Found {} movies for search {}".format(len(movies), search))
for m in movies:
	print("{} -- {}".format(m.year, m.title))
