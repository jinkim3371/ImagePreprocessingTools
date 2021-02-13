# Author: JaydenK

import cv2
import os
import numpy as np

class ImageCropper:
    def __init__(self, imgTag = 0, resize = False, scale = 1):
        self.imgTag = imgTag
        self.resize = resize
        self.scale = scale
        self.outPath = "./Output/"
        self.path = "./SourceImg/"

    def imageDimensions(self, image):
        """ This function takes your input image and returns its array shape.
        Parameters
        ----------
        image : numpy.ndarray
            A numpy array of three dimensions (HxWxD) and type np.uint8
        Returns
        ----------
        tuple:  tuple of numpy integers of type np.int
            the tuple returns the shape of the image ordered as  (rows, columns, channels)
        """

        return image.shape

    def crop(self, image, height, width, start_point = (0,0)):
        """ This function takes your input image and returs cropped image
        Parameters
        ----------
        image : numpy.ndarray
            A numpy array of three dimensions (HxWxD) and type np.uint8
         height, width : int
            Desired dimension of the image after crop
        start_point : tuple
            Coordiation of starting pixel
        Returns
        ----------
        image : numpy.ndarray
                A numpy array of three dimensions (height x width xD) and type np.uint8
        """
        image_cropped = image[start_point[0]:start_point[0]+height, start_point[1]:start_point[1]+width]
        return image_cropped

    def striding_crop(self, image, height, width ):
        """ This function strides over the input image and crops to the
            specified image dimension as many times as possible, and save the images
              Parameters
        ----------
        image : numpy.ndarray
            A numpy array of three dimensions (HxWxD) and type np.uint8
         height, width : int
            Desired dimension of the image after crop
        start_point : tuple
            Coordiation of starting pixel
        Returns
        ---------
            None
        """
        dims = self.imageDimensions(image)

        if self.resize :
            # dim = (int(dims[0] * self.scale), int(dims[1]  * self.scale))
            image = cv2.resize(image, None, fx = self.scale, fy=self.scale)
            dims = self.imageDimensions(image)

        num_H = int(dims[0] / height)
        num_W = int(dims[1] / width)

        for i in range(0,num_H):
            for j in range(0,num_W):
                cropped_img = self.crop(image,height,width, (i*height,j*width))
                cv2.imwrite(self.outPath +  str(self.imgTag) + ".png", cropped_img)  # save image
                self.imgTag += 1


if __name__ == "__main__":

    #init ImageCropper class
    IC = ImageCropper(resize = True, scale=0.6)
    IC.outPath = "./Output/"
    IC.path = "./SourceImg/"
    path = IC.path

    #init_output size
    height = 256
    width = 256

    # iterate through the names of contents of the folder
    for i, image_path in enumerate(os.listdir(path)):
        input_path = os.path.join(path, image_path)
        image = cv2.imread(input_path)
        IC.striding_crop(image, height , width)
        print ("Complete: ", round(i/len(os.listdir(path))*100,2), " %", end="\r")
        if i == len(os.listdir(path))-1:
            print("Complete: 100.0 %")

    print(" -- Process Completed --")

    pass
