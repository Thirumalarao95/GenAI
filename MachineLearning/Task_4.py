#importimng the required packages for my project
import requests
import pandas as pd

#I am creating the empty DataFrame to store the data from all pages of the API response
movies_data = pd.DataFrame()
# I am using for loop to iterate through the pages of the API response and storing the data into the DataFrame
for i in range(1,101):
    print("Loop_Counter:", i)
    #web url & headers for the API request
    url = f"https://api.themoviedb.org/3/movie/changes?api_key=1896085a376ce7dc6fefb17566d03e9&page={i}".format(i)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxODk2MDg1YTM3NmNlN2RjYzZmZWJiMTc1NjZkMDNlOSIsIm5iZiI6MTc3NzQzMjczNi4wMTcsInN1YiI6IjY5ZjE3OGEwODRjNGVhNGI1N2JjYjVlOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9_S9Hh4oVC0vv6BQErDanwJgYz7aCNn2_5a8aCkkaFs"
    }

    #calling the requests using get method and passing the url and headers as parameters
    response = requests.get(url, headers=headers)
    # pinting the response of the API request
    print(response)
    #now converting the response into json then into DataFrame
    page_data = pd.DataFrame(response.json()['results'])
    # now I am concatenating the data from all pages into a single DataFrame
    movies_data = pd.concat([movies_data, page_data], ignore_index=False)


# printing the DataFrame
print(movies_data)
# saving the DataFrame into a CSV file
movies_data.to_csv('D:\TuteDude\GenAI\MachineLearning\Tmdb_movies.csv')