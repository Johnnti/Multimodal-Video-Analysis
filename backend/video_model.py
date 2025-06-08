from google import genai
from google.genai import types
from dotenv import load_dotenv  
import os 
import time
from youtube_video_downloader import download_video
from pydantic import BaseModel
import json

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

# video_url = "https://youtu.be/KWgYha0clzw"

class timeStamp(BaseModel):
      timestamp: str
      caption: str
      
def get_video_timestamps(video_url):
      video_title = download_video(video_url)

      myfile = client.files.upload(file=rf".\media\{video_title}.mp4")

      #use a while loop to wait for video to upload
      while myfile.state == "PROCESSING":
            print('Waiting for video to be processed.')
            time.sleep(5)
            myfile = client.files.get(name=myfile.name)

      response = client.models.generate_content(
      model="gemini-2.0-flash", contents = [myfile, """generate hyperlink timestamps for the events in this
                                                video in clever way by chunking the video into sections and captioning each section. Let the caption be short and descriptive
                                          your output should be in the format {<a>00:00</a>: <p>caption</p>} as a python list of dictionary elements.
                                                """]
      ,config = types.GenerateContentConfig(
            response_mime_type='application/json',
            response_schema = list[timeStamp]
      )
      )

      return response.text

def get_video_timestamps_url(video_url):
      response = client.models.generate_content(
            model="gemini-2.0-flash",contents = types.Content(
                  parts=[
                        types.Part(
                              file_data = types.FileData(file_uri=video_url)
                        ),
                        types.Part(
                              text = """generate hyperlink timestamps for the events in this
                                                video in clever way by chunking the video into sections and captioning each section. Let the caption be short and descriptive
                                          your output should be in the format {<a>00:00</a>: <p>caption</p>} in an array.
                                                """
                        )
                  ]
            ),
            config= types.GenerateContentConfig(
                  response_mime_type='application/json',
                  response_schema= list[timeStamp]
            )
            
      )
      print(json.loads(response.text))
      return response.text


get_video_timestamps_url("https://youtu.be/KWgYha0clzw")