
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
    #remove newline character
    file = file[:-1]

    #set the destination of the converted file
    #need to rename the extension to .mp4
    start_pos = file.find('/',1)
    destination = targetdir + file[start_pos:]
    end_pos = file.rfind('/')
    filepath = file[start_pos:end_pos]

    #create target directory as needed
    if ( filepath != ''):
        print "creating directory " + filepath
        destdir = targetdir + filepath + '/'
        subprocess.call(["mkdir", "-p", destdir])

    print "Converting to " + destination
    subprocess.call(['ffmpeg', '-stats', '-i', file, '-c:v', 'copy', \
          '-acodec', 'ac3', '-b:a', '640k', '-ac', '6', '-f', 'mp4', \
          destination ])

#copy "file" to "targetdir" preserving file path relative to sourcedir
def copy(file):
    start_pos = file.find('/',1)
    end_pos = file.rfind('/')
    filepath = file[start_pos:end_pos]
    #create target directory as needed
    destdir = targetdir + filepath + '/'
    if ( filepath != ''):
        print "creating directory " + filepath
        subprocess.call(["mkdir", "-p", destdir])
    
    #remove newline character
    file = file[:-1]
    
    print "Copying " + file + " to " + destdir
    subprocess.call(['cp', file, destdir])


#Recursively list files in "directory" into "file" 
def listdir2file(directory, file):
    for filename in os.listdir(directory):
        if (filename[0] != '.'):
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
count = 1
for filename in lines:
    print ("File %d" % count)
    count = count + 1
    extension = filename[filename.rfind('.'):]
    if any(x in extension for x in filetype):
        convert(filename)
    else:
        copy(filename)
    print "END\n\n"

#clean up
f.close()
subprocess.call(['/bin/rm', tempfile])






