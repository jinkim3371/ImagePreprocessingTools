# ImageCropper v.1.0

Simple image cropper for preprocessing training data for GANs.

# Requirements 
- python 3
- ffmpeg 4.3.1    
   > conda install -c conda-forge ffmpeg    
   >	or    
   > Download from : https://anaconda.org/conda-forge/ffmpeg

# Usage
1. Place desired images for cropping to 'SourceImg' directory.

2. Run:
   > python Main.py

Running this will crop the images into as many pieces with defined output size as possible. The default size is 256x256.
To change in/out path or size of the crop, change following parameters in line 83~89.

    IC.outPath = "./Output/"
    IC.path = "./SourceImg/"

    #init_output size
    height = 256
    width = 256

