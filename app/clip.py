import os
import json
import requests
import subprocess
from urllib.parse import urlparse
from app import app, db
from app.models import Clip
from flask import url_for

clip_api_base = "https://api.twitch.tv/helix/clips?id="
ffmpeg_path = os.path.join(os.path.dirname(app.instance_path), 'dependencies', 'ffmpeg.exe')
video_folder = os.path.join(app.root_path, 'static', 'clips', 'video')
audio_folder = os.path.join(app.root_path, 'static', 'clips', 'audio')

# fetches up to 10 clips already in the databse for display on homepage
def get_clips():
    clips = Clip.query.limit(10).all()

    return clips

# Get or create the database entry for the Clip with the specified clip_id
def get_clip(clip_id):
    clip = Clip.query.get(clip_id)
    exists = clip is not None # wheter or not this clip is already in the DB

    if exists:
        return clip
    else:
        clip_api_data = get_clip_data(clip_id)
        clip_mp4_req = requests.get(clip_api_data['mp4_url'])
        video_input = os.path.join(video_folder, (clip_id + '.mp4'))
        audio_output = os.path.join(audio_folder, (clip_id + '.aac'))
        with open(video_input, 'wb+') as f:
            f.write(clip_mp4_req.content)
        subprocess.call([ffmpeg_path, '-i', video_input, '-vn', '-acodec', 'copy', audio_output])
        clip = Clip(id=clip_id, title=clip_api_data['title'], broadcaster_name=clip_api_data['broadcaster'], thumb_url=clip_api_data['thumb_url'])
        db.session.add(clip)
        db.session.commit()
        return clip

# Retrieves API data for this clip from twitch and passes
# the necessary parsed info along in a dictionary
def get_clip_data(clip_id):
    if 'TWITCH_API_KEY' not in app.config or \
        not app.config['TWITCH_API_KEY']:
        return 'ERROR: Clip audio generator is not configured'

    url = (clip_api_base + clip_id)
    api_client_id = {'Client-ID': app.config['TWITCH_API_KEY'] }
    clip_data = requests.get(url, headers=api_client_id).json()
    clip_data = clip_data['data'][0]

    clip = dict()
    clip['title'] = clip_data['title']
    clip['thumb_url'] = clip_data['thumbnail_url']
    thumb_url = clip['thumb_url']
    clip['mp4_url'] = thumb_url[:(thumb_url.index('-preview-'))] + '.mp4'
    clip['broadcaster'] = clip_data['broadcaster_name']

    return clip