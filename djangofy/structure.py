"""
structure
=========


"""
TAB = "    "  # a tab in spaces

# -------------------------------------------------------------------------------


def make_urls(group,
              path_to_file,
              group_name='group',
              app_name='app', 
              template_name='template'):
    """
    group [list]: 
    """

    # 
    urls = (
        "from django.conf.urls import patterns, url\n\n"
        "import {app_name}.views\n\n\n"
        "urlpatterns = patterns(\n"
        "{TAB}'',\n"
    ).format(TAB=TAB, app_name=app_name)

    #
    for page in group:
        url = (
            'r(?P<{group_name})/{page}$>'
        ).format(group_name=group_name, page=page)
        urls += (
            '{TAB}url("'+url+'",\n'
            '{TAB}{TAB}{app_name}'
            '.views.{template_name})'
        ).format(TAB=TAB, app_name=app_name, 
                 template_name=template_name)
        if page != group[-1]:
            urls += ",\n"

    urls += "\n)\n"

    with open(path_to_file, 'wb') as f:
        f.write(urls)


def make_sitemaps(group,
                  path_to_file,
                  group_name='group',
                  app_name='app', 
                  template_name='template'):
    """
    """

    #
    urls = (
        "from django.conf.urls import patterns, url\n\n"
        "import {app_name}.views\n\n\n"
        "urlpatterns = patterns(\n"
        "{TAB}'',\n"
    ).format(TAB=TAB, app_name=app_name)

    #
    for page in group:
        url = (
            'r(?P<{group_name})/{page}$>'
        ).format(group_name=group_name, page=page)
        urls += (
            '{TAB}url("'+url+'",\n'
            '{TAB}{TAB}{app_name}'
            '.views.{template_name})'
        ).format(TAB=TAB, app_name=app_name, 
                 template_name=template_name)
        if page != group[-1]:
            urls += ",\n"

    urls += "\n)\n"

    with open(path_to_file, 'wb') as f:
        f.write(urls)


def make_redirects():
    return
