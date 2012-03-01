# Author: Nishanth Amuluru
# Description: 
#     A script that parses a browse desktops page from the website 
#     `www.simpledesktops.com`

from requests import get
from BeautifulSoup import BeautifulSoup
from PIL import Image

def get_img_links(url="http://simpledesktops.com/browse/3/"):
    """ Takes a browse url and returns a list of links of all the desktops
    listed on the webpage."""

    BASE_URL = "http://simpledesktops.com"
    links = []

    resp = get(url)
    data = resp.content
    soup = BeautifulSoup(data)

    desktops = soup.findAll("div", attrs = {"class": "desktop"})

    for d in desktops:
        h_tag = d.findAll("h2")[0]
        link_tag = h_tag.findAll("a")[0]
        links.append(BASE_URL+link_tag["href"])

    return links

def get_dl_link(img_link):
    """ Takes a desktop image link and returns the download link corresponding
    to the full size image of the desktop.
    """

    BASE_URL = "http://simpledesktops.com"

    resp = get(img_link)
    data = resp.content
    soup = BeautifulSoup(data)

    div_tag = soup.findAll("div", attrs = {"class": "desktop"})[0]
    link_tag = div_tag.findAll("a")[0]

    return BASE_URL + link_tag["href"]

def download_img(url):
    """ Takes a download link and downloads the image and saves it.
    """

    resp = get(url)
    fname = resp.url.split("/")[-1]
    img_data = resp.content

    f = open(fname, "wb")
    f.write(img_data)
    f.close()

if __name__ == "__main__":
    for l in get_img_links():
        download_img(get_dl_link(l))

