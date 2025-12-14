import pandas as pd
import pickle
import requests
import sys
import streamlit as st
 
# Fix for pandas compatibility with older pickle files
pd.Int64Index = pd.Index
pd.Float64Index = pd.Index
pd.UInt64Index = pd.Index
try:
    import pandas.core.indexes.numeric as numeric_index
except ModuleNotFoundError:
    import pandas as numeric_index
    sys.modules['pandas.core.indexes.numeric'] = numeric_index

if hasattr(pd, '_libs'):
    pd._libs.Int64Index = pd.Index
    pd._libs.Float64Index = pd.Index
    pd._libs.UInt64Index = pd.Index

@st.cache_data
def load_data():
    """Load movie list and similarity matrix from pickle files."""
    try:
        with open('model/movie_list.pkl', 'rb') as f:
            movies_df = pickle.load(f)
            
        with open('model/similarity.pkl', 'rb') as f:
            similarity = pickle.load(f)
            
        return movies_df, similarity
    except FileNotFoundError:
        st.error("Model files not found. Please ensure 'model/movie_list.pkl' and 'model/similarity.pkl' exist.")
        return None, None
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None, None

def fetch_poster(movie_id):
    """Fetch movie poster from TMDB API."""
    try:
        # Using the API key found in the original source code
        url = "https://api.themoviedb.org/3/movie/{}?api_key=41d86c2adc37a6151dc71b5ec3c75d39&language=en-US".format(movie_id)
        response = requests.get(url, timeout=5)
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
    except Exception as e:
        print(f"Error fetching poster: {e}")
    
    # Return a placeholder or None if fetch fails
    return "https://via.placeholder.com/500x750?text=No+Available+Poster"

def recommend(movie, movies_df, similarity):
    """
    Recommend similar movies based on the selected movie.
    Returns lists of recommended movie names and posters.
    """
    try:
        # Find the index of the movie in the dataframe
        movie_index = movies_df[movies_df['title'] == movie].index[0]
        
        # Get similarity scores for this movie
        distances = similarity[movie_index]
        
        # Sort by similarity score (descending) and get top 5 (excluding the movie itself)
        # enumerate gives (index, score) pairs
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        
        recommended_movies = []
        recommended_movies_posters = []
        
        for i in movies_list:
            movie_id = movies_df.iloc[i[0]].movie_id
            
            recommended_movies.append(movies_df.iloc[i[0]].title)
            recommended_movies_posters.append(fetch_poster(movie_id))
            
        return recommended_movies, recommended_movies_posters
        
    except IndexError:
        st.error("Movie not found in database.")
        return [], []
    except Exception as e:
        st.error(f"Error in recommendation: {e}")
        return [], []
