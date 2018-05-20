# convert2ac3
Convert the audio stream in movies to AC3. Based on jrottenberg/ffmpeg


###WORK IN PROGRESS###

This project uses jrottenberg/ffmpeg as a base image.
It does the following:

It will convert all files in the SOURCE directory (non recursive) with ffmpeg to change their audio stream to AC3 5.1

It will then write the converted files to the DESTINATION directory using the same name

The container for the video files will also be converted to mp4 while the video stream is just copied over

The full ffmpeg command is as follow:
ffmpeg -stats original- video.mp4 -c:v copy -acodec ac3 -b:a 640k -ac 6 -f mp4 converted-video.mp4

v0.1: Original files are not deleted. Only files in the base directory will be actioned upon. ffmpeg will try to convert all files regardless of type

USAGE:
docker run --rm -v /SOURCE:/media/convert -v /DESTINATION:/media/done een625/convert2ac3

v0.2: Original files are note deleted. All files of type .mp4 .mkv .avi will be processed recursively

USAGE:
docker run --rm -v /SOURCE:/media/convert -v /DESTINATION:/media/done een625/convert2ac3
