import openai
import speech_recognition as sr
from gtts import gTTS
import os

# Use the OpenAI Secret Manager to get your API key
openai.api_key = "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"

# Initialize the recognizer
r = sr.Recognizer()

def listen():
    # Listen to the user's voice
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # Try to recognize the voice
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return None
    except sr.RequestError as e:
        print("Error: " + e)
        return None

def speak(text):
    # Use the gTTS library to convert the text to speech
    tts = gTTS(text, lang='en', tld='ie')
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")

def chatbot_response(text):
    # Use the OpenAI API to get a response from the chatbot
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"{text}"),
        max_tokens=1024,
        n = 1,
        stop=None,
        temperature=0.5,
    )

    # Get the response from the chatbot
    return response.choices[0].text

while True:
    text = listen()
    if text:
        response = chatbot_response(text)
        speak(response)
