# Web Page Q&A Assistant using RAG

## Overview

This project demonstrates how to implement Retrieval-Augmented Generation (RAG) using a large language model like GPT and information from a web page. Users can ask questions, and the system will retrieve relevant information from the specified web page to generate accurate responses.

## Features

- Scrape and clean web page content
- Store embeddings locally with `pickle`
- Retrieve top relevant chunks via cosine similarity
- Generate answers using OpenAI's GPT model
- Web interface using Gradio

## Project Structure

```
rag-mock/
├── app.py
├── scraper.py
├── chunker.py
├── embedder.py
├── retriever.py
├── llm.py
├── utils.py
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Process a Web Page via the Interface

You can now enter a web page URL directly into the Gradio interface. The system will automatically scrape, chunk, embed, and index the content for you.

Steps handled internally:
- `scrape_web_page()` retrieves the page content.
- `chunk_text()` breaks it into segments.
- `generate_embeddings()` embeds the chunks.
- `save_embeddings()` stores them for querying.

No manual scripting needed!

### 4. Run the App

```bash
export OPENAI_API_KEY="your-key-here"
export OPENAI_BASE_URL="https://your-base-url/v1" # not required if you are using OpenAI Platform
export OPENAI_MODEL_NAME="gpt-4o-mini"

python app.py
```

Once launched, follow these steps in your browser:
1. Enter the URL of a web page you want to query.
2. Click 'Process URL' to index the page.
3. Ask any question based on that content.

## Testing Example

URL to index: https://en.wikipedia.org/wiki/Natural_language_processing

Try questions like:

- "What is natural language processing?"
- "Which techniques are used in NLP?"
- "What are common applications of NLP?"

## Notes

- You must provide your own OpenAI API key, OpenAI model name and the based url (optional) if you are using other llm provider.
- This project is educational and should not be used in production without additional safeguards.
