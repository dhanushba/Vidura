import pyttsx3
import speech_recognition as sr
from api import GeminiAPI
from web_actions import open_website

class VoiceAssistant:
    def __init__(self, gemini_api_key):
        self.engine = pyttsx3.init()
        self.set_voice_properties()
        self.gemini_api = GeminiAPI(gemini_api_key)

    def set_voice_properties(self):
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)

    def speak(self, text, lang='en'):
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if lang in voice.languages:
                self.engine.setProperty('voice', voice.id)
                break
        self.engine.say(text)
        self.engine.runAndWait()

    def take_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            try:
                audio = r.listen(source, timeout=5)
                query = r.recognize_google(audio, language="en-IN")
                print(f"User said: {query}")
                return query
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return "None"
            except sr.UnknownValueError:
                print("Could not understand the audio")
                return "None"
            except Exception as e:
                print(f"Error occurred: {e}")
                return "None"

    def handle_conversation(self, text, lang='en'):
        if "open" in text:
            mode = None
            if "incognito" in text:
                mode = "incognito"
            elif "developer" in text or "dev mode" in text:
                mode = "developer"
            open_website(text, mode)
        elif "ask" in text:
            question = text.replace("ask", "").strip()
            response = self.gemini_api.get_response(question)
            print(response)
            self.speak(response, lang)
        else:
            response = self.gemini_api.get_response(text)
            print(response)
            self.speak(response, lang)

    def run(self):
        self.speak("Hello Dhanush, how can I assist you today?", 'en')
        while True:
            text = self.take_command().lower()
            if text != "none":
                lang = 'en'  # Change based on user input or detection
                self.handle_conversation(text, lang)
            if "stop" in text:
                self.speak("Goodbye!", lang)
                break
