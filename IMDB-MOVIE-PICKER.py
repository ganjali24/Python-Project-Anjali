import requests as r
from bs4 import BeautifulSoup
import pandas as pd
import random

gen_list = ['action', 'adventure',
               'animation', 'biography',
               'comedy', 'crime',
               'documentary', 'drama',
               'family', 'fantasy',
               'film-noir', 'history',
               'horror', 'music', 'musical',
               'mystery', 'romance', 'sci-fi',
               'short', 'sport', 'thriller',
               'war', 'western']

while True:
    print("Please select a genre from the list or type quit\n", '\n'.join(gen_list))
    gen = input()
    if gen.lower() in gen_list:
        break
    elif gen.lower() == 'quit':
        exit()
    else:
        print("please provide the right genre, type again. Thank you")


imdb = fr'https://www.imdb.com/search/title/?genres={gen}&explore=genres&title_type=feature&ref_=ft_movie_0'
res = r.get(imdb)

soup = BeautifulSoup(res.content.decode(), "html.parser")

list_of_movies = soup.find_all("div", class_='lister-item mode-advanced')

movie_dataframe = pd.DataFrame()

for o_movie in list_of_movies:

    try:
        movie_name = str(o_movie.find('h3', class_="lister-item-header").a.get_text())
    except:
        movie_name = ''
    try:
        year = str(o_movie.find('h3', class_="lister-item-header").find(
            class_="lister-item-year text-muted unbold").get_text()).strip('(').strip(')')
        year = int(''.join(filter(str.isdigit, year)))
    except:
        year = ''

    try:
        run_time = str(o_movie.find_all('p').__getitem__(0).find_all('span').__getitem__(2).get_text()).strip(
            ' ').strip('')
        run_time = int(''.join(filter(str.isdigit, run_time)))
    except:
        run_time = 0

    temp_dict = {'name': [movie_name], 'year': [year], 'run_time': [run_time]}

    movie_dataframe = movie_dataframe.append(pd.DataFrame(temp_dict), ignore_index=True)

while True:
    yr = input(f'Please select a year of a movie from list {movie_dataframe["year"].unique()} or for any random movie type "any" \n')
    if str(yr) in list(movie_dataframe["year"].astype(str).unique()):
        df_yr_filter = movie_dataframe[movie_dataframe["year"].astype(str) == str(yr)]
        break
    elif yr == "any":
        df_yr_filter = movie_dataframe
        break
    else:
        print("Invalid Input provided, please provide the correct inptut")

while True:
    movie_runtime = input(f'Please provide the movie runtime (in mins) or "any" for random movie pick \n')
    if movie_runtime.isdigit():
        df_rate_filter = df_yr_filter[df_yr_filter["run_time"] >= int(movie_runtime)]
        print('\n'.join(df_rate_filter["name"].unique()))

        break
    elif movie_runtime == "any":
        df_rate_filter = df_yr_filter
        print('\n'.join(df_rate_filter["name"].unique()))
        break
    else:
        print("Invalid Input provided, please provide the valid rating")




