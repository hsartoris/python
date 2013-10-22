""" This is a simple module for processing a single URL and
    returning all the links in that page as a set. Note that some 
    URLs may not be returned if they do not match the searched 
    format.  

    Author: Sibel Adali, Charles Stewart
    Usage:
         parse_url.get_links(url)
"""

# Section 1: Import commands

import urllib2 

# Section 2: Function definitions

def add_links(links, link):
    """ Simple post processing to exclude links to documents
        or relative links
  
    """
    if '#' not in link and 'mailto' not in link and \
            "../" not in link and link.startswith("http://"):
        links.add(link.strip("\n"))

def get_links(url, max_links = -1):
    """ Processes the given url, finds all links in that page
        and returns a single set of links.
    """

    try:
        f = urllib2.urlopen(url)
    except urllib2.URLError, e:
        return set([])

    file = f.read()
    links = set([])
    search_str = '<a href="'

    start_loc = 0
    while True and (max_links == -1 or len(links) < max_links):
        pos = file.find(search_str, start_loc)
        if pos == -1:
            break
        end_pos = file.find('"',pos+len(search_str))
        if end_pos == -1:
            print "invalid HTML... aborting."
            break
        else:
            add_links(links,file[pos+len(search_str):end_pos])
            start_loc = end_pos

    return links


# Section 3: Main program (optional for modules)

if __name__ == '__main__':
    print "Starting with http://www.cs.rpi.edu"
    print get_links('http://www.cs.rpi.edu')
