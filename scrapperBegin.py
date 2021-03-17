import os
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
base_url="https://apod.nasa.gov/apod/archivepix.html"
download_dir="apod_pictures"
content=urllib.request.urlopen(base_url).read()
for link in BeautifulSoup(content,"lxml").find_all("a"):
	print("Following link: ",link)
	href=urljoin(base_url,link["href"])
	content=urllib.request.urlopen(href).read()
	for img in BeautifulSoup(content,"lxml").find_all("img"):
		img_href=urljoin(href,img["src"])
		print("Downloading image: ", img_href)
		img_name=img_href.split("/")[-1]
		urllib.request.urlretrieve(img_href,os.path.join(download_dir,img_name))