import pandas as pd
import math

def predict(moviename, moviedict):  ##### we need the name of the movie so we can make a new vector for it

    givenvector = {}

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
        quit()
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

    #####print the winning movies
    print(mov1,win1)
    print(mov2,win2)
    print(mov3,win3)

pd.options.display.width = 0

name_basics_df = pd.read_csv('Data/name_basics/data.tsv', sep='\t', dtype=str, nrows=5000)
title_basics_df = pd.read_csv('Data/title_basics/data.tsv', sep='\t', dtype={'startYear': 'int32'}, nrows=5000)
title_basics_df = title_basics_df.rename(columns={'tconst':'titleId'})
title_basics_df = title_basics_df.replace(to_replace = "\\N", value = "0")
title_basics_df = title_basics_df.astype({'runtimeMinutes' : 'int32' })
title_akas_df = pd.read_csv('Data/title_akas/data.tsv', sep='\t', dtype=str, nrows=5000)
title_rating_df = pd.read_csv('Data/title_ratings/data.tsv', sep='\t', dtype=str, nrows=5000)
title_crew_df = pd.read_csv('Data/title_crew/data.tsv', sep='\t', dtype=str, nrows=5000)
title_crew_df = title_crew_df.rename(columns={'tconst':'tconst1'})

title = title_akas_df[title_akas_df["region"]=="US"]
# title_basics_df = title_basics_df[title_basics_df["startYear"] > 2000]




title_merged = pd.merge(left=title, right=title_basics_df, left_on='titleId',right_on='titleId')
title_merged = title_merged[title_merged['titleType']=="movie"]
title_merged = pd.merge(left=title_merged, right = title_rating_df, left_on='titleId', right_on='tconst')
title_merged = pd.merge(left=title_merged, right = title_crew_df, left_on='titleId', right_on='tconst1')
title_merged=title_merged.drop(labels=['numVotes','tconst','tconst1','ordering','language','types','attributes','isOriginalTitle','titleType','primaryTitle','originalTitle','isAdult','endYear'],axis=1)

#Converts title_merged df into dictionary (Format --> {movieName : {'titleId' : ..., 'Year': ..., etc.)
title_dict = {title_merged['title'][index]:{} for index in title_merged.index}

for index in title_merged.index:
    movieName = title_merged['title'][index]
    title_dict[movieName] = {title_merged['titleId'][index] : 0, title_merged['startYear'][index] : 0, title_merged['runtimeMinutes'][index] : 0, title_merged['genres'][index] : 0, title_merged['averageRating'][index] : 0}

print(title_dict)

##### Need to call the predict function and give it a user entered value and the dictionary we made

userMovie = input("Enter the exact name of your movie: ")




predict(userMovie, title_dict)


# print(title_merged)


