import requests

class GeminiAPI:
    def __init__(self, api_key):
        self.api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
        self.api_key = api_key

    def get_response(self, query):
        headers = {
            'Content-Type': 'application/json'
        }
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": query}
                    ]
                }
            ]
        }
        response = requests.post(f"{self.api_url}?key={self.api_key}", headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            if 'candidates' in data:
                return data['candidates'][0]['content']['parts'][0]['text']
            else:
                return "No content found in the response."
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return "Sorry, I couldn't process your request."
