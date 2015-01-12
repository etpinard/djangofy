"""
djangofy
=========


"""
TAB = "    "  # a tab in spaces

# -------------------------------------------------------------------------------


def _make_urls(group,
               path_to_output_file,
               group_name='group',
               app_name='app', 
               template_name='template'):
    """
    group [list]: 
    """

    # 
    out = (
        "from django.conf.urls import patterns, url\n\n"
        "import {app_name}.views\n\n\n"
        "urlpatterns = patterns(\n"
        "{TAB}'',\n"
    ).format(TAB=TAB, app_name=app_name)

    #
    for page in group:
        item = (
            'r(?P<{group_name})/{page}$>'
        ).format(group_name=group_name, page=page)
        out += (
            '{TAB}url("' + item + '",\n'
            '{TAB}{TAB}{app_name}'
            '.views.{template_name})'
        ).format(TAB=TAB, app_name=app_name, 
                 template_name=template_name)
        if page != group[-1]:
            out += ",\n"

    out += "\n)\n"

    with open(path_to_output_file, 'wb') as f:
        f.write(out)

def make_urls(group,
              path_to_output_file,
              app_name='app', 
              class_name='Page'):

    # 
    out = (
        "from django.conf.urls import patterns, url\n\n"
        "import {app_name}.views\n\n\n"
        "urlpatterns = patterns(\n"
        "{TAB}'',\n"
    ).format(TAB=TAB, app_name=app_name)

    #
    for page in group:

        item = 'r/{page}$'.format(page=page)

        out += (
            '{TAB}url("' + item + '",\n'
            '{TAB}{TAB}{class_name}.as_view(\n'
            '{TAB}{TAB}{TAB}lang=\'IPython-Notebooks\'\n'
            '{TAB}{TAB}{TAB}notebook=\'{page}\'),\n'
            '{TAB}{TAB}name={page}),'
        ).format(TAB=TAB, class_name=class_name, page=page)

        if page != group[-1]:
            out += ",\n"

    out += "\n)\n"

    with open(path_to_output_file, 'wb') as f:
        f.write(out)


def make_sitemaps(group,
                  path_to_output_file,
                  group_name='group',
                  app_name='app', 
                  template_name='template'):
    """
    """

    out = (
        "import os\n\n"
        "from django.conf import settings\n\n\n"
        "def items():\n"
        "{TAB}items = [\n"
    ).format(TAB=TAB)

    for page in group:

        location = "'/IPython-Notebooks/{page}'".format(page=page)
        lmfile = (
            "os.path.join(\n{TAB}{TAB}{TAB}{TAB}"
            "settings.TOP_DIR,\n{TAB}{TAB}{TAB}{TAB}"
            "'shelly',\n{TAB}{TAB}{TAB}{TAB}"
            "'templates',\n{TAB}{TAB}{TAB}{TAB}"
            "'api_docs',\n{TAB}{TAB}{TAB}{TAB}"
            "'includes',\n{TAB}{TAB}{TAB}{TAB}"
            "'ipython_notebooks',\n{TAB}{TAB}{TAB}{TAB}"
            "'{page}',\n{TAB}{TAB}{TAB}{TAB}"
            "'body.html')"
        ).format(page=page, TAB=TAB)

        out += (
            "{TAB}{TAB}dict(\n"
            "{TAB}{TAB}{TAB}location={location},\n"
            "{TAB}{TAB}{TAB}lmfile={lmfile},\n"
            "{TAB}{TAB}{TAB}priority=0.5\n"
            "{TAB}{TAB})"
        ).format(location=location, lmfile=lmfile, TAB=TAB)

        if page != group[-1]:
            out += ",\n"

    out += (
        "\n{TAB}]"
        "\n{TAB}return items"
        "\n"
    ).format(TAB=TAB)

    with open(path_to_output_file, 'wb') as f:
        f.write(out)


def make_redirects():
    # TODO
    return
