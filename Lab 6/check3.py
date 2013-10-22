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

def resizeAndCrop(image, sideLength):
    if image.size[0] < image.size[1]:
        image = image.resize((sideLength, image.size[1] * sideLength / image.size[0]))
    else:
        image = image.resize((image.size[0] * sideLength / image.size[1], sideLength))
    
    image.crop((0,0,sideLength,sideLength))
    return image

def makeWallpaper(across, down, apicode, sideLength):
    photos = getPhotos(apicode, 'geometric', across * down)
    
    output = Image.new("RGB", (across * sideLength, down * sideLength), 'white')
    for i in range(0, across * down):
        output.paste(resizeAndCrop(openPhoto(photos[i]), sideLength), ((i % across) * sideLength, (i / across) * sideLength))
    
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
                                 #safe_search = '1',\
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
    
    background = makeWallpaper(int(raw_input("Enter the number of photos across: ")), int(raw_input("Enter the number of photos down: ")), apicode, 512)
    background.show()
