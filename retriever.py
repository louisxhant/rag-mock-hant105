# retriever.py
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from embedder import vectorizer

def retrieve_relevant_chunks(query, embedded_chunks, top_k=3):
    """
    Tìm các chunks liên quan nhất đến query
    """
    if not embedded_chunks or not query.strip():
        return []
    
    try:
        # Transform query using the same vectorizer
        query_vec = vectorizer.transform([query]).toarray()[0]
        
        # Calculate similarities
        similarities = []
        for chunk_text, chunk_vec in embedded_chunks:
            similarity = cosine_similarity([query_vec], [chunk_vec])[0][0]
            similarities.append((chunk_text, similarity))
        
        # Sort by similarity (highest first)
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        # Return top-k chunks
        return [chunk for chunk, _ in similarities[:top_k]]
        
    except Exception as e:
        print(f"Error in retrieval: {e}")
        return []