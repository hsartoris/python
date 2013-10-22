'''
Created on Oct 22, 2013

@author: hsartoris
'''
import parse_url

max_links = 10

if __name__ == "__main__":
    url = raw_input("Please enter a URL: ")
    links = []
    if url.startswith("http://"):
        links = parse_url.get_links(url, max_links)
    else:
        links = parse_url.get_links("http://" + url, max_links)
    
    all_links = links.copy()
    
    for link in links:
        all_links = all_links.union(parse_url.get_links(link, max_links))
    
    for link in all_links:
        print link
    print len(all_links)