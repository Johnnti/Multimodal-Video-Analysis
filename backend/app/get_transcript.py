from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()
result = ytt_api.fetch('KWgYha0clzw')
text = ''
for snippet in result:
    text += snippet.text
    
print(text)