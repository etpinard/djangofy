"""
translate
=========


"""
import bs4 as _bs4
import re as _re

import update as _upd


# -------------------------------------------------------------------------------


def translate(nodes, astr, translator,
              method='startswith',
              cleanup=True,
              translate_href_google=False,
              add_attr=False,
              add_target_blank=False):
    """
    nodes [list of bs4.Tag]: ...
    astr [string]: ...
    translator [dict]: ...
    """

    # List node that do not have inner text (for cleanup)
    node_wo_inner_text = ['img', 'iframe']

    # Enforce argument type
    if not isinstance(astr, str):
        return
    if not isinstance(translator, dict):
        return

    for node in nodes:  # loop through nodes

        if not isinstance(node, _bs4.Tag):
            raise Exception('')

        # Cleanup if node doesn't have astr
        if not node.has_attr(astr):
            if cleanup:
                node.extract()
            continue

        # Cleanup if node doesn't have any text or children
        if all([
                cleanup,
                node.name not in node_wo_inner_text,
                not node.getText(strip=True),
                not node.findChildren()
        ]):
            node.extract()
            continue

        # Loop through and translate the node attr in question
        attr = node[astr]
        for phrase in translator.keys():
            if method == 're':
                re.sub(phrase, translator[phrase])
            elif getattr(attr, method)(phrase):
                node[astr] = attr.replace(phrase, translator[phrase])

        # Convert google redirects
        if translate_href_google:
            _translate_href_google([node])

        # Add attr(s) to node
        if add_attr and isinstance(add_attr, dict):
            _upd.add_attr(node, add_attr)

        # Add target='blank'
        if add_target_blank and isinstance(add_target_blank, str):
            _upd.add_target_blank(node, add_target_blank)


def _translate_href_google(node):
    """
    """

    google_starts = (
        'https://www.google.com/url?q=',
        'http://www.google.com/url?q='
    )
    google_end = '&'  # TODO could this be more strict?

    if not node['href']:
        raise Exception('')

    attr = node['href']

    for google_start in google_starts:
        if attr.startswith(google_starts):
            _s = attr.find(google_start) + len(google_start)
            _e = attr.find(google_end)
            attr = attr[_s:_e]
            attr = attr.replace('%3A', ':').replace('%2F', '/')

