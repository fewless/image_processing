import glob
import os
from skimage.color import rgb2gray
from skimage.io import imread, imsave
from skimage.filters import threshold_otsu
from skimage import img_as_uint
import sys
from skimage import io, exposure, img_as_float, img_as_ubyte
import warnings

path = os.getcwd()
paths = './gray'
if not os.path.exists(paths):
	os.mkdir(paths)

for infile in glob.glob(path + "/*.jpg"):
	img = io.imread(infile)
	img = img_as_float(img)
	imgL = exposure.adjust_gamma(img, 2.2) 
	img_grayL = rgb2gray(imgL)
	img_gray = exposure.adjust_gamma(img_grayL, 1.0/2.2) 
	with warnings.catch_warnings():
    		warnings.simplefilter("ignore")
    		img_gray = img_as_ubyte(img_gray) 
	save_path = os.path.join(paths, os.path.basename(infile) )
	io.imsave(save_path, img_gray)

