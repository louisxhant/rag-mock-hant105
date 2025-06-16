# Mock Project Requirement for RAG Course

## Course
For Beginners: Learn to Implement RAG with LLMs! Build an AI that Answers Questions Using Web Page Info

## Project
Build an AI Q&A Assistant Using RAG and Web Page Information

## Objective
Create a Q&A AI assistant that can answer user queries based on the content of a specific web page using the Retrieval-Augmented Generation (RAG) approach and a Large Language Model (LLM).

## Overview
Students will apply the concepts learned throughout the course to develop a Python application that integrates RAG to extract and process information from a designated web page. The final product will be a simple web-based chatbot that can answer questions using this retrieved data, combined with the reasoning capabilities of an LLM like GPT.

## Project Requirements

### 1. Web Scraping
- Select a publicly available, information-rich web page (e.g., Wikipedia article or documentation page).
- Use libraries such as `BeautifulSoup`, `requests`, or `Selenium` to scrape and preprocess the text content.

### 2. Chunking and Indexing
- Divide the web page content into manageable text chunks.
- Index these chunks using a simple vector store that can be embedded directly in the project, such as one based on `pickle`.

### 3. Retrieval Mechanism
- Implement a retrieval step to find the most relevant chunks based on a user query.
- Use cosine similarity or another similarity metric for ranking.

### 4. Integration with LLM
- Combine retrieved chunks with the query and send them to a large language model (e.g., GPT via OpenAI API).
- Generate responses based on the retrieved context.

### 5. User Interface
- Build a web interface using **Gradio**.
- Allow users to ask questions and view AI-generated answers in real-time.

### 6. Bonus (Optional)
- Let users input different web page URLs.
- Highlight which source content was used in the answer.

## Deliverables
- Python source code with comments and documentation.
- A short report (markdown or PDF) detailing the approach and implementation.
- Optional: Demo video.

## Evaluation Criteria
- Completeness and correctness of RAG implementation.
- Code clarity and maintainability.
- Quality and usability of the interface.
- Implementation of any optional enhancements.

## Learning Goals
- Master the RAG framework.
- Learn LLMs enhanced with retrieval.
- Develop Python skills in NLP, web scraping, and vector search.
- Gain practical experience in building an AI assistant.

## Reference Code Access

Students can refer to a pre-built implementation of a RAG-based Q&A assistant available at the following link:

**🔗 [Reference Source Code](https://github.com/vietanh85/rag-mock)**

> ⚠️ **Important Note:**  
If students choose to use the reference source code as a starting point, they **must modify or enhance** it meaningfully. One such required enhancement is to **allow users to input a list of URLs** instead of just one, enabling the assistant to process and retrieve information from multiple web pages.
