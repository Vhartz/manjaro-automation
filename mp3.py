#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import youtube_dl

# FAZ DOWNLOAD DE VIDEOS DO YOUTUBE EM MP3 COM YOUTUBE-DL

music = input("  URL : \t")

ydl_opts = {'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'}],
        'postprocessor_args': [
        '-ar', '16000'],
        'prefer_ffmpeg': True,
        'keepvideo': True
        }

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([music])
