# Videos2Images

Converts multiple images into images with defined fps.

# Requirements 
- python 3
- ffmpeg 4.3.1    
   > conda install -c conda-forge ffmpeg    
   >	or    
   > Download from : https://anaconda.org/conda-forge/ffmpeg

# Usage
1. Place videos to convert in 'Source' directory.

2. Run:
   > python video2img.py

 the images into as many pieces with defined output size as possible. The default size is 256x256.
To change in/out path or size of the crop, change following parameters in line 83~89.


    #init paths
    outPath = "./Output/"    
    path = "./Source/"

    #init fps
    fps = 0.1


