import os, sys, subprocess

command1 = "ffmpeg -stats -i "
command2 = "-c:v copy -acodec ac3 -b:a 640k -ac 6 -c:s copy -f mp4"
sourcedir = sys.argv[1]
targetdir = sys.argv[2]


def convert2ac3(file):
  """convert "abs-file" into ac3 with mp4 container"""
  subprocess.call(['ffmpeg', '-stats', '-i', file, '-c:v', 'copy', '-acodec', 'ac3', '-b:a', '640k', '-ac', '6', '-f', 'mp4', target-dir + file.split('/',2)[2] ])



def listdir2file(directory, file):
  """List files in the "directory" into "file" and 
     recursively call listdir2file for subsequent 
     directories recursively"""
  for filename in os.listdir(directory):
    filename = directory + "/" + filename  
    if os.path.isfile(filename):
      file.write("%s\r\n" % filename)
    else:
      listdir2file(filename, file)

      

f=open(targetdir + "list.txt", "w+")

listdir2file(sourcedir, f)

f.close()

f=open(targetdir + "list.txt", "r")

lines = f.readlines()

for item in lines:
  #if item ends in .mp4 .mkv .avi, convert
  print item

f.close()















"""
1. List files in source directory, and write the full path into a dir-file

2. For each line in dir-file:
  if it's .avi, .mp4, .mkv, convert using ffmpeg to new location.
  if it's not copy as is to new location
t
"""



"""
os.path.isfile("bob.txt") # Does bob.txt exist?  Is it a file, or a directory?
os.path.isdir("bob")
f=open("guru99.txt", "a+")
f.write("Appended line %d\r\n" % (i+1))
f.close()

tim.split(':', 1) # split() only once
['16', '30:10']
f=open("/rootlist.txt", "a+")

""" 


"""
for filename in os.listdir(sys.argv[1]):
  subprocess.call(['ffmpeg', '-stats', '-i', sys.argv[1] + filename, '-c:v', 'copy', '-acodec', 'ac3', '-b:a', '640k', '-ac', '6', '-f', 'mp4', sys.argv[2] + filename])
  #subprocess.call(['/bin/rm', sys.argv[1] + filename])
"""

