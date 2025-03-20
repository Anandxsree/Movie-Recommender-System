import streamlit as st
import pandas as pd
import pickle
import requests

# Function to fetch movie poster from TMDB API
def fetch_poster(movie_id):
    try:
        api_key = "60e5c8632b4d69eba8a0b66028644869"
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster+Available"
    except Exception as e:
        print(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/500x750?text=Error"


# Function to recommend movies
def recommend(movie):
    try:
        # Find the index of the selected movie
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_posters = []

        for i in movie_list:
            movie_data = movies.iloc[i[0]]
            recommended_movies.append(movie_data['title'])

            # Fetch poster using movie_id
            movie_id = movie_data.get('movie_id', None)
            if movie_id:
                recommended_posters.append(fetch_poster(movie_id))
            else:
                recommended_posters.append("https://via.placeholder.com/500x750?text=No+Poster+Available")

        return recommended_movies, recommended_posters
    except Exception as e:
        print(f"Error in recommend(): {e}")
        return [], []

# Load movie data and similarity matrix
try:
    # Replace these with the correct paths to your pickle files
    movie_dict = pickle.load(open('movie_dict.pk1', 'rb'))
    movies = pd.DataFrame(movie_dict)

    similarity = pickle.load(open('simi.pk1', 'rb'))
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Streamlit app UI
st.title("🎥 Movie Recommender System")

# Dropdown for selecting a movie
selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

# Button to generate recommendations
if st.button('Show Recommendation'):
    try:
        # Get recommendations
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)

        if recommended_movie_names:
            # Display recommendations
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                st.text(recommended_movie_names[0])
                st.image(recommended_movie_posters[0])
            with col2:
                st.text(recommended_movie_names[1])
                st.image(recommended_movie_posters[1])
            with col3:
                st.text(recommended_movie_names[2])
                st.image(recommended_movie_posters[2])
            with col4:
                st.text(recommended_movie_names[3])
                st.image(recommended_movie_posters[3])
            with col5:
                st.text(recommended_movie_names[4])
                st.image(recommended_movie_posters[4])
        else:
            st.error("No recommendations found. Please try again.")

    except Exception as e:
        st.error(f"An error occurred while generating recommendations: {e}")