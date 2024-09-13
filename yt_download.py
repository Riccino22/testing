#from pytube import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress

def download(url):
    yt = YouTube(url)
    ys = yt.streams.get_highest_resolution()
    ys.download()
    #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
    #yt.streams.first().download()
    #return yt.title
    """pydevd warning: Getting attribute YouTube.age_restricted was slow (took 1.04s)
Customize report timeout by setting the `PYDEVD_WARN_SLOW_RESOLVE_TIMEOUT` environment variable to a higher timeout (default is: 0.5s)"""


def download_with_pytubefix(url):
    yt = YouTube(url, on_progress_callback = on_progress)
    ys = yt.streams.get_highest_resolution()
    ys.download()
    

download_with_pytubefix('https://www.youtube.com/live/SC94Jfuz9T0')

