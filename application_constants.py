from re import *

FIRST_NAME_TXT_NAME = r'text_files/baseball_first_names.txt'
LAST_NAME_TXT_NAME = r'text_files/baseball_last_names.txt'
ENGLISH_NOUNS_TXT_NAME = r'text_files/english_nouns.txt'
ENGLISH_ADJECTIVES_TXT_NAME = r'text_files/english_adjectives.txt'
CITY_NAMES_TXT_NAME = r'text_files/city_names.txt'
ENGLISH_WORDS_TXT_NAME = r'text_files/english_words.txt'
PLAYER_HEADSHOT_RESIZED_PATH = r'player_headshots_resized'
BASEBALL_POSITIONS = ['C', 'P', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'OF', 'UT']

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