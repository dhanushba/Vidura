import pyttsx3
import speech_recognition as sr

def speak(text, lang='en'):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if lang in voice.languages:
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()

def take_command():
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
