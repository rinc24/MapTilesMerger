# Tiles preparation
You can use [TileDownloader](http://sourceforge.net/projects/tiledownloader/) project for dowloading tiles from any
online map server or custom location. But it is writed in Visual Basic and contains hardcoded file extension for tiles :(

#Merge tiles

For merging map tiles into one file you may run `mergetiles.py` script with several parameters:
`python mergetiles.py -i <input directiry> -o <output file>`

For example:
`python mergetiles.py -i "C:/demo/" -o "C:/demo/result.jpg"`

After start, script will find first file in firts direcory and try to get width of image. Size of all tiles mush be equal.
Next it will find tiles by mask `baseDir/<y>/<x>.<tileExtension>`, there `y` is row number and `x` is column number, and merge them into one image.