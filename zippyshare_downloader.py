#!/bin/python3
#victor.oliveira@gmx.com
from urllib import request
from urllib import parse
from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tag = list()
        self.attrib = list()
        self.data = list()
    def handle_starttag(self, tag, attrib):
        self.tag.append(tag)
        self.attrib.append(attrib)
    def handle_data(self, data):
        if 'dlbutton' in data:
            self.data.append(data)


url = 'https://www28.zippyshare.com/v/GefAKsEE/file.html'
html = request.urlopen(url).read().decode()
parser = MyHTMLParser()
parser.feed(html)

download_link = re.findall('/d/.*;', parser.data[0])
auth_number = eval(re.findall('\(.*\)', download_link[0])[0])
filename = re.findall('"/.*"', download_link[0])[0].strip('"/')

url_download = url.replace('/v/', '/d/').replace('file.html', str(auth_number)) + '/' + filename
