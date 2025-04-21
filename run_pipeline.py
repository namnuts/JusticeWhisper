import sys
import subprocess

def run_pipeline(query: str):
    if not query.strip():
        print("❌ Please provide a query string.")
        print("Usage: python run_pipeline.py \"Your question here\"")
        sys.exit(1)

    print("🟡 Running Query Retrieval...")
    subprocess.run(f'"{sys.executable}" query_transcripts.py "{query}"', shell=True, check=True)

    print("🟢 Sending to OpenRouter for response...")
    subprocess.run(f'"{sys.executable}" final_llm_ans.py "{query}"', shell=True, check=True)

    print("🔊 Converting response to speech...")
    subprocess.run(f'"{sys.executable}" textToSpeech.py', shell=True, check=True)

    print("✅ Pipeline completed. Audio file generated.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ No query provided.")
        print("Usage: python run_pipeline.py \"Your question here\"")
        sys.exit(1)

    query_input = sys.argv[1]
    run_pipeline(query_input)
