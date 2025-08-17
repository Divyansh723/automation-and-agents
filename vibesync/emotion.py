import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()

ASSEMBLYAI_API_KEY = os.getenv('ASSEMBLYAI_API_KEY')  # Make sure to set this in your .env file

def upload_audio(filename):
    headers = {'authorization': ASSEMBLYAI_API_KEY}
    with open(filename, 'rb') as f:
        response = requests.post('https://api.assemblyai.com/v2/upload', headers=headers, data=f)
    response.raise_for_status()
    upload_url = response.json()['upload_url']
    return upload_url

def request_emotion_transcript(audio_url):
    endpoint = "https://api.assemblyai.com/v2/transcript"
    json_data = {
        "audio_url": audio_url,
        "sentiment_analysis": True,   # enables emotion/sentiment analysis
    }
    headers = {
        "authorization": ASSEMBLYAI_API_KEY,
        "content-type": "application/json"
    }
    response = requests.post(endpoint, json=json_data, headers=headers)
    response.raise_for_status()
    transcript_id = response.json()['id']
    return transcript_id

def get_transcript_result(transcript_id):
    endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
    headers = {"authorization": ASSEMBLYAI_API_KEY}
    while True:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        status = response.json()['status']
        if status == 'completed':
            return response.json()
        elif status == 'error':
            raise Exception("Transcription failed:", response.json())
        else:
            print(f"Waiting for transcript... status: {status}")
            time.sleep(5)

if __name__ == "__main__":
    filename = "voice_clip.wav"
    print("Uploading audio...")
    audio_url = upload_audio(filename)
    print("Requesting transcription and emotion analysis...")
    transcript_id = request_emotion_transcript(audio_url)
    result = get_transcript_result(transcript_id)

    # Print the sentiment analysis part
    sentiment = result.get("sentiment_analysis_results")
    print("Sentiment/Emotion analysis results:")
    if sentiment:
        for segment in sentiment:
            print(f"Start: {segment['start']}, End: {segment['end']}, Sentiment: {segment['sentiment']}, Confidence: {segment['confidence']}")
    else:
        print("No sentiment analysis data found.")
