import requests
from bs4 import BeautifulSoup
from time import sleep

base_url="https://www.codechef.com/"

def get_ratings(username):
		print("Fetching ratings...")
		url = "https://www.codechef.com/users/" + str(username) 
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text)
		sleep(2)
		try:
			codechefname = soup.find("h1", attrs={'class': 'h2-style'}).text
			overall_rating = soup.find("div", attrs={'class': 'rating-number'}).text
			ratings = soup.find('table', attrs={'class': 'rating-table'}).findAll('td')
			long_rating = ratings[1].text
			cookoff_rating = ratings[5].text
			lunch_rating = ratings[9].text
			print('\n\n\n')
			print("Code Chef rating of", codechefname)
			print("Overall Rating: {}\nLong Challenge Rating: {}\nCookoff Rating: {}\nLunch Time Rating: {}"
                  .format(overall_rating, long_rating, cookoff_rating, lunch_rating))
		except Exception:
			print("Something went wrong!")

username = input("Enter the username: ")
get_ratings(username)
#crawl(str(username))

