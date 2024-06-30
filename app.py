import argparse
from pytube import YouTube
import os

def download_mp3(url):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    download_folder = 'downloads'

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    output_file = audio_stream.download(output_path=download_folder)
    base, ext = os.path.splitext(output_file)
    new_file = base + '.mp3'
    os.rename(output_file, new_file)
    print(f'Pobrano: {new_file}')

while True:
    url = input("Provide YouTube link: ")
    download_mp3(url)
