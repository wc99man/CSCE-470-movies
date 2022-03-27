import pandas as pd 
pd.options.display.width = 0


name_basics_df = pd.read_csv('Data/name_basics/data.tsv', sep='\t', dtype=str, nrows=4000)
title_basics_df = pd.read_csv('Data/title_basics/data.tsv', sep='\t', dtype=str, nrows=4000)
title_basics_df = title_basics_df.rename(columns={'tconst':'titleId'})
title_akas_df = pd.read_csv('Data/title_akas/data.tsv', sep='\t', dtype=str, nrows=4000)
title_rating_df = pd.read_csv('Data/title_ratings/data.tsv', sep='\t', dtype=str, nrows=4000)
title_crew_df = pd.read_csv('Data/title_crew/data.tsv', sep='\t', dtype=str, nrows=4000)
title_crew_df = title_crew_df.rename(columns={'tconst':'tconst1'})


title = title_akas_df[title_akas_df["region"]=="US"]




title_merged = pd.merge(left=title, right=title_basics_df, left_on='titleId',right_on='titleId')
title_merged = title_merged[title_merged['titleType']=="movie"]
title_merged = pd.merge(left=title_merged, right = title_rating_df, left_on='titleId', right_on='tconst')
title_merged = pd.merge(left=title_merged, right = title_crew_df, left_on='titleId', right_on='tconst1')
title_merged=title_merged.drop(labels=['numVotes','tconst','tconst1','ordering','language','types','attributes','isOriginalTitle','titleType','primaryTitle','originalTitle','isAdult','endYear'],axis=1)
# print(title.head(1000))
# print(title_basics_df.head(20))
# print(title_rating_df.head(20))
print(title_merged.head(1000))