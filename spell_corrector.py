'''
This module performs
* Spelling correction task given amharic text
*

Output Example

=====================
ነው 260338
ላይ 174891
ውስጥ 80072
እና 77266
ወደ 75254
=====================
'''


__author__ = 'yididiya.yilma@gmail.com'

from pysymspell import SymSpell, EditDistance

spellcheck = SymSpell()
print('Loading Dictionary File...')
spellcheck.load_dictionary('./data/dictionary.txt')



def lookup(phrase, distance=2):
    '''
    Accepts an Amharic exerpt of a text to correct its spelling
    @param distance - Distance of editing a word [Merges, splits, deletions, insertions]
        Default - 2
    '''
    suggestions = spellcheck.lookup_compound(phrase, 2)

    return suggestions

def calculate_distance(word, another):
    '''
    Calculates the # of additions, deletion, insertions needed to match a `word` with `another`
    '''
    edit_distance = EditDistance(word, 'damerau')
    return edit_distance.compare(another, len(word))
