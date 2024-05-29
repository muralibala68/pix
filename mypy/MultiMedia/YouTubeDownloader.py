from pytube import YouTube
from typing import Union

count = 0


def on_progress_callback(arg1, arg2: bytes, arg3: int) -> None:
    global count
    count += 1
#    print(f'{count}: Download in progress...;\narg1:{arg1},\narg2:{arg2},\narg3:{arg3}')
    print(f'{count}: Download in progress...;\narg1:{arg1},\narg2:arg2,\narg3:{arg3}')


def on_complete_callback(arg1, arg2: Union[str, None]) -> None:
    print(f'Download complete.\narg1:{arg1},\narg2:{arg2}')


link = "https://youtu.be/F7Q61wdxvw4?si=0XASiMXOParx_9p_"
yt = YouTube(link, on_progress_callback, on_complete_callback)

print("Downloading...")
print("Title: ", yt.title)
print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()
output_dir: str = "./downloads"
yd.download(output_dir)

print("Downloaded ;)")
