from youtube_transcript_api import YouTubeTranscriptApi
from youtube_search import YoutubeSearch
import json
from .customs.custom_video_info import VideoInfo

def get_videos_related_by_id(term, number_videos):
    results = YoutubeSearch(term + ' scene', max_results=number_videos).to_json()
    json_object = json.loads(results)
    json_formatted_str = json.dumps(json_object, indent=2)
    # return json_formatted_str
    # print(json_formatted_str)
    return json_object['videos']
# SOLO importan los segundos inciales: "start"
# receive an array of videos and process by index

def get_general_info_video(video):
        subtitles = []
        try:
            subtitles = YouTubeTranscriptApi.get_transcript(video['id'],languages=['en'])
        except:
            pass
        return VideoInfo(id=video['id'], views=video['views'], thumbnail=video['thumbnails'], url_suffix=video['url_suffix'], channel=video['channel'], duration=video['duration'], subtitles=subtitles, subtitles_available=len(subtitles)>0)

# final function
def general_classifier(sentence, number_videos):
    print("analyzing", sentence, number_videos)
    num_of_videos = number_videos
    str_videos_list= get_videos_related_by_id(sentence, num_of_videos)
    for video in list(str_videos_list):
        print("------------ %s ------------","id de video",video['id'])
        info_video_obj = get_general_info_video(video)
        info_video_obj.save_on_db()

