from flask import Flask, render_template, request, redirect, send_file
import requests
import json
import pandas as pd
import numpy as np
import math


# pd.options.display.width = 0

title_merged = pd.read_csv('Data/output.csv')
title_merged['runtimeMinutes'] = title_merged['runtimeMinutes'].replace('\\N','0')
title_merged['genres'] = title_merged['genres'].replace('\\N','None')

#Converts title_merged df into dictionary (Format --> {movieName : {'titleId' : ..., 'Year': ..., etc.)
title_dict = {title_merged['title'][index]:{} for index in title_merged.index}

for index in title_merged.index:
    movieName = title_merged['title'][index]
    title_dict[movieName] = {title_merged['titleId'][index] : 0, title_merged['startYear'][index] : 0, title_merged['runtimeMinutes'][index] : 0, title_merged['genres'][index] : 0, title_merged['averageRating'][index] : 0, title_merged['directors'][index] : 0, title_merged['writers'][index] : 0}

def predict(moviename, moviedict):  ##### we need the name of the movie so we can make a new vector for it

    givenvector = {}
    movies_list = []

    ######Need these to store the winning movie
    mov1 = "None"
    mov2 = "None"
    mov3 = "None"
    win1 = 0
    win2 = 0
    win3 = 0

    #####need to make our given movies vector space
    for movie in moviedict:
        if movie == moviename:
            givenvector = moviedict[movie]
            # moviedict.pop(movie)


    if givenvector == {}:  #####just some basic error checking to make sure we found a movie
        print("Movie not found. Please check that you entered the official movie title.")
        return {}
    ####this is the best way I found to set a value at a specific entry location in a dict
    key = list(givenvector)[0]
    givenvector[key] = 0  ######### we need to set to what ever value we want
    key = list(givenvector)[1]
    givenvector[key] = 5  ######### we need to set to what ever value we want
    key = list(givenvector)[2]
    givenvector[key] = 3  ######### we need to set to what ever value we want
    key = list(givenvector)[3]
    givenvector[key] = 20  ######### we need to set to what ever value we want
    key = list(givenvector)[4]
    givenvector[key] = 10  ######### we need to set to what ever value we want

    for movie in moviedict:  ####now we need to set up the movie vectors and run the comparisons
        bmovie = moviedict[movie]  ####get the dict for current movie
        # for i in bmovie:
        #     print(i)
        if list(givenvector)[0] == list(bmovie)[0]:
            key = list(bmovie)[0]
            bmovie[key] = 1
            continue
        if list(givenvector)[1] == list(bmovie)[1]:
            key = list(bmovie)[1]
            bmovie[key] = 1
        if abs(int(list(bmovie)[2])-int(list(givenvector)[2])) <= 15:
            key = list(bmovie)[2]
            bmovie[key] = 1
        if list(givenvector)[3] == list(bmovie)[3]:
            key = list(bmovie)[3]
            bmovie[key] = 1
        if abs(float(list(bmovie)[4])-float(list(givenvector)[4])) <= 1:
            key = list(bmovie)[4]
            bmovie[key] = 1
    ####start the knn equation
        abot = 0
        for word in givenvector:
            abot += givenvector[word] * givenvector[word]
        asbot = math.sqrt(abot)
        # print(asbot)

        bbot = 0
        for word in bmovie:
            bbot += bmovie[word] * bmovie[word]
        bsbot = math.sqrt(bbot)


        bot = bsbot * asbot
        top = 0
        for word in givenvector:  ######this section might be scuffed or redundant since we already did a comparison
            for word2 in bmovie:
                if word == word2:
                    top += givenvector[word] * bmovie[word]

        ##########determine a minner
        simularity = top / bot if bot > 0 else 0
        if simularity > win1:
            win3 = win2
            mov3 = mov2
            win2 = win1
            mov2 = mov1
            win1 = simularity
            mov1 = movie
        elif simularity > win2:
            win3 = win2
            mov3 = mov2
            win2 = simularity
            mov2 = movie
        elif simularity > win3:
            win3 = simularity
            mov3 = movie

    
    rec_movies = []
    
    result_dict = {}
    #Movie names in movies_list
    movies_list = [mov1, mov2, mov3]

    #Appends all attributes of recommended movies into rec_movies and returns it
    for i in movies_list:
        result_dict = {
            'title' : i,
            'year' : title_merged.loc[title_merged['title'] == i, 'startYear'].iloc[0],
            'runtime' : title_merged.loc[title_merged['title'] == i, 'runtimeMinutes'].iloc[0],
            'genres' : title_merged.loc[title_merged['title'] == i, 'genres'].iloc[0],
            'rating' : title_merged.loc[title_merged['title'] == i, 'averageRating'].iloc[0]

        }
        rec_movies.append(result_dict)
        
    return rec_movies


app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():
    userMovie = request.args.get('query')
    movies = []

    if userMovie: 
        movies =  predict(userMovie, title_dict)
    else:
       movies 
    
    return render_template('index.html', movies=movies)


