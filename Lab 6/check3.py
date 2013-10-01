'''
modified on Sep 30, 2013

'''

'''
    Illustrates how to use flickr API to get a number of images
'''

from PIL import Image
import cStringIO
import urllib
import flickrapi

def resizeAndCrop(image):
    if image.size[0] < image.size[1]:
        image.resize((256, image.size[1] * 256 / image.size[0]))
    else:
        image.resize((image.size[0] * 256 / image.size[1], 256))
    
    image.crop((0,0,256,256))
    return image

def makeWallpaper(across, down, apicode):
    photos = getPhotos(apicode, 'geometric', across * down)
    
    output = Image.new("RGB", (across * 256, down * 256), 255)
    for i in range(0, across * down):
        output.paste(resizeAndCrop(openPhoto(photos[i])), ((i % across) * 256, (i / across) * 256))
    
    output.save('output.jpg')
    return output

def openPhoto(url):
    ''' Take a URL and open it as an image'''
    photo = urllib.urlopen(url)
    im_io = cStringIO.StringIO(photo.read())
    im = Image.open(im_io)
    return im

def getPhotos(apicode, query, num_images):
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
    
    background = makeWallpaper(int(raw_input("Enter the number of photos across: ")), int(raw_input("Enter the number of photos down: ")), apicode)
    background.show()