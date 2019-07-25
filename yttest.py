from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=V4KYWHR1E1c')
(yt.streams
   .filter(progressive=True, file_extension='mp4')
   .order_by('resolution')
   .desc()
   .first()
   .download())