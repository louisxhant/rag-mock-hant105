# Web Page Q&A Assistant using RAG with OpenAI

## Overview

This project demonstrates how to implement Retrieval-Augmented Generation (RAG) using OpenAI GPT and information from web pages. Users can ask questions, and the system will retrieve relevant information from the specified web page to generate accurate responses using OpenAI's language models.

## Features

- 🌐 **Web Scraping**: Extract and clean content from any public webpage
- 📝 **Smart Chunking**: Break down content into manageable, overlapping chunks
- 🔢 **TF-IDF Embeddings**: Generate embeddings using scikit-learn (lightweight and fast)
- 💾 **Local Storage**: Save embeddings locally using pickle for persistence
- 🔍 **Cosine Similarity Retrieval**: Find most relevant chunks for any query
- 🤖 **OpenAI Integration**: Generate answers using GPT-3.5-turbo or GPT-4
- 🎨 **Modern Web Interface**: Beautiful Gradio interface with Vietnamese support

## Project Structure

```
rag-openai-project/
├── app.py              # Main Gradio application
├── scraper.py          # Web scraping functionality
├── chunker.py          # Text chunking with overlap
├── embedder.py         # TF-IDF embedding generation
├── retriever.py        # Cosine similarity retrieval
├── llm.py              # OpenAI API integration
├── utils.py            # Utility functions
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
└── README.md          # This file
```

## Getting Started

### 1. Prerequisites

- Python 3.8+ installed on your system
- OpenAI account with API access
- Basic understanding of command line

### 2. Installation

Clone or download this repository:
```bash
# If using Git
git clone <repository-url>
cd <this folder>

# Or download and extract the files
```

Create and activate virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. OpenAI API Setup

#### Get API Key:
1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign up or log in to your account
3. Navigate to "API keys" section
4. Click "Create new secret key"
5. Copy the API key (starts with `sk-proj-...`)

#### Add Payment Method:
- OpenAI requires a payment method to use the API
- Minimum $5 credit recommended
- GPT-3.5-turbo is very affordable (~$0.002/1K tokens)

### 4. Environment Configuration

Create a `.env` file in the project root:
```env
OPENAI_API_KEY=sk-proj-your-api-key-here
OPENAI_MODEL_NAME=gpt-3.5-turbo
```

**Available Models:**
- `gpt-3.5-turbo` - Fast and cost-effective (recommended)
- `gpt-4o-mini` - Balanced performance and cost
- `gpt-4o` - Most capable, higher cost

### 5. Run the Application

```bash
python app.py
```

You should see:
```
🚀 Starting RAG Q&A Assistant with OpenAI...
📋 Make sure you have set OPENAI_API_KEY in .env file
💰 Using OpenAI GPT-3.5-turbo
* Running on local URL:  http://127.0.0.1:7860
```

Open your browser and navigate to: **http://127.0.0.1:7860**

## How to Use

### Step 1: Process a Web Page
1. Enter a URL in the "URL của trang web" field
2. Click "🔄 Process URL"
3. Wait for the success message: "✅ Success! Processed X chunks..."

### Step 2: Ask Questions
1. Type your question in the "Câu hỏi của bạn" field
2. Click "🔍 Hỏi" or press Enter
3. Get AI-powered answers based on the webpage content

### Step 3: Clear Data (Optional)
- Use "🧹 Clear Data" to reset and process a new webpage

## Example URLs for Testing

### Educational Content:
- **AI/ML**: https://en.wikipedia.org/wiki/Machine_learning
- **Programming**: https://docs.python.org/3/tutorial/introduction.html
- **Science**: https://en.wikipedia.org/wiki/Quantum_computing

### News Articles:
- Any recent news article from reputable sources
- Blog posts and documentation pages
- Wikipedia articles on any topic

## Example Questions

### General Understanding:
- "What is the main topic of this article?"
- "Can you summarize the key points?"
- "What are the most important concepts mentioned?"

### Specific Information:
- "Who are the notable people mentioned?"
- "What are the main applications discussed?"
- "What challenges or limitations are described?"

### Analytical Questions:
- "How does this relate to current technology trends?"
- "What are the pros and cons mentioned?"
- "What future developments are predicted?"

