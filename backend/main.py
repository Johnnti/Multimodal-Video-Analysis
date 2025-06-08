# backend/main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from youtube_video_downloader import download_video
from video_model import get_video_timestamps, get_video_timestamps_url
app = FastAPI()

# Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoRequest(BaseModel):
    url: str

class ChatRequest(BaseModel):
    query: str

@app.post("/process_upload")
async def process_video(req: VideoRequest):
    response = get_video_timestamps(req.url)
    return response
@app.post("/process_url")
async def process_video_url(req: VideoRequest):
    response = get_video_timestamps_url(req.url)
    return response

@app.post("/chat")
async def chat(req: ChatRequest):
    
    return {
        "answer": f"Here's what I found in the video related to: '{req.query}' [timestamp: 60s]"
    }
