from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import subprocess
import os

app = FastAPI()

# CORS middleware configuration
origins = [
    "http://localhost",  # Allow localhost for local development
    "http://localhost:5173",  # If your frontend runs on a different port
    "http://127.0.0.1",  # Allow localhost with IP
    # Add other origins as needed, for example, your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Define the request model
class QueryRequest(BaseModel):
    query: str

# Define the POST endpoint that will run the pipeline
@app.post("/rag-pipeline")
async def rag_pipeline(request: QueryRequest):
    query = request.query

    # Check if the query is empty or only contains spaces
    if not query.strip():
        return {"error": "❌ Please provide a valid query string."}

    # Run your pipeline steps
    try:
        print("🟡 Running Query Retrieval...")
        subprocess.run(f'python query_transcripts.py "{query}"', shell=True, check=True)

        print("🟢 Sending to OpenRouter for response...")
        subprocess.run(f'python final_llm_ans.py "{query}"', shell=True, check=True)

        print("🔊 Converting response to speech...")
        subprocess.run(f'python textToSpeech.py', shell=True, check=True)

        print("✅ Pipeline completed successfully.")

        # Read the final answer (text output)
        with open("final_answer_output.txt", "r", encoding="utf-8") as f:
            final_text = f.read()

        return {
            "answer": final_text.strip(),
            "audio_file_url": "http://127.0.0.1:8000/audio"  # Audio file URL
        }

    except subprocess.CalledProcessError as e:
        return {"error": f"❌ Error during pipeline execution: {e.stderr}"}

# Endpoint to serve the audio file
@app.get("/audio")
async def get_audio():
    audio_path = "final_answer_audio.mp3"
    if os.path.exists(audio_path):
        return FileResponse(audio_path, media_type="audio/mpeg", filename="final_answer_audio.mp3")
    return {"error": "Audio file not found."}
