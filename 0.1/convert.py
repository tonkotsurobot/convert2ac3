import os, sys, subprocess

command1 = "ffmpeg -stats -i "
command2 = "-c:v copy -acodec ac3 -b:a 640k -ac 6 -c:s copy -f mp4"
for filename in os.listdir(sys.argv[1]):
  subprocess.call(['ffmpeg', '-stats', '-i', sys.argv[1] + filename, '-c:v', 'copy', '-acodec', 'ac3', '-b:a', '640k', '-ac', '6', '-c:s', 'copy', '-f', 'mp4', sys.argv[2] + filename])
  subprocess.call(['/bin/rm', sys.argv[1] + filename])
