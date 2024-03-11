import englishtextclassifier, tanglishtextclassifier, translate_other_language_text_to_english_text
from langdetect import detect

def textclassifier(text):
    output_from_tanglishmodel = tanglishtextclassifier.tanglishtextclassifier(text)     
    
    if output_from_tanglishmodel[0]['label']=='Profanity':
        return 'Profanity', output_from_tanglishmodel[0]['score']
    
    # output_from_englishmodel = englishtextclassifier.englishtextclassifier(text)
    # if output_from_englishmodel[0]['label']=='toxic':
    #     return 'toxic', output_from_englishmodel[0]['score']
    print("pls work",text)
    
    translated_to_english = translate_other_language_text_to_english_text.translate_to_english(text)
    print("translated_to_english",translated_to_english)
    output_from_englishmodel = englishtextclassifier.englishtextclassifier(translated_to_english)
    
    if output_from_englishmodel[0]['label']=='toxic':
        return 'toxic', output_from_englishmodel[0]['score']
    else:
        return output_from_englishmodel[0]['label'], output_from_englishmodel[0]['score']
        
