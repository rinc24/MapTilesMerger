from PIL import Image

baseDir = "C:/Users/Anton/Desktop/wolgadeutsche.net"
destinationFile = "C:/Users/Anton/Desktop/wolgadeutsche.net/result.jpg"
tileSize = 256
zoomLevel = 5
horizontalTilesCount = 23
verticalTilesCount = 16
tileExtension = ".jpg"


new_image = Image.new('RGB', (tileSize * (horizontalTilesCount + 1), tileSize * (verticalTilesCount + 1)))

i = 0
while i <= verticalTilesCount:
    y = tileSize * i

    j = 0
    while j <= horizontalTilesCount:
        tilePath = baseDir + "/" + str(zoomLevel) + "/" + str(i) + "/" + str(j) + tileExtension
        tile = Image.open(tilePath)

        x = tileSize * j
        new_image.paste(tile, (x, y))

        j += 1
    i += 1

new_image.save(destinationFile, "JPEG")