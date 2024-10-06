from assistant import VoiceAssistant
from api import GeminiAPI

if __name__ == "__main__":
    assistant = VoiceAssistant(gemini_api_key="AIzaSyB3L8HBbbiuc8cNhgO4VB4ewSxcmnxQkz4")
    try:
        assistant.run()
    except KeyboardInterrupt:
        assistant.running = False
        print("Assistant shutting down...")
