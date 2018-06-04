#!/bin/python3
#Copyright (C) 2018 Victor Oliveira <victor.oliveira@gmx.com>
#This work is free. You can redistribute it and/or modify it under the
#terms of the Do What The Fuck You Want To Public License, Version 2,
#as published by Sam Hocevar. See the COPYING file for more details.
#!/bin/python3
#Copyright (C) 2018 Victor Oliveira <victor.oliveira@gmx.com>
#This work is free. You can redistribute it and/or modify it under the
#terms of the Do What The Fuck You Want To Public License, Version 2,
#as published by Sam Hocevar. See the COPYING file for more details.

from selenium import webdriver

#JUST A TEST FILE
URL = 'http://www14.zippyshare.com/pd/GDjSDTr2/40276/fifa-mobile-soccer-v8.1.00-mod.apk'

def Download():
    

driver = webdriver.PhantomJS()
driver.get(URL)
element = driver.find_element_by_id('dlbutton')
url_download = element.get_attribute('href')
print(url_download)
