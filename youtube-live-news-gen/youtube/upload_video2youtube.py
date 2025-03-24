from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo
from datetime import datetime
import os

date_str = datetime.now().strftime('%Y-%m-%d')

dname = "F:/certifications/IIITH-AIML/research/imagen/banner/"
folder = os.path.join(dname, datetime.now().strftime('%Y-%m-%d'))
youtube_dir = dname + "/youtube/"
fname = folder+"/todays-headlines.mp4"

# loggin into the channel
channel = Channel()
#channel.login(youtube_dir+"client_secret_desktop.json", youtube_dir+"credentials.storage")
channel.login(youtube_dir+"client_secret_ainews.json", youtube_dir+"credentials_bawai.storage")


# setting up the video that is going to be uploaded
video = LocalVideo(file_path=fname)

# setting snippet
video.set_title("Today's Top headlines | " + date_str + " | AI NEWS | #news #topheadlinestoday #todaytopheadlines")
video.set_description("Watch this video for today's top headlines by AI. A simple, straight and noiseless AI news headlines. Top trending headlines and top news articls today. You will see Top headlines by sections. Top news in india today, top news headlines in movies-etertainment, top news headlines in sports, top news headlines in education and top news headlines in technology. Sourced from India today, For full news please visit: https://www.indiatoday.in/news.html")
video.set_tags(["news", "topheadlines", "trendingnews", "ai", "ainews"])
video.set_category("news")
video.set_default_language("en-US")

# setting status
video.set_embeddable(True)
video.set_license("creativeCommon")
video.set_privacy_status("public")
video.set_public_stats_viewable(True)

# setting thumbnail
video.set_thumbnail_path(youtube_dir+'top_headlines_thumbnail.png')

#add video to playlist
playlist_id = 'PLdfZfXRKqSMUlXXCF88dlO4EYBg6I6tMs'
#video.set_playlist(playlist_id)
#channel.add_video_to_playlist(playlist_id, video)

# uploading video and printing the results
video = channel.upload_video(video)

print(video.id)
print(video)

# liking video
#video.like()
