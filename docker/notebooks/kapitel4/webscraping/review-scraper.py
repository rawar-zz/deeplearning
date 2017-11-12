import sys
import argparse
import requests
from lxml import html  
from lxml.etree import tostring

def read_product_ids(filename):
    pids = []
    with open(filename, "r") as f:
        try:
            for pid in f:
                pids.append(pid.strip())
        except: 
            print("could not read file "+filename)

    return pids

def scrape_data(url, pids, filename_neg, filename_pos):
    neg_f = open(filename_neg, "w")
    pos_f = open(filename_pos, "w")

    for pid in pids:
        print("scrape url "+url+pid+"...")
        r  = requests.get(url+pid)
        data = r.text
        parser = html.fromstring(data)

        XPATH_RATINGS                  = './/div[@class="g-tp-column g-tp-column--full"]'
        XPATH_RATING_RESULTS           = './/div[@class="m-rating-result"]'
        XPATH_RATING_TEXT_ELEMENT      = './/div[@class="m-tp-textblock"]'
        XPATH_RATING_TEXT              = './/div[@class="c-tp-copytext"]//text()'
        XPATH_RATING_STAR_LIST         = './/ul[@class="c-rating-stars"]'
        XPATH_RATING_STARS             = './/li[starts-with(@class, "c-rating-stars-item")]'

        all_rating_results = parser.xpath(XPATH_RATINGS)
        for ratings in all_rating_results:
            textresults = ratings.xpath(XPATH_RATING_TEXT)
            title = ''
            text = ''
            if(len(textresults) > 1):
                title = textresults[1]
                print(title)
                if(len(textresults) > 3):
                    text = textresults[3]
                    print(text)

            list_stars = ratings.xpath(XPATH_RATING_STAR_LIST)
            for stars in list_stars:
                index = 10
                rating = 0
                rating_stars = stars.xpath(XPATH_RATING_STARS)
                for rating_star in rating_stars:

                    if(rating_star.attrib['class'] == "c-rating-stars-item c-rating-stars-item--active"):
                        rating = index/2
                        if(rating >= 3):
                            print(str(rating)+" is positive")
                            pos_f.write(title+": "+text+"\n")
                        else:
                            print(str(rating)+" is negative")
                            neg_f.write(title+": "+text+"\n")

                    index = index - 1
    neg_f.close()            
    pos_f.close()


url = 'https://www.tchibo.de/ratings/'

parser = argparse.ArgumentParser(description='scrapes product reviews from tchibo.de')
parser.add_argument('-i','--input-file', help='filename for product id list', required=True)
parser.add_argument('-n','--negative', help='filename for the negativ reviews', required=True)
parser.add_argument('-p','--positive', help='filename for the positive reviews', required=True)
args = parser.parse_args()

if(args.input_file):
    filename_pids = args.input_file 

if(args.negative):
    filename_neg = args.negative

if(args.positive):
    filename_pos = args.positive

pids = read_product_ids(filename_pids)
scrape_data(url, pids, filename_neg, filename_pos)

