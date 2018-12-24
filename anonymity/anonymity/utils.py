class utils(object):
    """description of class"""
    pass

def map(string : str, substrings : list):
    """
        Custom mapper for proxies
    """
    for elem in substrings:
        if elem in string:
            return True
        return False