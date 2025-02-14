import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=7a09f4013fcced22ccb8a32d6f4a6eda&language=en-US'.format(movie_id))
    # https://image.tmdb.org/t/p/w780/bvYjhsbxOBwpm8xLE5BhdA3a8CZ.jpg
    data = response.json()
    #st.text(data)
    #st.text('https://api.themoviedb.org/3/movie/{}?api_key=7e63afdb9f70b156c707e9294dd82983&language=en-US'.format(movie_id))
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie,num_recommendations):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x:x[1])[1:num_recommendations+1]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

# gdown.download('https://drive.google.com/uc?id=1-chIIipJl-4kBukpf7jKrhLj8bF2Im1k', 'simi.pkl', quiet=False)

# with open('simi.pkl', 'rb') as f:
#     similar = pickle.load(open('simi.pkl','rb'))


similarity = pickle.load(open('simi.pkl', 'rb'))
st.title("Movie Recommender System")

selected_movie = st.selectbox('What movie are you watching?',movies['title'].values)

num_recommendations = st.selectbox('How many movies would you like me to recommend for you today? ',[1,2,3,4,5,6,7,8,9,10])

if st.button('Recommend'):
    names,posters= recommend(selected_movie,num_recommendations)
    for i in range(num_recommendations):
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image(posters[i], width=200)  # Adjust the width as needed
        with col2:
            st.write(
                f"<div style='display: flex; align-items: center; justify-content: center; height: 200px;'>{names[i]}</div>",
                unsafe_allow_html=True,
            )

