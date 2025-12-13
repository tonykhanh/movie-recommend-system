import pickle
import pandas as pd
import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Fix pandas compatibility
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

# Load the movie list
with open('./model/movie_list.pkl', 'rb') as m:
    movies = pickle.load(m)

print("Movies loaded successfully!")
print(f"Number of movies: {len(movies)}")
print(f"Columns: {movies.columns.tolist()}")

# Create similarity matrix based on genres
# Check if 'genres' column exists
if 'genres' in movies.columns:
    # Convert genres to string if it's a list
    movies['genres_str'] = movies['genres'].apply(lambda x: ' '.join(x) if isinstance(x, list) else str(x))
    
    # Create count vectorizer
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies['genres_str']).toarray()
    
    # Calculate cosine similarity
    similarity = cosine_similarity(vectors)
    
    print(f"Similarity matrix shape: {similarity.shape}")
    
    # Save similarity matrix
    with open('./model/similarity.pkl', 'wb') as s:
        pickle.dump(similarity, s)
    
    print("Similarity matrix created and saved successfully!")
else:
    print("Warning: 'genres' column not found. Available columns:", movies.columns.tolist())
    # Create a simple identity matrix as fallback
    import numpy as np
    similarity = np.eye(len(movies))
    with open('./model/similarity.pkl', 'wb') as s:
        pickle.dump(similarity, s)
    print("Created identity similarity matrix as fallback")
