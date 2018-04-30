import pandas as pd
import os

df_ratings = pd.read_csv("ml-latest-small/ratings.csv")
df_movies = pd.read_csv("ml-latest-small/movies.csv")

user_id = 1
movie_id = 0

#creating directory
if not os.path.exists('./hw4.movies/'):
            os.makedirs('./hw4.movies/')


f = open('hw4.movies/user1.txt','w')
for row in df_ratings.itertuples():
    if row[1] == user_id:
        movie_id = row[2]
        r = df_movies.loc[df_movies['movieId'] == movie_id]
        idx = r.index.values[0]
        movie = df_movies["title"][idx]
        f.write("%r\n"% movie)
    else:
        user_id += 1
        file_name = 'hw4.movies/user'+str(user_id)+'.txt'
        f = open(file_name,'w')
        movie_id = row[2]
        r = df_movies.loc[df_movies['movieId'] == movie_id]
        idx = r.index.values[0]
        movie = df_movies["title"][idx]
        f.write("%r\n"% movie)
f.close()