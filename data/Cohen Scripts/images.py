# core
from core import environConfig

# third party libs
from svglib.svglib import svg2rlg
from reportlab.platypus import Image as platImage
from reportlab.lib import utils
from reportlab.lib.units import cm
from PIL import Image
# python core
import os
import sys
from datetime import datetime
from io import BytesIO

def img_buffer_to_svg(figure):
	with BytesIO() as figure_buffer:
		figure.savefig(figure_buffer, format='svg')
		figure_buffer.seek(0)	
		image = svg2rlg(figure_buffer)
	return image

def resize_img_aspect(img_buffer: BytesIO, width=1*cm, img_mode='RGB', size= (900, 900)) -> platImage:
	img = Image.frombytes(img_mode, size, img_buffer.getvalue())
	iw, ih = img.size
	aspect = ih / float(iw)
	return platImage(img_buffer, width=width, height=(width * aspect))
