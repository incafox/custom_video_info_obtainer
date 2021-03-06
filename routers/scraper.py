from fastapi import APIRouter
from services import service_subtitle_downloader 
from redis import Redis
from rq import Queue
from pydantic import BaseModel
from controllers import subtitles_controller

class ItemExample(BaseModel):
    sentence: str
    number_videos: int

router = APIRouter()
q = Queue(connection=Redis(host='redis'),)

@router.post("/scraper/", tags=["scraper"])
async def scrap_this(data: ItemExample):
    #to redis xd
    q.enqueue(service_subtitle_downloader.general_classifier, data.sentence, data.number_videos)
    return data

@router.get("/scraper/subtitles", tags=["scraper"])
async def get_subtitles():
    subtitles_controller.suntitles_controller()
    return {"username": "fakecurrentuser"}

@router.get("/scraper/{username}", tags=["scraper"])
async def read_user(username: str):
    return {"username": username}
