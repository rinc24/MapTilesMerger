from PIL import Image
import argparse
import os
import sys


def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]


def get_immediate_files(dir):
    return [name for name in os.listdir(dir)
            if os.path.isfile(os.path.join(dir, name))]


print "Start map tiles merge..."

parser = argparse.ArgumentParser()

parser.add_argument("-i", action="store", dest='baseDir', help="Input directory path")
parser.add_argument("-o", action="store", dest='destinationFile', help="Output file path")
args = parser.parse_args()

if not args.baseDir:
    print "Error! Input directory is not specified. Please user -i argument."
    sys.exit()
else:
    baseDir = args.baseDir

if not args.destinationFile:
    print "Error! Output file is not specified. Please user -o argument."
    sys.exit()
else:
    destinationFile = args.destinationFile

try:
    baseDirectoryContent = get_immediate_subdirectories(baseDir)
except:
    print "Error! Base directory not found."
    sys.exit()
verticalTilesCount = len(baseDirectoryContent)

if verticalTilesCount == 0:
    print "Error! Base directory is empty."
    sys.exit()

firstDirectoryContent = get_immediate_files(baseDir + "/" + baseDirectoryContent[0] + "/")
horizontalTilesCount = len(firstDirectoryContent)
if horizontalTilesCount == 0:
    print "Error! First tile directory is empty. Please check tile files."
    sys.exit()

try:
    tileName, tileExtension = os.path.splitext(baseDir + "/" + baseDirectoryContent[0] + "/" + firstDirectoryContent[0])
    firstTile = Image.open(tileName + tileExtension)
    tileSize = firstTile.size[0]
except:
    print "Error! An error occurred while finding first tile. Please check files in tiles directories."
    sys.exit()

image = Image.new('RGB', (tileSize * horizontalTilesCount, tileSize * verticalTilesCount))

i = 0
for dir in sorted(baseDirectoryContent, key=lambda x: int(x)):
    y = tileSize * i
    j = 0
    for file in sorted(get_immediate_files(baseDir + dir), key=lambda x: int(x.split('.')[0])):
        tilePath = baseDir + dir + "/" + file
        tile = Image.open(tilePath)
        x = tileSize * j
        image.paste(tile, (x, y))
        j += 1
    i += 1
image.save(destinationFile, "JPEG")
print "Result file is writen successfully!"