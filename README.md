⚖️ JusticeWhisper: Audio-RAG for Legal Court Hearings
JusticeWhisper is a domain-specific Audio-based Retrieval-Augmented Generation (RAG) system built to process, transcribe, analyze, and respond to legal court hearing audio files—delivering answers in both text and audio formats.

🚀 From court hearing audio → intelligent legal insight → audio/text response!

📌 Key Features
🎧 Audio Ingestion: Handles legal audio recordings from court hearings.

🗣️ Speech-to-Text: Converts spoken legal content into accurate transcripts.

📚 Transcript Embedding: Embeds transcripts into a vector store for semantic search.

🔍 Query System: Users ask questions and get answers from court hearing data.

🤖 LLM Integration: Contextual legal responses using Large Language Models.

🔁 Text-to-Speech: Converts LLM responses back into human-like audio.

🔄 End-to-End Pipeline: Scripted pipeline for automation and backend integration.

🧩 Architecture Overview
A breakdown of the system pipeline:


Component	Description
audio_hearings.py	Loads court hearing audio from the downloads/ folder
speech_to_text.py	Converts audio into transcripts and stores in transcripts/
embed_transcripts.py	Embeds the transcripts and stores them in the VectorStore/
query_Transcripts.py	Accepts user queries and retrieves relevant transcript chunks
final_llm_ans.py	Uses an LLM (like GPT) to generate final answers
final_output.txt	Stores the generated text response
text_to_speech.py	Converts the response text into audio final_audio_answer.mp3
run_pipeline.py	Runs the entire pipeline from audio to audio/text output
backend.py	Exposes API endpoints for interaction
client/	Frontend or API consumer for querying
📁 Directory Structure
bash
Copy
Edit
JusticeWhisper/
│
├── downloads/                  # Raw court hearing audio files
├── transcripts/                # Generated transcripts
├── VectorStore/                # Vector database for retrieval
├── client/                     # Frontend or API consumer
├── audio_hearings.py
├── speech_to_text.py
├── embed_transcripts.py
├── query_Transcripts.py
├── final_llm_ans.py
├── text_to_speech.py
├── run_pipeline.py
├── backend.py
└── final_output.txt / .mp3    # Response results
⚙️ Getting Started
🔧 Clone the repo
bash
Copy
Edit
git clone https://github.com/namnuts/JusticeWhisper.git
cd JusticeWhisper
📦 Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
🚀 Run the Backend
bash
Copy
Edit
uvicorn backend:app --reload
🖥️ Run the Frontend

cd client --->
npm run dev
