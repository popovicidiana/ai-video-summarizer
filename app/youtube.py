from youtube_transcript_api import YouTubeTranscriptApi

def fetch_transcript(video_id):

    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id)
    transcript_text = '\n'.join([line.text for line in transcript])
    return transcript_text
