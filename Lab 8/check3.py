'''
Created on Oct 22, 2013

@author: hsartoris
'''
import parse_url

max_links = 10
max_total_links = 100

if __name__ == "__main__":
    url = raw_input("Please enter a URL: ")
    links = []
    unvisited = []
    if url.startswith("http://"):
        unvisited.append(url)
    else:
        unvisited.append("http://" + url)
        
    all_links = set([unvisited[0]])
    
    while (len(unvisited) > 0 and len(all_links) < max_total_links):
        l = unvisited.pop(0)
        new_links = parse_url.get_links(l)
        for link in new_links:
            if link not in all_links:
                unvisited.append(link)
        all_links = all_links.union(new_links)
        print "URL: ", l
        print "Number of links returned: ", len(new_links)
        print "Number of unvisited links: ", len(unvisited)
        print "Number of total links: ", len(all_links)
        raw_input('<enter>')
    print ""