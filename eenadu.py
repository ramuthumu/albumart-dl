import wget
import requests, sys, os
years = [2016,2017]
month = range(1,3)
date = range(1,3)
page = range(1,3)
for y in years:
    for m in month:
        for d in date:
            for p in page:
                url = r"https://dl.dropboxusercontent.com/u/79920565/"
                ymd_main= str(y) + '_' + str(m) + '_' + str(d) + '_main'
                url += ymd_main
                url += '/' + ymd_main + '_' + str(p) +'.pdf'
                wget.download(url)
