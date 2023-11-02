import os
from pytube import YouTube
from moviepy.editor import VideoFileClip, concatenate_videoclips


def processing_video(video_url, to_first, from_second, output_filename):
    # Scarica il video da YouTube
    # yt = YouTube(video_url)
    # stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    # stream.download(filename="temp_video.mp4")

    # Taglia il video
    with VideoFileClip("temp_video.mp4") as video:
        # Taglia il video in prima parte e seconda parte
        first_part = video.subclip(0, to_first)
        second_part = video.subclip(from_second, video.duration)
        
        # Unisce le parti del video
        final_clip = concatenate_videoclips([first_part, second_part])

        # Salva l'audio in un file
        audio = final_clip.audio

         # Salva l'audio in un file, specificando la frequenza di campionamento
        audio.write_audiofile(output_filename, 
                              fps=audio.fps if hasattr(audio, 'fps') else 44100)

        # Chiudi e rilascia le risorse
        audio.close()

    # Elimina il file video temporaneo
    # os.remove("temp_video.mp4")



######à# Processing del video

# scarica video, taglie le due parti che ci servono e uniscile
url = "https://www.youtube.com/watch?v=fVCAFvIq_F8"
to_first = 53.5
from_second = 97
output_filename = 'audio_matrimonio.wav'

processing_video(url, to_first, from_second, output_filename)