import nose
from PIL import Image
import sphinx
import simplejson
import elementtree.ElementTree as ET
from numpy import *
import flickrapi
import urllib2 as urllib
from cStringIO import StringIO


def test_nose():
	assert True == True
	print "Tested Nose: Assertion Passed"

def test_PIL():
	img_file = urllib.urlopen("http://www.ecse.rpi.edu/~agung/logo.jpg")
	im = StringIO(img_file.read())
	resized_image = Image.open(im)
	cropped_image = resized_image.crop((0,0,resized_image.size[1],resized_image.size[1]))
	cropped_image.rotate(90).show()
	print "Testing PIL: RPI logo rotated 90 degrees is shown."

def test_sphinx():
	print "Tested Sphinx: Import Successful"

def test_simplejson():
	print "Testing SimpleJSON: " + simplejson.dumps(['test', {'status': ('successful', None, 1.0, 1)}])
	
def test_elementtree():
	xml =  '<outside> \
			     <inside name="Test Successful"> \
			     </inside> \
			</outside>'

	print "Testing ElementTree: " + str(ET.fromstring(xml).find('inside').attrib)

def test_numpy():
	print "Testing Numpy: " + str(arctan2(array([0, 1]), array([1, 0])))

def test_flickr():
	api_key = '2540a052263125506d844abe96c610a5'
	flickr = flickrapi.FlickrAPI(api_key, cache=True)
	photos = flickr.photos_search(tags='rensselaer', lat='42.732387', lon='-73.683929', radius='5')
	print "Testing Flickr API: " + photos[0][0].attrib['title']

test_nose()
test_PIL()
test_sphinx()
test_simplejson()
test_elementtree()
test_numpy()
test_flickr()

