import os
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
base_url="https://apod.nasa.gov/apod/archivepix.html"
download_dir="apod_pictures"

to_visit=set((base_url,))
visited=set()

while to_visit:
	#pick a link to visit.
	current_page=to_visit.pop()
	print("Visiting: ", current_page)
	visited.add(current_page)
	
	#visit the link.
	content=urllib.request.urlopen(current_page).read()
	
	#extract any new links from that page.
	#when current_page is some link which doesnot have an href, we need to have a check "find_all("a",{"a":True})".
	for link in BeautifulSoup(content,"lxml").find_all("a",{"a":True}):
		absolute_link=urljoin(current_page,link["href"])
		if absolute_link not in visited:
			to_visit.add(absolute_link)
		else:
			print("Already visited: ", absolute_link)

	#download any images on the page if any a check "find_all("img",{"src":True})".
	for img in BeautifulSoup(content,"lxml").find_all("img",{"src":True}):
		img_href=urljoin(current_page,img["src"])
		print("Downloading image: ",img_href)
		img_name=img_href.split("/")[-1]
		urllib.request.urlretrieve(img_href,os.path.join(download_dir,img_name))		