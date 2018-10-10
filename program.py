import movieSearch
import requests


def main():
	print_header()
	search_event_loop()


def print_header():
	print('--------------------------------')
	print('          Movie Search')
	print('--------------------------------')




def search_event_loop():
	search = 'ONCE_THROUGH_LOOP'

	while search != 'x':
		try:
			search = input('Movie search text (x to exit): ')
			if search != 'x':
				results = movieSearch.find_movies(search)
				print("Found {} results.".format(len(results)))
				for r in results:
					print('{} -- {}'.format(r.year, r.title))
				print()
		except ValueError:
			print("Please, you need to enter a search text")
		except requests.exceptions.ConnectionError:
			print("Sorry, It seems your network is down.")
		except Exception as x:
			print("Ooh!, Something went wrong! Details: {}".format(x))

	print('exiting....')






if __name__ == '__main__':
	main()