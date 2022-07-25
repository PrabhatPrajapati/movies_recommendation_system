import streamlit as st
import pandas as pd
import joblib
similarity=joblib.load("similarity.pkl")
st.title("Movie Recommender System")
movie=pd.read_csv("tmdb_5000_movies.csv")
name=movie["title"].values
option = st.selectbox(
     'How would you like to be contacted?',
     name)

def recommendaction(name):
    movie_index=movie[movie["title"]==name].index[0]
    distance=similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda X:X[1])[1:6]
    recommanded_movie=[]
    for i in movie_list:
        recommanded_movie.append(movie.iloc[i[0]].title)
    return recommanded_movie

if st.button("Recommend"):
    recommand=recommendaction(option)
    for i in recommand:
        st.write(i)
