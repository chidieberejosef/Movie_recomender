import pickle
import streamlit as st
import requests
import os

API_KEY = '6eabf5975bdf921d2aca78d1d9c00d5f'

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            full_path = "http://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
    return None

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        poster = fetch_poster(movie_id)
        if poster:
            recommended_movies_poster.append(poster)
            recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name, recommended_movies_poster

st.header("Movies Recommendation System Using Machine Learning")

movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select movie name to get recommendations',
    movie_list
)

if st.button('Show recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    if recommended_movies_name:
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            col.text(recommended_movies_name[idx])
            col.image(recommended_movies_poster[idx])
    else:
        st.error("Could not fetch recommendations. Please try again.")


