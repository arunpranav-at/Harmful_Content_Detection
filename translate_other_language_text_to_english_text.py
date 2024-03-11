from googletrans import Translator

def translate_to_english(text, source_language='auto'):
    
    try:
        translator = Translator()        
        translated_text = translator.translate(text, src=source_language, dest='en').text
        
        return translated_text
    except Exception as e:
        
        return f"Translation error: {str(e)}"

# Example usage:
# text_to_translate = "пошел на хуй, сука?"  
# translated_text = translate_to_english(text_to_translate)
# print("Translated text:", translated_text)