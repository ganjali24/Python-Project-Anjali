# Python-Project-Anjali

A utility script which assists in getting movies information by selecting Genre/Year/runtime.

Modules used:
1. BeautifulSoup
2. Requests
3. pandas

The provided Python script scrapes movie data from IMDb data base on user inputs for genre, year, and movie runtime. It uses the requests library to make HTTP requests, the BeautifulSoup library to parse HTML content, and the pandas library to store and manipulate the scraped data.

Below is the breakdown of how the code works:

1.	It imports the necessary libraries: requests, BeautifulSoup, and pandas.
2.	It defines a list of movie genres called gen_list.
3.	It enters a while loop that prompts the user to select a genre from the gen_list or enter "quit" to exit the program. The loop continues until a valid genre is selected or the user chooses to quit.
4.	It constructs the IMDb URL based on the selected genre.
5.	It sends an HTTP GET request to the IMDb URL and stores the response in the res variable.
6.	It creates a BeautifulSoup object from the HTML content of the response.
7.	It finds all the movie items on the page using the specified HTML class name and stores them in the list_of_movies variable.
8.	It creates an empty pandas DataFrame called movie_dataframe to store the movie data.
9.	It iterates over each movie item in list_of_movies and extracts the movie name, year, and runtime using various BeautifulSoup methods. It handles exceptions if the data is not found.
10.	It creates a dictionary temp_dict with the extracted movie data.
11.	It appends the movie data as a new row to the movie_dataframe DataFrame.
12.	It enters another while loop that prompts the user to select a year from the available options or enter "any" for a random movie. The loop continues until a valid year or "any" is selected.
13.	It filters the movie_dataframe based on the selected year and stores the result in df_yr_filter.
14.	It enters a third while loop that prompts the user to enter a movie runtime or "any" for a random movie. The loop continues until a valid runtime or "any" is entered.
15.	It filters the df_yr_filter DataFrame based on the selected runtime and stores the result in df_rate_filter.
16.	It prints the names of the movies in df_rate_filter.
The code allows users to select a genre, year, and runtime to filter the movie options. If the user enters "any" for any of the options, a random movie is selected from the available options.
