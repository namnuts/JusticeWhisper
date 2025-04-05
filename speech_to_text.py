import os
import assemblyai as aai

aai.settings.api_key = "4e57a4c5d93845f292ca0820a41f326f"

audio_folder = "downloads"
transcript_folder = "transcripts"

os.makedirs(transcript_folder, exist_ok=True)

mp3_files = [f for f in os.listdir(audio_folder) if f.endswith(".mp3")]

transcriber = aai.Transcriber()

for file in mp3_files:
    audio_path = os.path.join(audio_folder, file)
    print(f"🔊 Transcribing: {audio_path}")

    try:
        transcript = transcriber.transcribe(audio_path)

        if transcript and transcript.text:
            print(f"\n📝 Transcript for {file}:\n{transcript.text}\n")
            output_file = os.path.join(transcript_folder, f"{os.path.splitext(file)[0]}.txt")
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(transcript.text)
            print(f"✅ Saved to: {output_file}")
        else:
            print(f"⚠ No transcript returned for {file}")
    except Exception as e:
        print(f"❌ Error transcribing {file}: {e}")

    print("-" * 60)
