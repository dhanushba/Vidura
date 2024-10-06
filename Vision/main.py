from assistant import VoiceAssistant
from api import GeminiAPI

if __name__ == '__main__':
    gemini_api_key = "AIzaSyB3L8HBbbiuc8cNhgO4VB4ewSxcmnxQkz4"  # Replace with your actual API key
    assistant = VoiceAssistant(gemini_api_key)
    assistant.run()
