# convert2ac3
Convert the audio stream in movies to AC3. Based on jrottenberg/ffmpeg

### WHY?
- I have a Sonos playbar 5.1 setup at home and it only plays 5.1 stream if it is encoded in AC3 format.
Thus any digital movies I have need to converted to this format while preserving the video stream.
Rather than manually converting each file, I just dump all the files in the "SOURCE" folder and run an ephemeral ffmpeg container to convert them
- mp4 container for movies are also more media player friendly


This project uses [jrottenberg/ffmpeg](https://hub.docker.com/r/jrottenberg/ffmpeg/) as a base image.


It does the following:

- It will convert all files in the SOURCE directory with ffmpeg to change their audio stream to AC3 5.1

- It will then write the converted files to the DESTINATION directory using the same name

- The container for the video files will also be converted to mp4 while the video stream is just copied over


The full ffmpeg command is as follow:
ffmpeg -stats original- video.mp4 -c:v copy -acodec ac3 -b:a 640k -ac 6 -f mp4 converted-video.mp4


### USAGE:
/media/convert and /media/done are the source and destination directory of your video files respectively


docker run --rm -v /SOURCE:/media/convert -v /DESTINATION:/media/done een625/convert2ac3

### Version history
- v0.1: Original files are not deleted. Only files in the base directory will be actioned upon. ffmpeg will try to convert all files regardless of type

- v0.2: Original files are note deleted. All files of type .mp4 .mkv .avi will be processed recursively
