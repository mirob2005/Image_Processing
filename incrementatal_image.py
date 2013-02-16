import sys
import time

inputFile1 = 'wide_beach.ppm'
inputFile2 = 'wide_mountain.ppm'
outputFileString = 'incremental_image'

#Can add auto-size based on files read later
width = 1280
height = 480

print('Start Program', time.clock())
inFile1 = open(inputFile1, 'rb').read()

file1 = inFile1.decode()

file1Pixels = file1.partition('\n255\n')[2]
file1PixelList = file1Pixels.split()

inFile2 = open(inputFile2, 'rb').read()

file2 = inFile2.decode()

file2Pixels = file2.partition('\n255\n')[2]
file2PixelList = file2Pixels.split()

print('Files inputted', time.clock())

maxPixels = width*height

newPixelList = []

RGB = 0
for hpix in range(1,height+1,1):
	for wpix in range(1,width+1,1):
		file1Mult = (width-wpix)/width
		file2Mult = wpix/width
		newPixelList.append(int( (float(file1PixelList[RGB])*file1Mult) + (float(file2PixelList[RGB])*file2Mult) ))
		RGB +=1
		newPixelList.append(int( (float(file1PixelList[RGB])*file1Mult) + (float(file2PixelList[RGB])*file2Mult) ))
		RGB +=1
		newPixelList.append(int( (float(file1PixelList[RGB])*file1Mult) + (float(file2PixelList[RGB])*file2Mult) ))
		RGB +=1


print('Interpolation done', time.clock())

comment = b'# Created by Michael Robertson\n'

image = b'P3\n'+ comment + str.encode(str(width))+b' '+str.encode(str(height))+b'\n'+str.encode(str(255))+b'\n'


try:
	outputFile = outputFileString+'.ppm'
	out = open(outputFile, 'wb')
	out.write(image)
	pixel = 0
	while(pixel < maxPixels*3):
		stringPixels=''
		item = newPixelList[pixel]
		stringPixels = str(item) + ' '
		pixel = pixel+1
		out.write(stringPixels.encode())

	out.write(b'\n')
	out.close()
	print('New File Made', time.clock())

except:
	print('Error in creating PPM! Exiting...')
	sys.exit(0)

