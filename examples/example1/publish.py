import djangofy as dfy
import os

PUBLISHED = './published/'  # path to published files!

# Make url and sitemaps files

urls = [
    'page1',
    'page2',
    'page3'
]

dfy.make_urls(urls, PUBLISHED + 'urls.py')
dfy.make_sitemaps(urls, PUBLISHED + 'sitemaps.py')
