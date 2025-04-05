import requests
import json
from dotenv import load_dotenv
import os
import argparse

load_dotenv()
api_key = "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"

parser = argparse.ArgumentParser(description="Ask a legal question to the Audio-RAG system.")
parser.add_argument("query", type=str, help="The question you want to ask")
args = parser.parse_args()
query = args.query

with open("retrieved_chunks.txt", "r", encoding="utf-8") as f:
    context = f.read()

model = "openrouter/quasar-alpha"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "Court-Transcript-RAG",
}

payload = {
    "model": model,
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"Context:\n{context}\n\nQuestion: {query}"
                }
            ]
        }
    ]
}

response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=json.dumps(payload))

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
