# import pyttsx3

# with open("final_answer_output.txt", "r", encoding="utf-8") as f:
#     text = f.read()

# engine = pyttsx3.init()
# engine.setProperty('rate', 150)
# engine.setProperty('volume', 1.0)

# # engine.say(text)
# engine.runAndWait()

# engine.save_to_file(text, 'final_answer_audio.mp3')
# engine.runAndWait()


from gtts import gTTS

# Read the text from the file
with open("final_answer_output.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Convert the text to speech using Google TTS
speech = gTTS(text=text, lang='en')

# Save the speech to an MP3 file
speech.save("final_answer_audio.mp3")

print("✅ Audio saved as 'final_answer_audio.mp3'.")

