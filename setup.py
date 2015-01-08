from setuptools import setup

exec (open('djangofy/version.py').read())

setup(name='djangofy',
      version=__version__,
      author='Étienne Tétreault-Pinard',
      author_email='etienne.t.pinard@gmail.com',
      maintainer='Étienne Tétreault-Pinard',
      maintainer_email='etienne.t.pinard@gmail.com',
      url='https://github.com/etpinard/djangofy',
      description="Python package generating django-ready urls and sitemaps",
      classifiers=[
          'Programming Language :: Python :: 2.7'
      ],
      license='MIT',
      packages=['djangofy'],
      zip_safe=False
)
