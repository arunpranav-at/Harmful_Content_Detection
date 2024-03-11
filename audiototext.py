#import library
import speech_recognition as sr
import translate_other_language_text_to_english_text as tt

def audiototext(audiofile, lang):
    r = sr.Recognizer()
    with sr.AudioFile(audiofile) as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio_text = r.record(source)
        try:
            if lang=="en-US":
                text = r.recognize_google(audio_text, language=lang)
                return text
            else:
                text = r.recognize_google(audio_text, language=lang)
                texteng = tt.translate_to_english(text)
                return texteng          
        
        except:
            # print('Sorry.. run again...')
            return "Error Occured"

# audio_file="audio and video/obama-fake-0.wav"
# lang="en-US"
# audiototext(audio_file,lang)

# Germany-"de-DE"
# English-"en-US"
# Hindi-"hi-IN"
# French-"fr-FR"
# Italian-"it-IT"
# Spanish-"es-ES"
# Russian-"ru-RU"
# Japanese-"ja-JP"
# Chinese-"zh-CN"
# Korean-"ko-KR"
# Arabic-"ar-AR"
# Turkish-"tr-TR"
# Dutch-"nl-NL"
# Portuguese-"pt-PT"
# Greek-"el-GR"
# Swedish-"sv-SE"
# Danish-"da-DK"
# Norwegian-"no-NO"
# Finnish-"fi-FI"
# Czech-"cs-CZ"
# Polish-"pl-PL"
# Hungarian-"hu-HU"
# Romanian-"ro-RO"
# Slovak-"sk-SK"
# Serbian-"sr-RS"
# Bulgarian-"bg-BG"
# Ukrainian-"uk-UA"
# Croatian-"hr-HR"
# Serbian-"sr-RS"
# Bosnian-"bs-BA"
# Slovenian-"sl-SI"
# Macedonian-"mk-MK"
# Albanian-"sq-AL"
# Montenegrin-"me-ME"
# Belarusian-"be-BY"
# Estonian-"et-EE"
# Latvian-"lv-LV"
#tamal-"ta-IN"
#telugu-"te-IN"
#malayalam-"ml-IN"
#kannada-"kn-IN"
#marathi-"mr-IN"
#bengali-"bn-IN"
#gujarati-"gu-IN"
#urdu-"ur-PK"
#punjabi-"pa-IN"
#nepali-"ne-NP"
#sinhala-"si-LK"



           
            
    


