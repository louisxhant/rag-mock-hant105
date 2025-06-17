# llm.py - OpenAI version
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("OPENAI_MODEL_NAME", "gpt-3.5-turbo")

# Debug: Check if API key is loaded
print(f"🔑 OpenAI API Key loaded: {'Yes' if api_key else 'No'}")

if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found in environment variables")

client = openai.OpenAI(api_key=api_key)

def generate_answer(query, context_chunks):
    context = "\n".join(context_chunks)
    
    prompt = f"""Based on the following context, please answer the question accurately and concisely.

Context:
{context}

Question: {query}

Please provide a clear and informative answer based only on the information provided in the context. If the context doesn't contain enough information to answer the question, please say so."""

    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.3
        )
        
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        return f"Error generating answer: {str(e)}"