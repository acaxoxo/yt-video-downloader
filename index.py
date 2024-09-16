import yt_dlp

video_url = 'https://www.youtube.com/watch?v=GPNPEiSqwdI'
    
ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print('Download selesai!') 