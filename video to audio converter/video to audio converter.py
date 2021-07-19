import moviepy.editor
video=moviepy.editor.VideoFileClip("C:\\Users\\ASUS\\PycharmProjects\\pythonProject1\\(video_name).mp4")#location of video
audio_file=video.audio
audio_file.write_audiofile("C:\\Users\\ASUS\\PycharmProjects\\pythonProject1\\(audio_name).mp3")#location you want to store audio