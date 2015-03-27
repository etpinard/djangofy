import os

from django.conf import settings


def items():
    items = [
        dict(
            location='/IPython-Notebooks/some-exciting-article',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'page1',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/IPython-Notebooks/another-exciting-article',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'page2',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/IPython-Notebooks/you-must-read-this',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'page3',
                'body.html'),
            priority=0.5
        )
    ]
    return items
