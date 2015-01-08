from django.conf.urls import patterns, url

import app.views


urlpatterns = patterns(
    '',
    url("r(?P<group)/page1$>",
        app.views.template),
    url("r(?P<group)/page2$>",
        app.views.template),
    url("r(?P<group)/page3$>",
        app.views.template)
)
