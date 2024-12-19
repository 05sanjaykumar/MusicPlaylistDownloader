import requests
from bs4 import BeautifulSoup

playlist_url = "https://www.youtube.com/playlist?list=PLBlnK6fEyqRgp46KUv4ZY69yXmpwKOIev"

# Fetch the HTML content
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(playlist_url, headers=headers)

# Parse the content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all video links
video_links = soup.find_all('ytm-playlist-video-renderer')
print('extracting...')
# Extract URLs
print(video_links)


print('extraction completed!')