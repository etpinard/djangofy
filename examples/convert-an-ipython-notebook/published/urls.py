from django.conf.urls import patterns, url

import app.views


urlpatterns = patterns(
    '',
    url("r(?P<group)/ipython-notebook$>",
        app.views.template)
)
