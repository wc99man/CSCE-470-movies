# CSCE-470-movies
The data set for our project was found here https://www.imdb.com/interfaces/ We are using title.akas.tsv.gz, title.basics.tsv.gz, title.crew.tsv.gz, title.principals.tsv.gz, title.ratings.tsv.gz, name.basics.tsv.gz.

The data set was first cleaned and filtered to include movie title, titleId, genre, average rating, runtime, and year. Our data was loaded into a dictionary which will be then introduced into our KNN classification system. 

To run 470.py (Clean/filters data and generates dictionary with movie name and its attributes): 
- Install python3 
- Install pandas: 'pip3 install pandas'
- Make sure you are able to import math
- Download and unzip the title.akas.tsv.gz, title.basics.tsv.gz, title.crew.tsv.gz, title.ratings.tsv.gz, and name.basics.tsv.gz files from the IMBD page linked here (https://datasets.imdbws.com/).


We currently plan on using an altered version of KNN classification system to provide movie recommendations.

The strong features are: Title, Genre

The weak features are: Startyear, Runtime, Ratings

We hope to eventually include directors, writers, and actors, but those are a bit harder for use to parse through currently.
