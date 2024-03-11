import streamlit as st
import textclassifier
import audiototext
import image_text_detection
import text_from_video
import os
import glob
import cv2
import instagram_scrapper
from speedometer import indicator_gauge
import extractaudiofromvideo


def select_language():
    
    st.write(""" #### Select Language:""")
    language_options = [
    "English", "German", "Hindi", "French", "Italian", "Spanish", "Russian", "Japanese", "Chinese", 
    "Korean", "Arabic", "Turkish", "Dutch", "Portuguese", "Greek", "Swedish", "Danish", "Norwegian", 
    "Finnish", "Czech", "Polish", "Hungarian", "Romanian", "Slovak", "Serbian", "Bulgarian", "Ukrainian", 
    "Croatian", "Serbian", "Bosnian", "Slovenian", "Macedonian", "Albanian", "Montenegrin", "Belarusian", 
    "Estonian", "Latvian", "Tamil", "Telugu", "Malayalam", "Kannada", "Marathi", "Bengali", "Gujarati", 
    "Urdu", "Punjabi", "Nepali", "Sinhala"]

    selected_language = st.selectbox("Choose Language", language_options)
    
    # Map selected language to language code
    language_codes = {
    "English": "en-US",
    "German": "de-DE",
    "Hindi": "hi-IN",
    "French": "fr-FR",
    "Italian": "it-IT",
    "Spanish": "es-ES",
    "Russian": "ru-RU",
    "Japanese": "ja-JP",
    "Chinese": "zh-CN",
    "Korean": "ko-KR",
    "Arabic": "ar-AR",
    "Turkish": "tr-TR",
    "Dutch": "nl-NL",
    "Portuguese": "pt-PT",
    "Greek": "el-GR",
    "Swedish": "sv-SE",
    "Danish": "da-DK",
    "Norwegian": "no-NO",
    "Finnish": "fi-FI",
    "Czech": "cs-CZ",
    "Polish": "pl-PL",
    "Hungarian": "hu-HU",
    "Romanian": "ro-RO",
    "Slovak": "sk-SK",
    "Serbian": "sr-RS",
    "Bulgarian": "bg-BG",
    "Ukrainian": "uk-UA",
    "Croatian": "hr-HR",
    "Bosnian": "bs-BA",
    "Slovenian": "sl-SI",
    "Macedonian": "mk-MK",
    "Albanian": "sq-AL",
    "Montenegrin": "me-ME",
    "Belarusian": "be-BY",
    "Estonian": "et-EE",
    "Latvian": "lv-LV",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Malayalam": "ml-IN",
    "Kannada": "kn-IN",
    "Marathi": "mr-IN",
    "Bengali": "bn-IN",
    "Gujarati": "gu-IN",
    "Urdu": "ur-PK",
    "Punjabi": "pa-IN",
    "Nepali": "ne-NP",
    "Sinhala": "si-LK"}
        
    return selected_language, language_codes[selected_language]

