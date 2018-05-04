#!/bin/python3
#Copyright © 2018 Victor Oliveira <victor.oliveira@gmx.com>
#This work is free. You can redistribute it and/or modify it under the
#terms of the Do What The Fuck You Want To Public License, Version 2,
#as published by Sam Hocevar. See the COPYING file for more details.

from urllib import request
from urllib import parse
import re
import argparse
from html.parser import HTMLParser

BUFFER = 1024 * 8

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
    def handle_data(self, data):
        if 'dlbutton' in data:
            self.data = data

def URLConvert(url, auth_number, filename):
    str_convert = {'/v/' : '/d/',
                   'file.html' : str(auth_number)}
    for old, new in str_convert.items():
        url = url.replace(old, new)
    url += '/' + filename
    return url

args_parser = argparse.ArgumentParser()
args_parser.add_argument('url',
                         help='URL to download')
args = args_parser.parse_args()

url = args.url
if not 'zippyshare.com/v/' in url:
    print('Invalid URL')
    exit(1)

print('Starting Zippyshare Downloader...')

html_page = request.urlopen(url).read().decode()
html_parser = MyHTMLParser()
html_parser.feed(html_page)

download_link = re.findall('/d/.*;', html_parser.data)
auth_number = eval(re.findall('\(.*\)', download_link[0])[0])
filename_encoded = re.findall('"/.*"', download_link[0])[0].strip('"/')
filename = parse.unquote(filename_encoded)

url_download = URLConvert(url, auth_number, filename_encoded)
req_download = request.urlopen(url_download)
filesize = int(req_download.getheader('Content-Length'))
print('Downloading: {}'.format(filename))
print('Size: {:.2f}MB'.format(filesize / 1000 / 1000))

with open(filename, 'wb') as file:
    c = 0
    while True:
        tmp = req_download.read(BUFFER)
        if tmp:
            file.write(tmp)
            c += 1
            print('{:.1f}%'.format((c * BUFFER / filesize) * 100), end='\r')
        else:
            break
