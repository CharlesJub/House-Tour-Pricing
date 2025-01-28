import re
from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd
import scrapetube
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi

from api_key import api_key


def get_transcript(video_id):
    """Get English or US English transcriptions for YouTube Video"""
    try:
        return YouTubeTranscriptApi.get_transcript(video_id)
    except Exception:
        try:
            return YouTubeTranscriptApi.get_transcript(video_id, languages=["en-US"])
        except Exception:
            print(f"Error fetching transcript for video {video_id}")
            return None


def scrape_channel_videos(channel_id):
    """Scrape all Videos from a YouTube channel"""
    videos = scrapetube.get_channel(channel_id=channel_id)
    video_ids = [video["videoId"] for video in videos]
    print(f"Total videos found: {len(video_ids)}")

    transcripts = {}
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_video = {
            executor.submit(get_transcript, video_id): video_id
            for video_id in video_ids
        }
        for future in as_completed(future_to_video):
            video_id = future_to_video[future]
            try:
                transcript = future.result()
                if transcript:
                    transcripts[video_id] = transcript
            except Exception as e:
                print(f"Error processing video {video_id}: {str(e)}")

    print(f"Successfully fetched transcripts for {len(transcripts)} videos")
    return transcripts


def remove_text_in_parentheses(text):
    return re.sub(r"\([^()]*\)", "", text)


def find_numbers_and_following_word(text):
    return re.findall(r"\b(\d+(?:\.\d+)?)\s+(\w+)\b", text)


def process_transcripts(transcripts):
    for video_id, transcript_list in transcripts.items():
        script = "\n".join(item["text"].strip() for item in transcript_list)
        script = remove_text_in_parentheses(script)
        transcripts[video_id] = {"script": script}
    return transcripts


def get_video_details(youtube, video_id):
    try:
        request = youtube.videos().list(part="snippet", id=video_id)
        response = request.execute()
        video_info = response["items"][0]["snippet"]
        return video_info["title"], video_info["description"]
    except Exception as e:
        print(f"Error fetching details for video {video_id}: {str(e)}")
        return None, None


def remove_text_in_parentheses(text):
    return re.sub(r"\([^()]*\)", "", text)


def find_numbers_and_following_word(text):
    return re.findall(r"\b(\d+(?:\.\d+)?)\s+(\w+)\b", text)


def process_transcripts(transcripts):
    for transcript_key in transcripts:
        # Get the list of dictionaries for the current transcript
        transcript_list = transcripts[transcript_key]

        # Join all text entries with newlines
        script = "\n".join(item["text"].strip() for item in transcript_list)

        # Remove text in parentheses
        script = remove_text_in_parentheses(script)

        # Store the processed script back in the dictionary
        transcripts[transcript_key] = {"script": script}

    return transcripts


def get_video_details(youtube, video_id):
    request = youtube.videos().list(part="snippet", id=video_id)
    response = request.execute()

    video_info = response["items"][0]["snippet"]
    title = video_info["title"]
    description = video_info["description"]

    return title, description


youtube = build("youtube", "v3", developerKey=api_key)


def main():

    channel_id = "UCHWbZM3BIGgZksvXegx_h3w"

    transcripts = scrape_channel_videos(channel_id)

    transcripts_clean = process_transcripts(transcripts)

    for video_id in transcripts_clean:
        title, description = get_video_details(youtube, video_id)
        transcripts_clean[video_id]["title"] = title
        transcripts_clean[video_id]["description"] = description

    df = pd.DataFrame(transcripts_clean).transpose().reset_index(names="id")

    non_asset_videos = [
        "s2aDACZZEN8",
        "ZBxUruN_E9o",
        "VpxGxfuJQFo",
        "gKh0TdDRbaQ",
        "s407qS-5UAU",
        "VibvmP4s72w",
    ]
    df_filtered = df[~df["id"].isin(non_asset_videos)]
    df_filtered.to_csv("video_info.csv", index=False)


if __name__ == "__main__":
    result = main()
