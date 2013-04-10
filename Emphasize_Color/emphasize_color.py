import sys
import time

if len(sys.argv) != 3:
	print('emphasize_color.py fileName.ppm ColorSelected')
	sys.exit(0)


colorSelect = sys.argv[2]
inputFile1 = sys.argv[1]

filename = inputFile1.partition('.ppm')[0]

outputFileString = filename+'_'+colorSelect

print('Start Program', time.clock())
inFile1 = open(inputFile1, 'rb').read()

file1 = inFile1.decode()

file1Pixels = file1.partition('\n255\n')[2]
resolution = file1.partition('\n255\n')[0]
res = resolution.split('\n')[2]
resX = res.split()[0]
resY = res.split()[1]

file1PixelList = file1Pixels.split()

print('File inputted', time.clock())

#Can add check wether the 2 files are the same resolution later...
maxPixels = int(resX)*int(resY)

comment = b'# Created by Michael Robertson\n'

image = b'P3\n'+ comment + str.encode(resX)+b' '+str.encode(resY)+b'\n'+str.encode(str(255))+b'\n'


try:

	outputFile = outputFileString+'.ppm'
	out = open(outputFile, 'wb')
	out.write(image)

	pixel = 0
	while(pixel < maxPixels):
		Red = int(file1PixelList[pixel*3+0])
		Green = int(file1PixelList[pixel*3+1])
		Blue = int(file1PixelList[pixel*3+2])

		newPixelList = []
	
		if((colorSelect == 'Red' and Red>Blue and Red>Green) or (colorSelect == 'Green' and Green>Blue and Green>Red) or (colorSelect == 'Blue' and Blue>Red and Blue>Green)):
			newPixelList.append(Red)
			newPixelList.append(Green)
			newPixelList.append(Blue)
		else:
			total = Red+Green+Blue
			average = int(total/3)
			newPixelList.append(average)
			newPixelList.append(average)
			newPixelList.append(average)

		stringPixels=''
		stringPixels = str(newPixelList[0]) + ' ' + str(newPixelList[1]) + ' ' + str(newPixelList[2]) + ' '
		out.write(stringPixels.encode())
		pixel = pixel+1


	out.write(b'\n')
	out.close()
	print('New File Made', time.clock())


except:
	print('Error in creating PPM! Exiting...')
	sys.exit(0)

