import pandas as pd 
pd.options.display.width = 0


name_basics_df = pd.read_csv('Data/name_basics/data.tsv', sep='\t', dtype=str)
title_basics_df = pd.read_csv('Data/title_basics/data.tsv', sep='\t', dtype=str)
title_basics_df = title_basics_df.rename(columns={'tconst':'titleId'})
title_akas_df = pd.read_csv('Data/title_akas/data.tsv', sep='\t', dtype=str)
title_rating_df = pd.read_csv('Data/title_ratings/data.tsv', sep='\t', dtype=str)
title_crew_df = pd.read_csv('Data/title_crew/data.tsv', sep='\t', dtype=str)
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
    title_dict[movieName] = {'titleId' : title_merged['titleId'][index],'Year' : title_merged['startYear'][index],'Runtime' : title_merged['runtimeMinutes'][index], 'Genres' : title_merged['genres'][index], 'Rating' : title_merged['averageRating'][index]}

# print(title_dict)
# print(title_merged)

tsvfile = title_merged.to_csv("output.csv")