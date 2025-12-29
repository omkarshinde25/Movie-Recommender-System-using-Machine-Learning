import pickle
import streamlit as st
import requests

API_KEY = "6e5244768e5b2853655d6139bfe22e67"

def fetch_poster(movie_id):
    try:
        url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id, API_KEY)
        response = requests.get(url, timeout=10)
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return None
    except:
        return None


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        key=lambda x: x[1],
        reverse=True
    )

    names = []
    posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))

    return names, posters


st.header("Movie Recommender System")

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movie_list = movies["title"].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button("Show Recommendation"):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)   # 5 posters in ONE LINE

    for i in range(5):
        with cols[i]:
            if posters[i]:
                st.image(posters[i], caption=names[i])
            else:
                st.write(names[i])
                st.write("Poster not available")
