"""
utils.shortcuts
===============


"""
import bs4 as _bs4

# -------------------------------------------------------------------------------


def _wrap_tag(wrappy, wrap_tag, wrap_attrs):
    """Wrap tag around an other
    [ref: http://stackoverflow.com/a/10192634]

    """

    _soup = _bs4.BeautifulSoup()
    _wrap_tag = _soup.new_tag(wrap_tag, **wrap_attrs)

    wrappy_contents = wrappy.replaceWith(_wrap_tag)
    _wrap_tag.append(wrappy_contents)


def _insert_tag(inserty, insert_tag,
                insert_tag_attrs, insert_tag_content,
                replace, no_empty):
    """Insert tag inside an other
    [ref: http://stackoverflow.com/a/21356230/4068492]

    """
    if no_empty and not insert_tag_content:
        return

    _soup = _bs4.BeautifulSoup()
    _insert_tag = _soup.new_tag(insert_tag, **insert_tag_attrs)

    if insert_tag_content:
        _insert_tag.string = insert_tag_content

    if replace:
        _strip_contents(inserty)

    inserty.append(_insert_tag)


def _strip_contents(tag):
    """Strip contents inside tag but keep tag
    """
    for content in tag.contents:
        if content == u'\n':  # Need this to not mess up loop
            pass
        else:
            content.extract()

# -------------------------------------------------------------------------------


def call_or_get(func_or_str, *args):
    """
    """

    if hasattr(func_or_str, '__call__'):
        return func_or_str(*args)
    elif isinstance(func_or_str, str):
        return func_or_str
    else:
        raise Exception('Positional argument 1 must be a function or a str')


def sub(string, sub_del, sub_add):
    """Str replace with support for lists
    """

    if not isinstance(sub, str):
        raise Exception('Positional argument 1 must be a str')
    msg = "Positional argument 2 and 3 must be a str or list of str"
    for sub in [sub_del, sub_add]:
        if not isinstance(sub, str):
            if isinstance(sub, list):
                for sub_i in sub:
                    if not isinstance(sub_i, str):
                        raise Exception(msg)
            else:
                raise Exception(msg)
    
    if isinstance(sub_del, str):
        sub_del = [sub_del]
    if isinstance(sub_add, str):
        sub_add = [sub_add]

    # ...
