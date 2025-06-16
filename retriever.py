from sklearn.metrics.pairwise import cosine_similarity
from embedder import vectorizer  # Use this instead of model

# Function to retrieve top-k relevant text chunks for a given query
def retrieve_relevant_chunks(query, embedded_chunks, top_k=3):
    query_vec = vectorizer.transform([query]).toarray()
    similarities = [(chunk, cosine_similarity([query_vec[0]], [vec])[0][0]) for chunk, vec in embedded_chunks]
    sorted_chunks = sorted(similarities, key=lambda x: x[1], reverse=True)
    return [chunk for chunk, _ in sorted_chunks[:top_k]]