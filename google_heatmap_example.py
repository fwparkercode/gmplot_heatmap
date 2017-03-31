import csv
import gmplot
from bs4 import BeautifulSoup

def insertapikey(page_name, apikey):
    """put the google api key in a html file"""
    def putkey(page, apikey, apistring=None):
        """put the apikey in the htmltxt and return soup"""
        if not apistring:
            apistring = "https://maps.googleapis.com/maps/api/js?key=%s&libraries=visualization&sensor=true_or_false&callback=initialize"
        soup = BeautifulSoup(page, 'html.parser')
        body = soup.body
        src = apistring % (apikey) # insert apikey for %s
        insert_tag = soup.new_tag("script", src=src, async="defer")
        body.insert(-1, insert_tag) # put the new script in with new src
        return soup
    page = open(page_name, 'r').read()
    soup = putkey(page, apikey)
    new_page_text = soup.prettify() # format it
    open(page_name, 'w').write(new_page_text) # rewrite the page

apikey = "AIzaSyB1Ev_xIK4pZLB9NjYz62zedM6yVPvtXcE"



