from django.conf.urls import patterns, url

from app.views import Page


urlpatterns = patterns(
    '',
    url("some-exciting-article/$",
        Page.as_view(
            lang='IPython-Notebooks',
            notebook='page1'),
        name='page1'),
    url("another-exciting-article/$",
        Page.as_view(
            lang='IPython-Notebooks',
            notebook='page2'),
        name='page2'),
    url("you-must-read-this/$",
        Page.as_view(
            lang='IPython-Notebooks',
            notebook='page3'),
        name='page3')
)
