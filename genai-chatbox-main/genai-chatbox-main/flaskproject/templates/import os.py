import os
from translate import Translator
import speech_recognition as sr

# Set the PYTHONIOENCODING environment variable to UTF-8
os.environ["PYTHONIOENCODING"] = "UTF-8"

def translate_text(text, target_language='en'):
    translator = Translator(to_lang=target_language)
    translated_text = translator.translate(text)
    return translated_text

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak here MR.vishnupargavan..")
    recognizer.adjust_for_ambient_noise(source) 
    audio = recognizer.listen(source)

try:
    user_speech = recognizer.recognize_google(audio)
    print("Recognized Speech:")
    print(user_speech)
    target_language = 'ta'
    translated_text = translate_text(user_speech, target_language)
    # Explicitly specify encoding when printing
    print("Translated text ({}): {}".format(target_language, translated_text.encode('utf-8').decode('utf-8')))

except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError as e:
    print("Could not request results from Speech Recognition service; {}".format(e))
