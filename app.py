import gradio as gr
from scraper import scrape_web_page
from chunker import chunk_text
from embedder import generate_embeddings, save_embeddings, load_embeddings
from retriever import retrieve_relevant_chunks
from llm import generate_answer

embedding_data = None

def load_and_process_url(url):
    global embedding_data
    text = scrape_web_page(url)
    chunks = chunk_text(text)
    embedding_data = generate_embeddings(chunks)
    save_embeddings(embedding_data)
    return "Web page processed and indexed successfully!"

def answer_question(question):
    if embedding_data is None:
        return "Please process a web page first by entering its URL."
    chunks = retrieve_relevant_chunks(question, embedding_data)
    return generate_answer(question, chunks)

# Gradio UI with two inputs: one for URL, one for questions
with gr.Blocks() as demo:
    gr.Markdown("# Web Page Q&A Assistant using RAG")
    
    with gr.Row():
        url_input = gr.Textbox(label="Web Page URL")
        process_btn = gr.Button("Process URL")
    
    process_output = gr.Textbox(label="Status")
    
    process_btn.click(fn=load_and_process_url, inputs=url_input, outputs=process_output)

    question_input = gr.Textbox(label="Ask a Question")
    answer_output = gr.Textbox(label="Answer")

    question_input.change(fn=answer_question, inputs=question_input, outputs=answer_output)

demo.launch()
