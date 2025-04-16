import requests
import json
import os
import argparse
from dotenv import load_dotenv

# Load environment variables (optional, fallback to hardcoded key)
load_dotenv()
api_key = os.getenv("GROQ_API_KEY", "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")

# CLI argument to pass query
parser = argparse.ArgumentParser(description="Ask a legal question to the Audio-RAG system.")
parser.add_argument("query", type=str, help="The question you want to ask")
args = parser.parse_args()
query = args.query

# Read the retrieved context
with open("retrieved_chunks.txt", "r", encoding="utf-8") as f:
    context = f.read()

# Set a valid Groq-supported model
model = "llama3-8b-8192"  # or "llama3-70b-8192" for more powerful response

# Prepare headers and payload
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

payload = {
    "model": model,
    "messages": [
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {query}"
        }
    ]
}

# Make the POST request to Groq's OpenAI-compatible endpoint
response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, data=json.dumps(payload))

# Handle the response
if response.status_code == 200:
    try:
        answer = response.json()["choices"][0]["message"]["content"]
        print("🧠 Final Answer:\n")
        print(answer)
        output_filename = "final_answer_output.txt"
        with open(output_filename, "w", encoding="utf-8") as out_file:
            out_file.write(answer)
        print(f"\n💾 Answer saved to: {output_filename}")
    except Exception as e:
        print("⚠️ Could not parse the response properly.")
        print("Raw response:\n", response.text)
else:
    print(f"❌ Error {response.status_code}: {response.text}")