## Technical Architecture

### RAG Pipeline:
```
Web Page → Scraper → Chunker → TF-IDF Embedder → Vector Store → Retriever → OpenAI GPT → Answer
```

### Components:
1. **Web Scraping**: BeautifulSoup + requests for content extraction
2. **Text Chunking**: Overlap-based chunking (500 words, 50-word overlap)
3. **Embeddings**: TF-IDF vectorization (lightweight, fast)
4. **Storage**: Pickle-based local storage
5. **Retrieval**: Cosine similarity for finding relevant chunks
6. **Generation**: OpenAI GPT for natural language responses

## Configuration Options

### Environment Variables:

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENAI_API_KEY` | Yes | None | Your OpenAI API key |
| `OPENAI_MODEL_NAME` | No | `gpt-3.5-turbo` | OpenAI model to use |

### Chunking Parameters (in `chunker.py`):
- `chunk_size`: Default 500 words
- `overlap`: Default 50 words

### Retrieval Parameters (in `retriever.py`):
- `top_k`: Number of chunks to retrieve (default: 3)

## Cost Estimation

### OpenAI Pricing (as of 2025):
- **GPT-3.5-turbo**: ~$0.002/1K tokens
- **GPT-4o-mini**: ~$0.150/1K tokens  
- **GPT-4o**: ~$15.00/1K tokens

### Example Usage:
- Processing a typical webpage: ~$0.01-0.05
- Answering a question: ~$0.001-0.01
- $5 credit can handle hundreds of queries

## Troubleshooting

### Common Issues:

#### 1. API Key Errors
```
Error: Invalid API key provided
```
**Solution**: Check your `.env` file and ensure the API key is correct

#### 2. Quota Exceeded
```
You exceeded your current quota
```
**Solution**: Add credit to your OpenAI account or check billing settings

#### 3. Web Scraping Failures
```
Error scraping URL: timeout
```
**Solutions**: 
- Try a different URL
- Check your internet connection
- Some sites may block automated requests

#### 4. Module Not Found
```
ModuleNotFoundError: No module named 'openai'
```
**Solution**: Ensure virtual environment is activated and run `pip install -r requirements.txt`

#### 5. Empty or Poor Responses
**Solutions**:
- Try more specific questions
- Ensure the webpage has sufficient content
- Check if the content is in a supported language

## Limitations

- **Language**: Works best with English content
- **Content Types**: Optimized for text-heavy pages
- **Rate Limits**: Subject to OpenAI API rate limits
- **Cost**: Requires OpenAI credits for usage
- **Dynamic Content**: Cannot process JavaScript-rendered content

## Security Notes

- ⚠️ **Never commit API keys** to version control
- ⚠️ **Keep `.env` file private** and add it to `.gitignore`
- ⚠️ **Monitor API usage** to avoid unexpected charges
- ⚠️ **Validate URLs** before processing to avoid malicious sites

## Extending the Project

### Possible Enhancements:
1. **Multiple URLs**: Process multiple webpages simultaneously
2. **Better Embeddings**: Switch to sentence-transformers for semantic search
3. **Vector Database**: Use FAISS, Chroma, or Pinecone for scalability
4. **Authentication**: Add user management and session handling
5. **Export Features**: Save Q&A sessions or generate reports
6. **Advanced UI**: Add file upload, URL validation, progress bars

### Enhancement Example - Multiple URLs:
```python
def process_multiple_urls(urls):
    all_chunks = []
    for url in urls:
        text = scrape_web_page(url)
        chunks = chunk_text(text)
        all_chunks.extend([(chunk, url) for chunk in chunks])
    return generate_embeddings(all_chunks)
```

## Contributing

This project is designed for educational purposes. Feel free to:
- Fork and modify for your needs
- Add new features or improvements
- Share your enhancements with the community

## License

This project is for educational use. Please respect the terms of service of:
- OpenAI API
- Websites you scrape
- Third-party libraries used

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify your API key and billing status
3. Test with simple examples first
4. Check OpenAI status page for service issues

---

**Built with ❤️ using Python, OpenAI, Gradio, and RAG principles**

*Last updated: June 2025*