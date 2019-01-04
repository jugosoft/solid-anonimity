class utils(object):
    """description of class"""
    pass

def map(dictionary, substrings):
    """
        Custom mapper for proxies
    """
    proxy = False
    for elem in substrings:
        if dictionary.get(elem) is not None:
            proxy = True
    return proxy