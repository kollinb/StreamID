from flask import render_template, flash, redirect, request, url_for
from app import app
from app.clip import get_clip, get_clips
from app.models import Clip
from urllib.parse import urlparse

@app.route('/')
def index():
    clips = get_clips() # fetch max of 10 clips from db to show

    return render_template('index.html', title='Home', announce="Website currently under development. Use at your own risk.", clips=clips)

@app.route('/clip')
def base_clip():
    return index()

@app.route('/clip/<clip_id>')
def show_clip(clip_id):
    requested_clip = get_clip(clip_id)

    return render_template('clip.html', clip=requested_clip)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404