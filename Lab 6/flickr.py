'''
    Illustrates how to use flickr API to get a number of images
'''

from PIL import Image
import cStringIO
import urllib
import flickrapi

def openphoto(url):
    ''' Take a URL and open it as an image'''
    photo = urllib.urlopen(url)
    im_io = cStringIO.StringIO(photo.read())
    im = Image.open(im_io)
    return im

def getphotos(apicode, query, num_images):
    ''' Return a list of URLs that have a tag that 
        matches the query code. '''
    # Form the object that will interact with the Flickr website
    flickr = flickrapi.FlickrAPI(apicode, format='etree')

    # Get each matching photo and store in a list, stopping when we
    # reach the target number of images
    photos = []
    for photo in flickr.walk(tags = query, \
                                 tag_mode = 'all',\
                                 safe_search = '0',\
                                 sort = 'interestingness-desc'):
        url = "http://farm" + photo.get('farm') + ".staticflickr.com/" + \
            photo.get('server') + "/" + photo.get('id') + "_" + \
            photo.get('secret') + ".jpg"
        print url
        photos.append(url)
        if len(photos) >= num_images:
            break

    return photos

#
#  See explanation of the use of if __name__ in three_double.py from
#  HW 3.
#
if __name__ == "__main__":
    apicode = '9ed8f638602443020d13fd0d68495f53'
    n = 4
    photo_list = getphotos(apicode, 'geometric', n)
    
    # Show the images in the photolist.  Be sure to close each image
    # before hitting return.
    for url in photo_list:
        im = openphoto(url)
        im.show()
        raw_input("Enter to continue ")
