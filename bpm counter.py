from logging import exception

import librosa
import yt_dlp
import os
import warnings
warnings.filterwarnings("ignore")

print("This is a bpm counter paste in any link it'll show the bpm")
while True:
    music_link= input("Paste in the link or type exit").strip()
    if music_link.lower()== "exit":
        print("")
        break
    try:
        print("Processsing")
        ydl_opts ={
            'quiet': True,
            'no_warnings' : True,
            'format' : 'bestaudio/best',
            'outtmpl' : 'temp_song.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([music_link])
        audio_data , sample_rate =librosa.load("temp_song.mp3")

        tempo, beat_frames=librosa.beat.beat_track(y=audio_data,sr=sample_rate)
        duration_seconds= librosa.get_duration(y=audio_data, sr=sample_rate)
        mins, secs= divmod(int(duration_seconds),60)
        print("")
        print(f"bpm for ts is {round(float(tempo))} and {mins}:{secs:02d} long")
        print("")
        print("tempo")
        if tempo <80:
            print("slow tempo")
        elif 80<= tempo <=120:
            print("mid tempo")
        elif 120<= tempo <= 150:
            print("high tempo")
        else:
            print("really high tempo")
    except Exception as e:
        print(f"Something went wrong:{e}")
    finally:
        if os.path.exists("temp_song.mp3"):
            os.remove("temp_song.mp3")