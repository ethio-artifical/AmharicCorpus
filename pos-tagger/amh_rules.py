# coding:utf-8

import codecs

word = raw_input('Enter a word: ').decode('utf-8')

# open needed files
let = codecs.open('amhletters.txt', 'r', 'utf-8')
letters = [line.strip() for line in let]
let.close()

cons = codecs.open('consonants.txt', 'r', 'utf-8')
consonants = [line.strip() for line in cons]
cons.close()

o = codecs.open('vowel_o.txt', 'r', 'utf-8')
vowel_o = [line.strip() for line in o]
o.close()

u = codecs.open('vowel_u.txt', 'r', 'utf-8')
vowel_u = [line.strip() for line in u]
u.close()

e = codecs.open('vowel_e.txt', 'r', 'utf-8')
vowel_e = [line.strip() for line in e]
e.close()

i = codecs.open('vowel_i.txt', 'r', 'utf-8')
vowel_i = [line.strip() for line in i]
i.close()

a = codecs.open('vowel_a.txt', 'r', 'utf-8')
vowel_a = [line.strip() for line in a]
a.close()

ae = codecs.open('vowel_ae.txt', 'r', 'utf-8')
vowel_ae = [line.strip() for line in ae]
ae.close()

vowels = list(set(letters) - set(consonants))

dem = codecs.open('demonstratives.txt', 'r', 'utf-8')
demonstratives = [line.strip() for line in dem]
dem.close()

p_prn = codecs.open('pers_pronouns.txt', 'r', 'utf-8')
personal_pronouns = [line.strip() for line in p_prn]
p_prn.close()

num = codecs.open('numerals.txt', 'r', 'utf-8')
numerals = [line.strip() for line in num]
num.close()

### MORPHOLOGY

# check plural for nouns
if len(word) >= 2 and (word[-1] == u'ች' or word[-1] == u'ቹ'):
    if word[-2] in vowel_o:
        print 'PLURAL DETECTED'
    # для существительных, редко для прилагательных
    # todo wights???
    # todo необязательно в конце - проследить

# check a definite article
if len(word) >= 2 and (word[-1] == u'ው' or word[-1] == u'ዋ' or word[-1] in vowel_u):
    print 'DEFINITE ARTICLE DETECTED'

# check possessive prefix
if len(word) >= 2 and word[0] == u'የ':
    print 'POSSESSIVE PREFIX DETECTED'
    # может делать относительные прилагательные
    # но будем считать, что это существительные типа "дорога города", а не "городская дорога"
    # problem: может присоединятся к целой группе в начале, то есть по факту к любому слову(((

# check double vowels
if word >= 4:
    for i in range(0, len(word) - 1):
        if word[i] == word[i + 1]:
            print 'DOUBLE LETTER DETECTED'
            break
    #  для прилагательных как множ число

# check possessive suffix
if word >= 2:
    if word[-1] in vowel_e or word[-1] in vowel_u or word[-1] == u'ው':
        print '1 or 3mask DETECTED'
    if word[-1] == u'ህ' or word[-1] == u'ህ' or word[-1] == u'ዎ' or word[-1] == u'ዋ':
        print '2 or 3fem DETECTED'
    if word[-2:] == u'ቸው' or word[-2:] == u'ችን' or word[-2:] == u'ቸሁ':
        print '3form and plural DETECTED'
    # todo мб понадобится знать про предыдущую букву (на листке)
    # после себя может присоединять множ число
    # могут присоединяться к местоим, числит, сущ

# check demonstartives
if word in demonstratives:
    print 'DEMONSTRATIVE DETECTED'
if word[:2] == u'የዚ':
    try_word = word[2:]
    if try_word in demonstratives:
        print 'DEMONSTRATIVE DETECTED'
    else:
        try_word = u'ይ' + word[2:]
        if try_word in demonstratives:
            print 'DEMONSTRATIVE DETECTED'

# check comparative
if word[0] == u'ከ' or word[0] == u'ከ':
    print 'COMPARATIVE DETECTED'
    # присоеединяется к сущ, с которым сравнивают
    # обычно стоит перед прилагательным

# check personal pronoun
if word in personal_pronouns:
    print 'PERSONAL PRONOUN DETECTED'
if word[0] == u'የ':
    try_word = word[1:]
    if try_word in personal_pronouns:
        print 'PERSONAL PRONOUN DETECTED'

# check numerals
if word in numerals:
    print 'CARDINAL DETECTED'
if word[-1] == u'ኛ' or word[-1] == u'ም':
    print 'ORDINAL DETECTED'
    # todo если есть еще такое окончание, то придется делать поиск по numerals







