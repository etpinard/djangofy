"""
djangofy
========


"""

from io import (
    load_soup,
    dump_soup,
    load_json,
    dump_soup
)

from translate import (
    translate
)

from update import (
    add_attr,
    insert_inside_nodes,
    insert_around_nodes,
    strip_nodes,
    strip_attrs
)

from structure import (
    make_urls,
    make_sitemaps,
    make_redirects
)

# from . import (
#     translate,
#     update,
#     structure
# )

import utils 

from version import __version__
