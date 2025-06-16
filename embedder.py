import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Vectorizer is CPU-only and very fast for small to medium scale
vectorizer = TfidfVectorizer()

# Global storage for vectorized data
tfidf_matrix = None
chunk_texts = None

def generate_embeddings(chunks):
    global tfidf_matrix, chunk_texts
    chunk_texts = chunks
    tfidf_matrix = vectorizer.fit_transform(chunks)
    return list(zip(chunks, tfidf_matrix.toarray()))

def save_embeddings(data, filename="embeddings.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(data, f)

def load_embeddings(filename="embeddings.pkl"):
    with open(filename, "rb") as f:
        return pickle.load(f)
