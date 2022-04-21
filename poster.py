import requests

response=requests.get("https://www.omdbapi.com/?i=tt2194499&apikey=4f73af2f")
movie_block=response.json()
print(movie_block)
print(movie_block['Poster'])
