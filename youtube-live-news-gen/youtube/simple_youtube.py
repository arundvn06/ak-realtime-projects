from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo
from datetime import datetime
import os

date_str = datetime.now().strftime('%Y-%m-%d')


def upload_video(youtube_dir, video_fname, thumbnail_fname, playlist_id, title, description, tags, category, language, privacy):

    print("Uploading video to your youtube channel.")
    # loggin into the channel
    channel = Channel()
    #channel.login(youtube_dir+"client_secret_desktop.json", youtube_dir+"credentials.storage")
    channel.login(youtube_dir+"client_secret_ainews.json", youtube_dir+"credentials_bawai.storage")


    # setting up the video that is going to be uploaded
    video = LocalVideo(file_path=video_fname)

    # setting snippet
    video.set_title(title)
    video.set_description(description)
    video.set_tags(tags)
    video.set_category(category)
    video.set_default_language(language)

    # setting status
    video.set_embeddable(True)
    video.set_license("creativeCommon")
    video.set_privacy_status(privacy)
    video.set_public_stats_viewable(True)

    # setting thumbnail
    if thumbnail_fname != "":
        video.set_thumbnail_path(thumbnail_fname)

    #add video to playlist
    #playlist_id = 'PLdfZfXRKqSMUlXXCF88dlO4EYBg6I6tMs'
    #video.set_playlist(playlist_id)
    #channel.add_video_to_playlist(playlist_id, video)

    # uploading video and printing the results
    video = channel.upload_video(video)

    print(video.id)
    print("Video uploaded to your youtube channel.")
    
    
def upload_india_headlines(youtube_dir, video_fname, thumbnail_fname):
    title = "Today's Top headlines | " + date_str + " | AI NEWS | #news #topheadlinestoday #todaytopheadlines"
    description = "Watch this video for today's top headlines by AI. A simple, straight and noiseless AI news headlines. Top trending headlines and top news articls today. You will see Top headlines by sections. Top news in india today, top news headlines in movies-etertainment, top news headlines in sports, top news headlines in education and top news headlines in technology. Sourced from India today, For full news please visit: https://www.indiatoday.in/news.html"
    tags = ["news", "topheadlines", "trendingnews", "ai", "ainews"]
    category = "news"
    language = "en-US"
    playlist_id = 'PLdfZfXRKqSMUlXXCF88dlO4EYBg6I6tMs'
    privacy = "public"
    upload_video(youtube_dir, video_fname, thumbnail_fname, playlist_id, title, description, tags, category, language, privacy)
    
def upload_world_headlines(youtube_dir, video_fname, thumbnail_fname):
    title = "World Top headlines | " + date_str + " | AI NEWS | #worldnews #topheadlinestoday #todaytopheadlines"
    description = "Watch this video for today's top headlines by AI. A simple, straight and noiseless AI news headlines. Top trending headlines and top news articls today. You will see Top headlines by sections. Top news in india today, top news headlines in movies-etertainment, top news headlines in sports, top news headlines in education and top news headlines in technology. Sourced from India today, For full news please visit: https://www.indiatoday.in/news.html"
    tags = ["news", "toptrends", "todaytrends", "worldnews", "ai", "ainews", 'internationalnews']
    category = "news"
    language = "en-US"
    playlist_id = 'PLdfZfXRKqSMUlXXCF88dlO4EYBg6I6tMs'
    privacy = "public"
    upload_video(youtube_dir, video_fname, thumbnail_fname, playlist_id, title, description, tags, category, language, privacy)    
    
def upload_youtube_trends(youtube_dir, video_fname, thumbnail_fname):
    title = "Youtube Trends as on | " + date_str + " | #youtube #trends #youtube_trends #viral #youtubevideos"
    description = "Top trendig videos and shorts of the day in music, movies and over all."
    tags = ["youtube", "toptrends", "todaytrends", "trends", "ai", "youtubevideos", 'viral']
    category = "entertainment"
    language = "en-US"
    playlist_id = 'PLdfZfXRKqSMUlXXCF88dlO4EYBg6I6tMs'
    privacy = "public"
    upload_video(youtube_dir, video_fname, thumbnail_fname, playlist_id, title, description, tags, category, language, privacy)        