
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies.csv")
# movies.csv lo 'genres' column lekapothe, 'title' ne vadutham
if 'genres' in movies.columns:
    movies['features'] = movies['genres'].fillna('')
else:
    movies['features'] = movies['title'].fillna('')

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# title -> index map
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

def recommend(title, num=5):
    if title not in indices:
        return ["Movie not found"]
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num+1]
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()