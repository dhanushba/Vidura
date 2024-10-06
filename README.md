# Vidura

# 🎤 Vidura: Your Voice Assistant

Welcome to **Vidura**, your interactive voice assistant that helps you with various tasks, provides information, and learns from your preferences! This project is built using Python, leveraging speech recognition, text-to-speech conversion, and the Gemini API for intelligent responses.

## 📦 Features

- **Voice Recognition**: Understands your voice commands and queries.
- **Text-to-Speech**: Responds back with clear audio.
- **Current Time & Date**: Easily ask for the current time and date.
- **Web Actions**: Open websites in various modes (e.g., incognito).
- **AI-Powered Responses**: Fetches intelligent responses using the Gemini API.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Install necessary libraries:

```bash
pip install pyttsx3 speechrecognition
Clone the Repository
bash
Copy code
git clone https://github.com/dhanushba/Vidura.git
cd Vidura
Set Up Your API Key
Sign up for the Gemini API and get your API key.
Create a file named api.py and add your API key.
python
Copy code
class GeminiAPI:
    def __init__(self, api_key):
        self.api_key = api_key
Run the Assistant
bash
Copy code
python main.py
🎤 Usage
Once the assistant is running, simply say your command:

"What is the time?"
"What is the date?"
"Open Google in incognito."
"Ask [your question]."
Example Interactions
User: "What is the time?"

Assistant: "The current time is 12:20."

User: "Open YouTube."

Assistant: Opens YouTube in the default browser.

💻 Contributing
We welcome contributions! Please follow these steps:

Fork the repository.
Create a new branch: git checkout -b feature/YourFeature.
Make your changes and commit: git commit -m 'Add your feature'.
Push to the branch: git push origin feature/YourFeature.
Open a pull request.
📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙏 Acknowledgments
SpeechRecognition
pyttsx3
Gemini API
🤖 Demo

📫 Contact
For inquiries or feedback, please reach out to:

Your Name: your.email@example.com
GitHub Profile: yourusername
vbnet
Copy code

### Notes for Customization:
- **Title and Description**: Adjust the title and description to reflect your project accurately.
- **API Key Setup**: Make sure to explain how to set up the API key, and adjust the instructions according to your implementation.
- **Demo Section**: Consider adding a demo GIF or image that showcases the assistant in action to attract users.
- **License**: Choose a license that suits your project and link to it.

Feel free to modify this template as per your project's requirements! An engaging README will significantly help others understand, use, and contribute to your project.


markdown
Copy code
# Voice Assistant

A voice-activated assistant that leverages the Gemini API for real-time responses and predictions. The assistant can perform various tasks such as telling the current time and date, answering questions, and opening websites.

## Features

- **Voice Recognition**: Utilizes SpeechRecognition to understand user commands.
- **Text-to-Speech**: Implements `pyttsx3` for interactive responses.
- **Real-time Information**: Fetches current time and date dynamically.
- **Web Interaction**: Opens specified websites based on user commands.
- **Question Answering**: Uses Gemini API to answer user queries.

## Technologies Used

- Python
- `pyttsx3` for text-to-speech functionality
- `SpeechRecognition` for voice command capture
- `datetime` for real-time date and time retrieval
- Gemini API for intelligent responses and predictions

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/dhanushba/Vidura.git
Navigate to the project directory:

bash
Copy code
cd voice-assistant
Set up a virtual environment:

bash
Copy code
python -m venv .venv
Activate the virtual environment:

On Windows:
bash
Copy code
.venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source .venv/bin/activate
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Set up your API keys and configurations in a separate config file or environment variables.

Usage
Run the assistant:

bash
Copy code
python main.py
Interact with the voice assistant by speaking commands like:

"What is the time?"
"What is the date?"
"Open Google in incognito mode."
"Ask what is the capital of France."
Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or enhancements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Special thanks to the developers of the libraries and APIs used in this project.
Inspired by various voice assistant implementations.