def main():
    
    if 'curr_page' not in st.session_state:
        st.session_state.curr_page = "Description"        
            
    st.markdown(
        """        
        <style>
        .stButton > button {
            border-radius: 0;
            border: none;
            width: 100%;
            justify-content: left;
            margin-top: 10px;
        }
        .sidebar-content .block-container > div:first-child {
            display: flex;
            justify-content: center;
        }
        button[kind="primary"] {
            display: flex;
            justify-content: center;
            width: auto;
            flex: unset;
            padding: 4px 14px 4px 14px;
        }
        button[kind="primary"]:hover {
            background-color: dark-gray;
            color: yellow;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.markdown("""<div style="text-align: left; font-size: 30px;">Em<span style="color: #FF0C93;">po</span>(<span style="color: #FF0C93;">W</span>)H<span style="color: #FF0C93;">ER</span></div><br>""", unsafe_allow_html=True)
    #st.sidebar.title(" Empo(W)HER")
    st.sidebar.write(""" ### DashBoard """)
    
    def change_state_to_audio():
        st.session_state.curr_page = "Audio"
        
    def change_state_to_video():
        st.session_state.curr_page = "Video"
                
    def change_state_to_image():
        st.session_state.curr_page = "Image"
        
    def change_state_to_url():
        st.session_state.curr_page = "URL"
        
    def change_state_to_text():
        st.session_state.curr_page = "Text"
    
    def change_curr_state_to(currState):
        st.session_state.curr_page = currState
        
    st.sidebar.button("Text", on_click=(change_state_to_text))
    st.sidebar.button("Audio", on_click=change_state_to_audio)
    st.sidebar.button("Video", on_click=change_state_to_video)
    st.sidebar.button("Image", on_click=change_state_to_image)
    st.sidebar.button("URL", on_click=change_state_to_url)
    
    if st.session_state.curr_page == "Audio":        
        st.session_state.audio_input = None        
        st.header("Audio Input")
        st.session_state.audio_input = st.file_uploader(label="Upload Audio File", type=["mp3", "wav"])
        if st.session_state.audio_input is not None:
            st.write("## Preview")
            st.audio(st.session_state.audio_input)
            selected_language, lang_code = select_language()
            if selected_language:                
                st.write("Selected Language:", selected_language)
                clicked = st.button("Process", type="primary")
                if clicked:
                    is_vulgar_word_detected = False                    
                    html_result_status = ""
                                       
                    extractedtext = audiototext.audiototext(st.session_state.audio_input, lang_code)
                    label, score = textclassifier.textclassifier(extractedtext)
                    print(select_language, lang_code, st.session_state.audio_input, extractedtext, label, score)
                    
                    if label=='Profanity' or label=='toxic':
                        is_vulgar_word_detected = True                    
                    outputtext = "The input audio is: "+label+" with a score of "+str(score) + ". The extracted text is: " + extractedtext
                    if is_vulgar_word_detected:
                        html_result_status = """<span style="color:#E30B0B;"> Offensive content detected </span>"""
                    else:
                        html_result_status = """<span style="color:#58E31A;"> Normal Content </span>"""
                    st.markdown("""<div style="text-align: left; font-size: 30px; margin-top: 15px; margin-bottom: 15px;">Output: """ + html_result_status + """</div>""",  unsafe_allow_html=True)
                    st.text_area(label="Given Text Input:", value = outputtext, key = "text_output_area", disabled=True)
                    indicator_gauge(score, is_vulgar_word_detected)
                                
    elif st.session_state.curr_page == "Video":
        st.session_state.video_input = None        
        st.header("Video Input")
        st.session_state.video_input = st.file_uploader("Upload Video File", type=["mp4","MPEG4"])
        if st.session_state.video_input is not None:
            st.write(" ## Preview")
            st.video(st.session_state.video_input)
            selected_language, lang_code = select_language()
            clicked = st.button("Process", type="primary")
            if selected_language and clicked:
                #st.write("Selected Language:", selected_language)
                if clicked:
                                       
                    is_vulgar_word_detected = False
                    html_result_status = ""
                    
                    videoinput = st.session_state.video_input
                    video_folder = "D:\\gdg_wtm_hackathon\\github\\gdg-hackathon\\MAINFOLDER\\video"
                    save_path = os.path.join(video_folder, videoinput.name)
                    with open(save_path, "wb") as f:
                        f.write(videoinput.getbuffer())

                    st.success(f"Video uploaded successfully! Filename: {videoinput.name}")
                    extractedtext = text_from_video.main()
                    label, score = textclassifier.textclassifier(extractedtext)
                    if label=='Profanity' or label=='toxic':
                        is_vulgar_word_detected = True
                    outputtext = "The input text is: "+label+" with a score of "+str(score)
                    
                    
                    audioofvideo = extractaudiofromvideo.extract_audio_from_video(videoinput, lang_code)
                    labela, scorea = textclassifier.textclassifier(audioofvideo)
                    if labela=='Profanity' or labela=='toxic':
                        is_vulgar_word_detected = True
                    outputaudiotext = "The input text is: "+labela+" with a score of "+str(scorea)
                    
                    if is_vulgar_word_detected:
                        html_result_status = """<span style="color:#E30B0B;"> Offensive content detected </span>"""
                    else:
                        html_result_status = """<span style="color:#58E31A;"> Normal Content </span>"""
                    st.markdown("""<div style="text-align: left; font-size: 30px; margin-top: 15px; margin-bottom: 15px;">Output: """ + html_result_status + """</div>""",  unsafe_allow_html=True)
                    indicator_gauge(scorea, is_vulgar_word_detected)
                    st.text_area(label="Text extracted from input:", value = outputtext, key = "text_outputtxt_area", disabled=True)
                    st.text_area(label="Text extracted from video image:", value = extractedtext, key = "text_extracted_area", disabled=True)
                    st.text_area(label="Text extracted from input:", value = outputaudiotext, key = "audio1_outputtxt_area", disabled=True)
                    # st.text_area(label="Text extracted from video's audio:", value = audioofvideo, key = "audio_extracted_area", disabled=True)
                    
                        
    elif st.session_state.curr_page == "Image":
        st.session_state.image_input = None
        st.header("Image Input")
        st.session_state.image_input = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
        if st.session_state.image_input is not None:
            st.write(" ## Preview")
            st.image(st.session_state.image_input)
            clicked = st.button("Proceed", type="primary")
            
                      
            if clicked:
                is_vulgar_word_detected = False
                html_result_status = ""
                
                imagetext = image_text_detection.image_text_detection(st.session_state.image_input)
                label, score = textclassifier.textclassifier(imagetext)
                if label=='Profanity' or label=='toxic':    
                    is_vulgar_word_detected = True
                outputtext = "The input text is: "+label+" with a score of "+str(score)
                
                if is_vulgar_word_detected:
                    html_result_status = """<span style="color:#E30B0B;"> Offensive content detected </span>"""
                else:
                    html_result_status = """<span style="color:#58E31A;"> Normal Content </span>"""
                st.markdown("""<div style="text-align: left; font-size: 30px; margin-top: 15px; margin-bottom: 15px;">Output: """ + html_result_status + """</div>""",  unsafe_allow_html=True)
                indicator_gauge(score, is_vulgar_word_detected)
                st.text_area(label="Given Text Input:", value = outputtext, key = "text_output_area", disabled=True)
                st.text_area(label="Text extracted from input:", value = imagetext, key = "text_imagetxt_area", disabled=True)
                
                        
    elif st.session_state.curr_page == "URL":
        st.session_state.url_input = None
        st.header("URL Input")
        st.session_state.url_input = st.text_input("Enter URL")
        clicked = st.button("Proceed", type="primary")
        if st.session_state.url_input is not None and st.session_state.url_input != "":
            if clicked:
                # download video and audio / pics and discription from the instagram
                image_files,text_files,video_files,shortcode = instagram_scrapper.instagram_scrapper(st.session_state.url_input)
                text_from_image = text_from_video.extract_text_from_images("D:\\gdg_wtm_hackathon\\github\\gdg-hackathon\\CxiHGwOpnpb")
                
    
                with open (text_files[0], "r") as myfile:
                    text_from_description = myfile.read()
                # for video in video_files:
                #     text_from_reel = text_from_video.(video)
                # text_from_video = text_from_video.extract_text_from_video(shortcode)
                is_vulgar_word_detected = False
                html_result_status = ""
                
                label, score = textclassifier.textclassifier(text_from_image)
                if label=='Profanity' or label=='toxic':
                    is_vulgar_word_detected = True
                outputtext = "The input text is: "+label+" with a score of "+str(score)
                
                if is_vulgar_word_detected:
                    html_result_status = """<span style="color:#E30B0B;"> Offensive content detected </span>"""
                else:
                    html_result_status = """<span style="color:#58E31A;"> Normal Content </span>"""
                st.markdown("""<div style="text-align: left; font-size: 30px; margin-top: 15px; margin-bottom: 15px;">Output: """ + html_result_status + """</div>""",  unsafe_allow_html=True)
                st.write("Given URL:", st.session_state.url_input)
                indicator_gauge(score, is_vulgar_word_detected)
                    
    elif st.session_state.curr_page == "Text":
        st.session_state.text_input = None
        st.header("Text Input")
        st.session_state.text_input = st.text_area("Enter Text", key="my_input_text_area")
        def clear_data():
            st.session_state.my_input_text_area = None
        
        col1, col2, = st.columns([1,5])

        with col1:
            clicked = st.button("Process",type="primary")
        with col2:
            st.button("Clear", on_click=clear_data, type="primary")
            
        if clicked or st.session_state.text_input is not None:
            if st.session_state.text_input is not None and st.session_state.text_input != "" :
                inputtext = st.session_state.text_input
                is_vulgar_word_detected = False
                label, score = textclassifier.textclassifier(inputtext)
                if label=='Profanity' or label=='toxic':
                    is_vulgar_word_detected = True
                outputtext = "The input text is: "+label+" with a score of "+str(score)
                #st.header("Output")                
                html_result_status = ""
                if is_vulgar_word_detected:
                    html_result_status = """<span style="color:#E30B0B;"> Offensive content detected </span>"""
                else:
                    html_result_status = """<span style="color:#58E31A;"> Normal word </span>"""
                st.markdown("""<div style="text-align: left; font-size: 30px; margin-top: 15px; margin-bottom: 15px;">Output: """ + html_result_status + """</div>""",  unsafe_allow_html=True)
                indicator_gauge(score, is_vulgar_word_detected)
                st.text_area(label="Given Text Input:", value = outputtext, key = "text_output_area", disabled=True)
                
                
    elif st.session_state.curr_page == "Description":#CE19FF
        st.markdown("""
            <div style="align-items:center; align-self:center; justify-content: center; min-height: 100vh;">
                <div style="text-align: center; font-size: 50px;">Em<span style="color: #FF0C93;">po</span>(<span style="color: #FF0C93;">W</span>)H<span style="color: #FF0C93;">ER</span></div><br>
                <div style="text-align: center; font-size: 32px;">Made with ❤️ by Enigmatic Technoverse</div><br><br>
                <div style="text-align: center; font-size: 16px;">A comprehensive tool to check whether the content of various formats are harmful towards women</div>
            </div>
            """, unsafe_allow_html=True)
            
if __name__ == "__main__":
    main()
