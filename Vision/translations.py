from googletrans import Translator

def translate(text, target_lang):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except Exception as e:
        print(f"Translation error: {e}")
        return text
