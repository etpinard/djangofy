import djangofy as dfy
import os


PATH = './examples/convert-an-ipython-notebook/'
PUBLISHED = PATH + 'published/'

soup = dfy.load_soup(PATH + 'notebook.html')  # get HTML soup!

# Download image(s) from online source and translate 'src'

imgs = soup.findAll('img')

def custom_img_name(img_src, img_i):
    ext = img_src[-4:]
    return 'IMAGE-{img_i}'.format(img_i=img_i) + ext


def img_alt(img_src, img_i):
    return 'IPython Notebook - {img_i}'.format(img_i=img_i)


img_src_map = dfy.utils.wget_images(imgs, PATH + 'images',
                                    translate_src=True,
                                    custom_img_name=custom_img_name,
                                    img_alt=img_alt)

# Add target='_blank' attributes to outbound links

my_site_root = 'https://plot.ly'
anchors = soup.findAll('a')

for anchor in anchors:
    if not anchor['href'].startswith(my_site_root):
        dfy.add_attr(anchor, {'target': '_blank'})

# Add anchors inside In / Out <div>

def div_id(div):
    text = div.getText(strip=True, separator=u' ')
    if text:
        return text[:-1].replace(' ', '-').replace(u"\xa0", "-")

def a_href(div):
    _id = div_id(div)
    if _id:
        return "#" + _id

def a_class(div):
    return div['class']

def a_content(div):
    return div.getText(strip=True, separator=u' ')

divs = soup.findAll('div', {'class': 'prompt'})
dfy.insert_inside_nodes(divs, 'a',
                        node_attrs={'id': div_id},
                        tag_attrs={'href': a_href, 'class': a_class},
                        tag_content=a_content)

# Add lightbox anchors around <img>

def a_href(img):
    return img['src']

def a_data(img):
    return os.path.splitext(os.path.basename(img['src']))[0]

imgs = soup.findAll('img')
dfy.insert_around_nodes(imgs, 'a',
                        tag_attrs={'href': a_href, 'data-lightbox': a_data})

# Dump head and body in separate files

dfy.dump_soup(soup.body, PUBLISHED + 'body.html', remove_tag='body')
dfy.dump_soup(soup.head, PUBLISHED + 'head.html', remove_tag='head')

# Make url and sitemaps files

url = ['ipython-notebook']

dfy.make_urls(url, PUBLISHED + 'urls.py')
dfy.make_sitemaps(url, PUBLISHED + 'sitemaps.py')
