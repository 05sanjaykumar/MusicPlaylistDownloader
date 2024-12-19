import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import yt_dlp

def getValues():
    # Initialize Selenium WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    playlist_url = "https://www.youtube.com/playlist?list=PLNrotoZZ8BaoXT_LJuwEyESQlctWNDCwD"
    driver.get(playlist_url)
    
    video_list = []
    try:
        elements = driver.find_elements(By.CSS_SELECTOR, "a#video-title")
        for element in elements:
            link = element.get_attribute("href")
            video_title = element.text
            if link and video_title:  # Ensure non-empty values
                video_list.append({"title": video_title, "link": link})
    except Exception as e:
        print(f"An error occurred while fetching video details: {e}")
    finally:
        driver.quit()
    
    # Deduplicate video list by link
    unique_video_list = {video["link"]: video for video in video_list}.values()
    return list(unique_video_list)

def downloadAudioAndSave(video_list):
    destination_folder_directory = createDestinationFolder()
    for video in video_list:
        try:
            # Use video ID to avoid duplicate filenames
            # video_id = video["link"].split("v=")[-1]
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(destination_folder_directory, f"{video['title']}.mp3"),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'ffmpeg_location': '/opt/homebrew/bin/ffmpeg',  # Explicit path to ffmpeg
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video["link"]])
            print(f"Downloaded: {video['title']}")
        except Exception as e:
            print(f"Failed to download {video['title']}: {e}")

def createDestinationFolder():
    destination_folder_directory = "/Users/sanjaykumar/Downloads/testMusic"
    os.makedirs(destination_folder_directory, exist_ok=True)
    return destination_folder_directory

# Main Execution
video_list = getValues()
if video_list:
    print(f"Found {len(video_list)} videos in the playlist:")
    for video in video_list:
        print(f"- {video['title']}")
    downloadAudioAndSave(video_list)
else:
    print("No videos found in the playlist.")
