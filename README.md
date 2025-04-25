⚖️ JusticeWhisper: Audio-RAG for Legal Court Hearings JusticeWhisper is a domain-specific Audio-based Retrieval-Augmented Generation (RAG) system built to process, transcribe, analyze, and respond to legal court hearing audio files—delivering answers in both text and audio formats.

🚀 From court hearing audio → intelligent legal insight → audio/text response!

📌 Key Features 🎧 Audio Ingestion: Handles legal audio recordings from court hearings.

🗣️ Speech-to-Text: Converts spoken legal content into accurate transcripts.

📚 Transcript Embedding: Embeds transcripts into a vector store for semantic search.

🔍 Query System: Users ask questions and get answers from court hearing data.

🤖 LLM Integration: Contextual legal responses using Large Language Models.

🔁 Text-to-Speech: Converts LLM responses back into human-like audio.

🔄 End-to-End Pipeline: Scripted pipeline for automation and backend integration.

🧩 Architecture Overview Below is the system architecture based on your pipeline:

🔄 Pipeline Breakdown

Component Description audio_hearings.py Loads court hearing audio from the downloads folder speech_to_text.py Converts audio into transcript and stores in transcripts/ embed_transcripts.py Embeds the transcripts and stores them in VectorStore query_Transcripts.py Accepts queries from the client and retrieves relevant text chunks final_llm_ans.py Uses an LLM to generate final answers final_output.txt Stores the generated response in text text_to_speech.py Converts text answers into final_audio_answer.mp3 run_pipeline.py Automates the end-to-end process backend.py Ties all logic to the backend API client Frontend or API consumer for interactive querying

📁 Directory Structure

JusticeWhisper/ │ ├── downloads/ # Raw court hearing audio files ├── transcripts/ # Generated transcripts ├── VectorStore/ # FAISS or vector DB for retrieval ├── client/ # Frontend or test client ├── audio_hearings.py ├── speech_to_text.py ├── embed_transcripts.py ├── query_Transcripts.py ├── final_llm_ans.py ├── text_to_speech.py ├── run_pipeline.py ├── backend.py └── final_output.txt / .mp3 # Response results

⚙️ Getting Started

Clone the repo
git clone https://github.com/namnuts/JusticeWhisper.git cd JusticeWhisper

Install dependencies
pip install -r requirements.txt

Run the full pipeline and Backend
uvicorn backend:app -reload

to run in port
cd client -------------> npm run dev this is my READme and give the Headings "JusticeWhisper: Audio-RAG for Legal Court Hearings JusticeWhisper is a domain-specific Audio-based Retrieval-Augmented Generation (RAG) system built to process, transcribe, analyze, and respond to legal court hearing audio files—delivering answers in both text and audio formats." Part in Big and Bold text
