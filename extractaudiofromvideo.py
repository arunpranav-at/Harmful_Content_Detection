import audiototext
from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_file_path, lang):
    try:
        # Load the video clip
        print(video_file_path)
        video_clip = VideoFileClip(video_file_path)
        
        # Extract audio
        audio_clip = video_clip.audio
        
        
        # Write the audio to a file
        # audio_clip.write_audiofile("output_audio_file_path.mp3")
        # print("Audio extracted successfully.")
        
        text = audiototext.audiototext(audio_clip, lang)
        
        
        # Close the video clip
        video_clip.close()
        
        print( True, "Audio extracted successfully.")
        return text
    except Exception as e:
        print( False, f"Error occurred: {str(e)}")
        return "Error occurred: " + str(e)
# Example usage:
# video_file_path = "tamil.mp4"
# output_audio_file_path = "output_audio.mp3"
# success, message = extract_audio_from_video(video_file_path, output_audio_file_path)
# if success:
#     print(message)
# else:
#     print("Failed to extract audio:", message)
