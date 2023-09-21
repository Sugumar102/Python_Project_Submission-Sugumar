import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np


url = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'
response = requests.get(url)
response
soup = BeautifulSoup(response.content,'html.parser')

# print(soup)

movie_name = []
genre = []
year = []
time = []
rating = []
metascore = []
votes = []
gross = []

movie_data = soup.findAll('div', attrs={'class' : 'lister-item mode-advanced'})

# print(movie_data)

for store in movie_data:
    name = store.h3.a.text
    movie_name.append(name)
    genre_type = store.p.find('span',class_ = 'genre').text.replace('\n','')
    genre.append(genre_type)
    year_of_release = store.h3.find ('span',class_ = 'lister-item-year text-muted unbold').text.replace('(','').replace(')','')
    year.append(year_of_release)
# print(year_of_release)
    runtime = store.p.find('span',class_ = 'runtime').text
    time.append(runtime)
    rate = store.find('div', class_ = 'inline-block ratings-imdb-rating').text.replace('\n','')    
    rating.append(rate)


# count=np.count_nonzero(movie_name)
# print(count)
movie_DF = pd.DataFrame({'Types of genre' : genre , 'Name of movie' : movie_name,'Year of release' : year, 'Watch time' : time, 'Movie rating' : rating})
# print(movie_DF.head(51))

movie_DF.to_csv('movie_list.csv')
# import pandas as pd

try:
    movie_DF  
  
except FileNotFoundError:
    print("Error: Scraped data file not found.")
    exit(1)
except pd.errors.EmptyDataError:
    print("Error: Scraped data file is empty.")
    exit(1)
except pd.errors.ParserError:
    print("Error: Unable to parse scraped data.")
    exit(1)

# user_search based on the genre
user_search = input("Enter a genre type: ")

# Filter movies by user's input genre
\
filtered_movies = movie_DF[movie_DF['Types of genre'].str.contains(user_search, case=False)]

# Display the movie suggestions
if not filtered_movies.empty:
    print("Here are some movie suggestions based on your search:")
    print(filtered_movies[['Types of genre','Name of movie', 'Year of release', 'Watch time' , 'Movie rating']])
    
else:
    print(f"No movies found for your search '{user_search}'.")

