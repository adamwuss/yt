import argparse
from pytube import YouTube
import os

def download_mp3(url):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    output_file = audio_stream.download()
    base, ext = os.path.splitext(output_file)
    new_file = base + '.mp3'
    os.rename(output_file, new_file)
    print(f'Pobrano: {new_file}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pobierz audio z YouTube jako MP3')
    parser.add_argument('url', type=str, help='URL filmu z YouTube')
    args = parser.parse_args()
    download_mp3(args.url)
