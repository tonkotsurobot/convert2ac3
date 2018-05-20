
"""
1. List files in source directory into a file

2. For each file:
  if it's .avi, .mp4, .mkv, convert using ffmpeg to new location.
  if it's not copy as is to new location

3. (optional) delete original files if successful
"""



import os
import sys
import subprocess


command1 = "ffmpeg -stats -i "
command2 = "-c:v copy -acodec ac3 -b:a 640k -ac 6 -c:s copy -f mp4"
sourcedir = sys.argv[1]
targetdir = sys.argv[2]
filetype = ['avi', 'mkv', 'mp4']
tempfile = targetdir + '/' + "list.txt"


#convert video "file" to have ac3 5.1 audio and mp4 container#
def convert(file):
    subprocess.call(['ffmpeg', '-stats', '-i', file, '-c:v', 'copy', \
          '-acodec', 'ac3', '-b:a', '640k', '-ac', '6', '-f', 'mp4', \
          targetdir + file.split('/',2)[2] ])


#copy "file" to "targetdir" preserving file path relative to sourcedir
def copy(file):
    #remove newline character
    filename = file[:-1]

    #get path of file relative to sourcedir
    filepath = os.path.dirname(file).split('/',2)[-1]

    #define destination directory (targetdir + relative dir)
    destdir = targetdir + '/' + filepath

    #create destination directory as needed and copy the file
    if (filename != ''):
        print targetdir + " plus " + filepath
        print "creating directory " + destdir
        subprocess.call(["mkdir", "-p", destdir])
        subprocess.call(['cp', filename, destdir])


#Recursively list files in "directory" into "file" 
def listdir2file(directory, file):
    for filename in os.listdir(directory):
        filename = directory + "/" + filename  
        if os.path.isfile(filename):
            file.write("%s\n" % filename)
        else:
            listdir2file(filename, file)


      
#MAIN PROGRAM
#prepare temporary file in target directory
f=open(tempfile, "w+")

#list all files in source directory
listdir2file(sourcedir, f)

#either copy or process the files listed
f.seek(0)
lines = f.readlines()
for filename in lines:
    extension = filename.split('.',-1)[-1]
    if any(x in extension for x in filetype):
        print "Converting " + filename
        #convert(filename)
        copy(filename)
    else:
        print "Copying " + filename
        copy(filename)

#clean up
f.close()
subprocess.call(['/bin/rm', tempfile])






"""
for filename in os.listdir(sys.argv[1]):
  subprocess.call(['ffmpeg', '-stats', '-i', sys.argv[1] + filename, '-c:v', 'copy', '-acodec', 'ac3', '-b:a', '640k', '-ac', '6', '-f', 'mp4', sys.argv[2] + filename])
  #subprocess.call(['/bin/rm', sys.argv[1] + filename])


1. List files in source directory into a file

2. For each file:
  if it's .avi, .mp4, .mkv, convert using ffmpeg to new location.
  if it's not copy as is to new location

3. (optional) delete original files if successful

os.path.isfile("bob.txt") # Does bob.txt exist?  Is it a file, or a directory?
os.path.isdir("bob")
f=open("guru99.txt", "a+")
f.write("Appended line %d\r\n" % (i+1))
f.close()

tim.split(':', 1) # split() only once
['16', '30:10']
f=open("/rootlist.txt", "a+")


for filename in os.listdir(sys.argv[1]):
  subprocess.call(['ffmpeg', '-stats', '-i', sys.argv[1] + filename, '-c:v', 'copy', '-acodec', 'ac3', '-b:a', '640k', '-ac', '6', '-f', 'mp4', sys.argv[2] + filename])
  #subprocess.call(['/bin/rm', sys.argv[1] + filename])
"""

