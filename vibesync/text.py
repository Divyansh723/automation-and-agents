import os
import requests
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from googleapiclient.discovery import build

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
HUME_API_KEY = os.getenv('HUME_API_KEY')

def test_spotify():
    print("\nTesting Spotify API...")
    try:
        auth_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
        sp = Spotify(auth_manager=auth_manager)
        results = sp.search(q="Chill", type='playlist', limit=5)
        print("Raw Spotify search response:", results)  # DEBUG
        playlists = results.get('playlists', {}).get('items', [])
        # Filter out None items
        playlists = [p for p in playlists if p]
        if playlists:
            playlist = playlists[0]
            print("Spotify API works! Found playlist:", playlist['name'])
        else:
            print("Spotify API search returned no valid playlists.")
    except Exception as e:
        print("Spotify API test failed:", e)


def test_youtube():
    print("\nTesting YouTube API...")
    try:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        request = youtube.search().list(q='happy music', part='snippet', maxResults=1)
        response = request.execute()
        video_title = response['items'][0]['snippet']['title']
        print("YouTube API works! Sample video title:", video_title)
    except Exception as e:
        print("YouTube API test failed:", e)

def test_hume():
    print("\nTesting Hume API (mock test)...")
    try:
        url = 'https://api.hume.ai/v1alpha/detect/prod'
        headers = {
            'Authorization': f'Bearer {HUME_API_KEY}',
            'Content-Type': 'application/json',
        }
        payload = {
            "requests": [
                {
                    "features": [
                        {"type": "EMOTION_RECOGNITION"}
                    ],
                    "media": {
                        # Using a real public image URL for testing
                        "image_url": "https://i.imgur.com/ZXBtVw7.jpg"
                    }
                }
            ]
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            print("Hume API works! Response received.")
        else:
            print(f"Hume API responded with status {response.status_code}: {response.text}")
    except Exception as e:
        print("Hume API test failed:", e)

if __name__ == "__main__":
    test_spotify()
    test_youtube()
    test_hume()
