from instaloader import *
import os

def instagram_scrapper(url):
    # Get instance
    L = instaloader.Instaloader()
    # getting shortcode from url
    shortcode = url.split("/")[-2]
    print("shortcode: ", shortcode)
    post = Post.from_shortcode(L.context, shortcode)
    print(post.shortcode)
    L.download_post(post, target=post.shortcode)
    print("post downloaded successfully")
    # returning the list of paths of image and description
    image_files = []
    video_files = []
    text_files = []
    # List all files in the folder
    files = os.listdir("D:\\gdg_wtm_hackathon\\github\\gdg-hackathon\\CxiHGwOpnpb")
    # Iterate through each file
    for file in files:
        # Check if the file is an image (you can extend this check for various image formats)
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.gif'):
            # Append the file name to the list
            image_files.append(shortcode + "/" + file)
        elif file.endswith('.mp4'):
            video_files.append(shortcode + "/" + file)
        elif file.endswith('.txt'):
            text_files.append(shortcode + "/" + file)
    return image_files, text_files,video_files,shortcode


# download_insta_post(
# "https://www.instagram.com/reel/C37B0Kax_fS/?utm_source=ig_web_copy_link"
# )
