import djangofy as dfy
import os

PATH = 'examples/example1/'
PUBLISHED = PATH + 'published/'  # path to published files!

# Make url and sitemaps files

names = [
    'page1',
    'page2',
    'page3'
]

urls = [
    'some-exciting-article',
    'another-exciting-article',
    'you-must-read-this'
]

dfy.make_urls(names, urls, PUBLISHED + 'urls.py')
dfy.make_sitemaps(names, urls, PUBLISHED + 'sitemaps.py')
