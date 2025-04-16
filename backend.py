from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import subprocess
import os

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/rag-pipeline")
async def rag_pipeline(request: QueryRequest):
    query = request.query

    # Run your pipeline steps
    subprocess.run(["python", "query_transcripts.py", query])
    subprocess.run(["python", "final_llm_ans.py", query])
    subprocess.run(["python", "textToSpeech.py"])

    # Read final answer
    with open("final_answer_output.txt", "r", encoding="utf-8") as f:
        final_text = f.read()

    return {
        "answer": final_text,
        "audio_file_url": "http://127.0.0.1:8000/audio"
    }

# Endpoint to serve the audio file
@app.get("/audio")
async def get_audio():
    audio_path = "final_answer_audio.mp3"
    if os.path.exists(audio_path):
        return FileResponse(audio_path, media_type="audio/mpeg", filename="final_answer_audio.mp3")
    return {"error": "Audio file not found."}
