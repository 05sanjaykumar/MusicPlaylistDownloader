import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pytube import YouTube

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def getValues():
    playlist_url = "https://www.youtube.com/playlist?list=PLBlnK6fEyqRgp46KUv4ZY69yXmpwKOIev"
    driver.get(playlist_url)

    try:
        elements = driver.find_elements(By.CSS_SELECTOR, "a#video-title")
        video_list = []
        for element in elements:
            link = element.get_attribute("href")
            video_title = element.text
            video_list.append({"title": video_title, "link": link})


    except Exception as e:
        print(f"An error occurred: {e}")

    driver.quit()
    return video_list

video_list = getValues()


destination_folder_directory = "/Users/sanjaykumar/Downloads/testMusic"

os.makedirs(destination_folder_directory, exist_ok=True)

