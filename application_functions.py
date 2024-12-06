from re import *

def pluralize_word(word):
    result = ""

    # Check if word is ending with s,x,z or is
    # ending with ah, eh, ih, oh,uh,dh,gh,kh,ph,rh,th
    # add es
    if search('[sxz]$', word) or search('[^aeioudgkprt]h$', word):
        result = sub('$', 'es', word)
    # Check if word is ending with ay,ey,iy,oy,uy
    # remove y add ies
    elif search('[aeiou]y$', word):
        result = sub('y$', 'ies', word)
    # In all the other cases
    # add s
    else:
        result = word + 's'

    return result