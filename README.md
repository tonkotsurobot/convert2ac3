# convert2ac3
Convert the audio stream in movies to AC3. Based on jrottenberg/ffmpeg


###WORK IN PROGRESS###

This project uses jrottenberg/ffmpeg as a base image.
It does the following:

It will convert all files in the SOURCE directory (non recursive) with ffmpeg to change their audio stream to AC3 5.1
It will then write the converted files to the DESTINATION directory using the same name
The container for the video files will also be converted to mp4 while the video stream is just copied over
Subtitles are copied over
The full ffmpeg command is as follow:
ffmpeg -stats original- video.mp4 -c:v copy -acodec ac3 -b:a 640k -ac 6 -c:s copy -f mp4 converted-video.mp4
USAGE:
docker run --rm -v /SOURCE:/media/convert -v /DESTINATION:/media/done een625/convert2ac3
