import moviepy.editor as mp
import speech_recognition as sr
from gtts import gTTS
from moviepy.editor import AudioFileClip, VideoFileClip
import os
from googletrans import Translator

# Path to your video file
video_file = "putin4.mp4"
# The source language of the audio track
source_language = "ru"
# The target language for the translation
target_language = "en"
# Load the video
video = mp.VideoFileClip("putin4.mp4")

# Extract the audio from the video
audio_file = video.audio
audio_file.write_audiofile("putin4.wav")


video_ = VideoFileClip("putin4.mp4")
audio_ = video_.audio
# Save audio as mp3
audio_.write_audiofile("temp.wav", codec='pcm_s16le')
# Initialize recognizer
r = sr.Recognizer()

# Load the audio file
with sr.AudioFile("putin4.wav") as source:
    data = r.record(source)

# Convert speech to text
text = r.recognize_google(data, language = source_language)

# init the Google API translator
translator = Translator()
# detect a language
detection = translator.detect(text)
translation = translator.translate(text, dest=target_language)
trans_text = translation.text
print('TRANS_TEXT ---', trans_text)
print('TRANSLATION ----', translation)
tts = gTTS(text = trans_text, lang=target_language, slow=False)
tts.save("output.wav")

# Split the original video into smaller parts
original_video = VideoFileClip(video_file)
original_audio = AudioFileClip("output.wav")
final_video = original_video.set_audio(original_audio)
final_video.write_videofile("final.mp4")


# Remove temporary files
os.remove("temp.wav")