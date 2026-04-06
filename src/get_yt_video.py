from youtubesearchpython import VideosSearch

def get_yt_video_link(query):
    videosSearch = VideosSearch(query=query, limit=3)
    result = videosSearch.result()
    video_titles = [video['title'] for video in result['result']]
    video_links = [video['link'] for video in result['result']]
    return video_titles, video_links