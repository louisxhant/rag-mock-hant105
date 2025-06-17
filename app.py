# app.py - OpenAI version
import gradio as gr
import os
from dotenv import load_dotenv
from scraper import scrape_web_page
from chunker import chunk_text
from embedder import generate_embeddings, save_embeddings, load_embeddings
from retriever import retrieve_relevant_chunks
from llm import generate_answer

# Load environment variables
load_dotenv()

# Global variable to store embeddings
embedding_data = None

def load_and_process_url(url):
    global embedding_data
    
    if not url or not url.strip():
        return "❌ Please enter a valid URL"
    
    try:
        # Step 1: Scrape the webpage
        print(f"🌐 Scraping: {url}")
        text = scrape_web_page(url)
        
        if text.startswith("Error"):
            return text
        
        if len(text) < 100:
            return "❌ Not enough content found on this webpage"
        
        # Step 2: Chunk the text
        print("📝 Chunking text...")
        chunks = chunk_text(text)
        
        if not chunks:
            return "❌ No valid chunks created from the webpage"
        
        # Step 3: Generate embeddings
        print("🔢 Generating embeddings...")
        embedding_data = generate_embeddings(chunks)
        
        # Step 4: Save embeddings
        print("💾 Saving embeddings...")
        save_embeddings(embedding_data)
        
        return f"✅ Success! Processed {len(chunks)} chunks from {url}\n📊 Ready to answer questions!"
        
    except Exception as e:
        return f"❌ Error processing URL: {str(e)}"

def answer_question(question):
    global embedding_data
    
    if not question or not question.strip():
        return "❓ Please enter a question"
    
    if embedding_data is None:
        # Try to load from file
        embedding_data = load_embeddings()
        if embedding_data is None:
            return "⚠️ Please process a web page first by entering its URL and clicking 'Process URL'"
    
    try:
        # Step 1: Retrieve relevant chunks
        print(f"🔍 Searching for: {question}")
        relevant_chunks = retrieve_relevant_chunks(question, embedding_data)
        
        if not relevant_chunks:
            return "❌ No relevant information found. Try rephrasing your question."
        
        # Step 2: Generate answer using OpenAI
        print("🤖 Generating answer with OpenAI...")
        answer = generate_answer(question, relevant_chunks)
        
        return answer
        
    except Exception as e:
        return f"❌ Error generating answer: {str(e)}"

def clear_data():
    global embedding_data
    embedding_data = None
    try:
        os.remove("embeddings.pkl")
    except:
        pass
    return "🧹 Data cleared! You can now process a new webpage."

# Create Gradio interface
with gr.Blocks(
    title="RAG Q&A with OpenAI",
    theme=gr.themes.Soft(),
    css="footer {visibility: hidden}"
) as demo:
    
    gr.Markdown("""
    # 🤖 RAG Q&A Assistant with OpenAI GPT
    
    **Hướng dẫn sử dụng:**
    1. 📝 Nhập URL của trang web bạn muốn phân tích
    2. 🔄 Click "Process URL" để xử lý trang web
    3. ❓ Đặt câu hỏi về nội dung trang web
    4. 🎯 Nhận câu trả lời từ OpenAI GPT
    
    **Powered by:** OpenAI GPT-3.5-turbo + RAG (Retrieval-Augmented Generation)
    """)
    
    with gr.Row():
        with gr.Column(scale=4):
            url_input = gr.Textbox(
                label="🌐 URL của trang web",
                placeholder="https://en.wikipedia.org/wiki/Artificial_intelligence",
                info="Nhập URL của trang web bạn muốn phân tích"
            )
        with gr.Column(scale=1):
            process_btn = gr.Button(
                "🔄 Process URL", 
                variant="primary",
                size="lg"
            )
    
    process_output = gr.Textbox(
        label="📊 Trạng thái xử lý",
        lines=3,
        interactive=False,
        info="Thông tin về quá trình xử lý trang web"
    )
    
    gr.Markdown("---")
    
    with gr.Row():
        with gr.Column(scale=4):
            question_input = gr.Textbox(
                label="❓ Câu hỏi của bạn",
                placeholder="What is artificial intelligence?",
                info="Đặt câu hỏi về nội dung trang web đã xử lý"
            )
        with gr.Column(scale=1):
            ask_btn = gr.Button(
                "🔍 Hỏi", 
                variant="secondary",
                size="lg"
            )
    
    answer_output = gr.Textbox(
        label="🎯 Câu trả lời từ OpenAI GPT",
        lines=8,
        interactive=False,
        info="OpenAI GPT sẽ trả lời dựa trên nội dung trang web"
    )
    
    with gr.Row():
        clear_btn = gr.Button("🧹 Clear Data", variant="stop")
        
    clear_output = gr.Textbox(visible=False)
    
    # Event handlers
    process_btn.click(
        fn=load_and_process_url,
        inputs=[url_input],
        outputs=[process_output]
    )
    
    ask_btn.click(
        fn=answer_question,
        inputs=[question_input],
        outputs=[answer_output]
    )
    
    question_input.submit(
        fn=answer_question,
        inputs=[question_input],
        outputs=[answer_output]
    )
    
    clear_btn.click(
        fn=clear_data,
        outputs=[clear_output]
    )
    
    # Example section
    gr.Markdown("""
    ## 💡 Ví dụ URLs để test:
    - **Wikipedia**: https://en.wikipedia.org/wiki/Machine_learning
    - **Python Docs**: https://docs.python.org/3/tutorial/introduction.html
    - **News**: Bất kỳ bài báo online nào
    
    ## 💡 Ví dụ câu hỏi:
    - "What is the main topic of this article?"
    - "What are the key concepts mentioned?"
    - "Can you summarize the main points?"
    
    ## 🔧 Technical Details:
    - **Embedding**: TF-IDF Vectorization
    - **Retrieval**: Cosine Similarity
    - **LLM**: OpenAI GPT-3.5-turbo
    - **Framework**: Gradio + Python
    """)

if __name__ == "__main__":
    print("🚀 Starting RAG Q&A Assistant with OpenAI...")
    print("📋 Make sure you have set OPENAI_API_KEY in .env file")
    print("💰 Using OpenAI GPT-3.5-turbo")
    demo.launch(
        share=False,
        server_name="127.0.0.1", 
        server_port=7860,
        show_error=True
    )