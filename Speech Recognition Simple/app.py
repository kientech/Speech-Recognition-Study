import requests
from main import *

filename = "output02.wav"
audio_url = upload(filename)

save_transcript(audio_url, 'file_title')
