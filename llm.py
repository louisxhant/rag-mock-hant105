# llm.py — compatible with openai>=1.0.0, with custom base_url and model support

import openai
import os

# Load configuration from environment variables
api_key = os.getenv("OPENAI_API_KEY")  # Required
base_url = os.getenv("OPENAI_BASE_URL")  # Optional
model_name = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")  # Default model if not provided

# Initialize the OpenAI client
client = openai.OpenAI(api_key=api_key, base_url=base_url) if base_url else openai.OpenAI(api_key=api_key)

def generate_answer(query, context_chunks):
    context = "\n".join(context_chunks)
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
