#python SilenceCutter.py --input 1_0.mp4 --output 1_1.mp4 --silent_speed 999999

import subprocess
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

'''TODO
Download the video
Cut it up into 5 segments(ish?) determined by the length
input it into the jumpcutter
wait for that and stich back together

Name the input files with the 11 code for youtube urls
'''
def extractIntoSegments(inputFilename):
  ffmpeg_extract_subclip(inputFilename, start_time, end_time, targetname="test.mp4")
 
def stitchTogether(inputFilenameList):
#ffmpeg -i "concat:input1.mpg|input2.mpg|input3.mpg" -c copy output.mpg
  lilo = "\"concat:"
  for filename in inputFilenameList:
    lilo += filename + ".mp4|"
  lilo = lilo[0:len(lilo)-1] + \"
  
  output = "DoneProduct"

def downloadFile(url):
    name = YouTube(url).streams.first().download()
    newname = name.replace(' ','_')
    os.rename(name,newname)
    return newname

def getLength(inputFilename):
  result = subprocess.Popen(["ffprobe", inputFilename],
    stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  return [x for x in result.stdout.readlines() if "Duration" in x]
