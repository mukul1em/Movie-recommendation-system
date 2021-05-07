import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')
column_names = ['user_id','item_id', 'rating','timestamp']
df = pd.read_csv('ml-100k/u.data', sep='\t', names=column_names)
movie_titles=pd.read_csv('ml-100k/u.item', sep='\|', header=None)
movie_titles = movie_titles[[0,1]]
movie_titles.columns=['item_id','title']
df = pd.merge(df, movie_titles, on='item_id')

ratings = pd.DataFrame(df.groupby('title').mean()['rating'])
ratings['num of ratings'] = pd.DataFrame(df.groupby('title').count()['rating'])
moviemat = df.pivot_table(index='user_id', columns='title', values='rating')

df = pd.merge(df, movie_titles, on='item_id')
def predict_movies(movie_name):
    movie_user_ratings = moviemat[movie_name]
    similar_to_movie = moviemat.corrwith(movie_user_ratings)
    
    corr_movie= pd.DataFrame(similar_to_movie, columns = ['correlation'])
    corr_movie.dropna(inplace=True)
    
    corr_movie = corr_movie.join(ratings['num of ratings'])
    predictions = corr_movie[corr_movie['num of ratings']>100].sort_values('correlation', ascending=False)
    return predictions


