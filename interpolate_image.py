import sys
import time

inputFile1 = 'rocky_beach.ppm'
inputFile2 = 'mountain.ppm'
outputFileString = 'interpolation'

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

#Can add check wether the 2 files are the same resolution later...
numSteps = 2
maxPixels = 1228800

newPixelList = []
a = 1/numSteps

newPixelList = {}

count = 1
while count < numSteps:
	newPixelList[count] = []
	count = count +1

count = 1
while count < numSteps:
	pixel = 0
	while(pixel < maxPixels*3):
		newPixelList[count].append(int((1-(a*count))*int(file1PixelList[pixel])+a*count*int(file2PixelList[pixel])))
		pixel = pixel +1
	count = count +1

print('Interpolation done', time.clock())

comment = b'# Created by Michael Robertson\n'

image = b'P3\n'+ comment + str.encode(str(1280))+b' '+str.encode(str(960))+b'\n'+str.encode(str(255))+b'\n'


try:


	count = 1
	while count < numSteps:
		outputFile = outputFileString+str(count)+'.ppm'
		out = open(outputFile, 'wb')
		out.write(image)
		#print(time.clock())
		pixel = 0
		while(pixel < maxPixels*3):
			stringPixels=''
			item = newPixelList[count][pixel]
			stringPixels = str(item) + ' '
			pixel = pixel+1
			out.write(stringPixels.encode())

		out.write(b'\n')
		out.close()
		print('New File Made', time.clock())
		count = count +1
	
		


except:
	print('Error in creating PPM! Exiting...')
	sys.exit(0)

