#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import html  
import json
import requests
import json,re
from dateutil import parser as dateparser
from time import sleep

def parse_reviews(url, pid):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    page = requests.get(url+pid,headers = headers)
    page_response = page.text
    parser = html.fromstring(page_response)

    XPATH_RATINGS = './/div[@class="m-tp-textblock"]//text()'
    XPATH_RATING_TEXTS = './/div[@class="c-tp-copytext"]//text()'
    XPATH_RATING_STARS = './/div[@class="c-rating-stars-item"]'

    # all rating till border_star are set. All stars after it are empty
    #XPATH_RATING_BORDER_STAR = './/div[@class="c-rating-stars-item c-rating-stars-item--active"]//text()'

    raw_ratings = parser.xpath(XPATH_RATING_TEXTS)

    #stars = parser.xpath(XPATH_RATING_STARS)
    #print stars

    #for star in stars:
    #    print star
    

    idx = 0
    title_index = 1
    text_index = 3
    block_index = 8
    ratings_dict = {}
    for rating in raw_ratings:
        try:     
            title_index = title_index + (idx * block_index)
            text_index = text_index + (idx * block_index) 
            print "\ntitle: " + raw_ratings[title_index]
            print "bewertung: "+ raw_ratings[text_index]
            key = str(pid) + "_" + str(idx)
            ratings_dict[key] = raw_ratings[title_index] + "," + raw_ratings[text_index]
            idx = idx + 1
        except IndexError:
            break
    return ratings_dict
			
def read_pid(url, pid_list):
    extracted_data = []
    for pid in pid_list:
        print "Downloading product with id ", pid
        extracted_data.append(parse_reviews(url, pid))
        sleep(5)
    f=open('data.json','w')
    json.dump(extracted_data,f,indent=2)

if __name__ == '__main__':
        tchibo_url  = 'https://www.tchibo.de/ratings/'
        pid_list = ['400098081', '400108977', '400108955', '400098065', '400098221', '400088181',
                    '400086934', '400098395', '400069099', '400096250', '400060127', '400084303',
                    '400091507', '400091507', '400074158', '400092654', '400061655', '400078540']
        
        #pid_list = ['400092476']
	read_pid(tchibo_url, pid_list)
