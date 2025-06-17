# embedder.py
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Global variables
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
tfidf_matrix = None
chunk_texts = None

def generate_embeddings(chunks):
    global tfidf_matrix, chunk_texts
    
    if not chunks:
        return []
    
    chunk_texts = chunks
    tfidf_matrix = vectorizer.fit_transform(chunks)
    
    # Return list of tuples (chunk_text, embedding_vector)
    return list(zip(chunks, tfidf_matrix.toarray()))

def save_embeddings(data, filename="embeddings.pkl"):
    try:
        with open(filename, "wb") as f:
            pickle.dump({
                'data': data,
                'vectorizer': vectorizer
            }, f)
        return True
    except Exception as e:
        print(f"Error saving embeddings: {e}")
        return False

def load_embeddings(filename="embeddings.pkl"):
    global vectorizer
    try:
        with open(filename, "rb") as f:
            saved_data = pickle.load(f)
            vectorizer = saved_data['vectorizer']
            return saved_data['data']
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error loading embeddings: {e}")
        return None