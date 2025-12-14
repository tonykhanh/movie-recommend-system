import streamlit as st
import utils

# Set page configuration
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for UI enhancements
st.markdown("""
<style>
    .reportview-container {
        background: #0e1117;
    }
    .main-header {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #ffffff;
        text-align: center;
        padding-bottom: 20px;
    }
    .movie-title {
        color: #fff;
        font-weight: bold;
        text-align: center;
        font-size: 1.1em;
        margin-top: 10px;
        height: 60px;
        overflow: hidden;
    }
    /* Add nice hover effects to images if possible, although Streamlit is limited */
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-header">🎬 Movie Recommender System</h1>', unsafe_allow_html=True)
    st.markdown("### Find your next favorite movie!")
    st.write("---")

    # Load data
    with st.spinner("Loading movie database..."):
        movies_df, similarity = utils.load_data()

    if movies_df is None or similarity is None:
        st.error("Could not load data. Please check if model files are present.")
        return

    # Sidebar for controls
    st.sidebar.header("Search")
    
    # Dropdown for movie selection
    movie_list = movies_df['title'].values
    selected_movie = st.sidebar.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

    # Button to trigger recommendation
    if st.sidebar.button('Show Recommendation', type="primary"):
        with st.spinner(f"Finding movies similar to '{selected_movie}'..."):
            names, posters = utils.recommend(selected_movie, movies_df, similarity)
        
        if names:
            st.subheader(f"Because you watched: **{selected_movie}**")
            st.write("") # Spacer
            
            # Display recommendations in a grid
            cols = st.columns(5)
            
            for i, col in enumerate(cols):
                if i < len(names):
                    with col:
                        # Display Image
                        st.image(posters[i], use_container_width=True)
                        # Display Title with some custom styling
                        st.markdown(f"<div class='movie-title'>{names[i]}</div>", unsafe_allow_html=True)
        else:
            st.warning("No recommendations found.")
    
    # Default state or footer
    if 'selected_movie' not in st.session_state:
        st.write("")

if __name__ == '__main__':
    main()
