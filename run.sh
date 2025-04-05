#!/bin/bash

# Accept query string from command-line input
QUERY="$1"

# Check if query was provided
if [ -z "$QUERY" ]; then
  echo "❌ Please provide a query string."
  echo "Usage: ./run_pipeline.sh \"Your question here\""
  exit 1
fi

echo "🟡 Running Query Retrieval..."
python query_transcripts.py "$QUERY"

echo "🟢 Sending to OpenRouter for response..."
python final_llm_ans.py "$QUERY"

echo "🔊 Converting response to speech..."
python textToSpeech.py

echo "✅ Pipeline completed. Audio file generated."
