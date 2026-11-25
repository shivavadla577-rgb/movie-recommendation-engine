
import streamlit as st
from recommender import recommend

st.set_page_config(page_title="Movie Recommendation Engine", layout="wide")

st.title("🎬 AI Movie Recommendation Engine")
st.write("Discover movies based on your interests using Machine Learning")

# Load movies
try:
    import pandas as pd
    movies = pd.read_csv("movies.csv")
    movie_list = movies['title'].tolist()
except:
    movie_list = ["Avatar", "Jurassic Park", "Titanic"]

# Sidebar
st.sidebar.title("🎬 Movie Preferences")
selected_movie = st.sidebar.selectbox("Select a Movie", movie_list)
number = st.sidebar.slider("How many recommendations?", 1, 10, 5)

st.write(f"**Selected Movie:** {selected_movie}")
st.write("Select a movie from the sidebar and click the button below.")

if st.button("🔍 Get Recommendations"):
    try:
        recs = recommend(selected_movie, number)
        st.subheader(f"Movies similar to {selected_movie}:")
        for movie in recs:
            st.success(f"🎬 {movie}")
    except Exception as e:
        st.error(f"Error: {e}")