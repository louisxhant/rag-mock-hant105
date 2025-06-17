# chunker.py
def chunk_text(text, chunk_size=500, overlap=50):
    """
    Chia text thành các chunks với overlap để tránh mất thông tin
    """
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        if chunk.strip():  # Chỉ thêm chunk không rỗng
            chunks.append(chunk)
        
        # Dừng nếu đã đến cuối
        if i + chunk_size >= len(words):
            break
    
    return chunks