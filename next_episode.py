import os
import sys

#reading the next video from save file (if it exists)
save_file = str()
next_video = str()
if os.path.exists("next"):
	save_file = open("next", "r+")
	next_video = save_file.readline()
else:
	next_video = ""

#opening save file for writing and creating if doesnt exist
save_file = open("next", "w+")

#getting list of files in current directory
files = os.listdir('./')


# getting the extension of the video format (e.g. .mkv .avi .mp4 etc.)
# first getting extention count in directory
extentions = dict()
for f in files:
	for i in range(len(f)-1, -1, -1):
		if(f[i] == '.'):
			ext = f[i:];
			if ext in extentions:
				extentions[ext] += 1;
			else:
				extentions[ext] = 1;
			break;
# extention with highest count is the video format
# (e.g. [".txt"] = 1 vs [".avi"] = 13)
extension = str()
ext_count = 0
for key in extentions.keys():
	if extentions[key] > ext_count:
		extention = key;
		ext_count = extentions[key]


# getting the list of videos with extention
videos = list()
for f in files:
	if f.endswith(extention):
		videos.append('\"' + f + '\"')
videos.sort()

# starting the video and saving the next
print ('Starting '),
if(len(next_video) == 0):
	print videos[0]
	os.system('vlc ' + videos[0])		# linux
	#os.startfile(videos[0])			# windows?
	save_file.write(str(2))
else:
	episode = int(next_video) - 1
	print videos[episode]
	os.system('vlc ' + videos[episode])	# linux 
	# os.startfile(videos[episode])		# windows?
	save_file.write(str(episode + 2));	

# closing save file
save_file.close()