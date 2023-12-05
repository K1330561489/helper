

def uuh_code(*args):
    ret = ""
    for arg in args:
        ret=ret+"|"+str(arg)
    return ret

def uuh_decode(arg):
    ret = str(arg)
    return ret.split('|')

