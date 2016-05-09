# coding:utf-8

# todo lxml делаем поиск по документу и читаем файл. бьем по предложениям. а потом по пробелам

import codecs

word = raw_input('Enter a word: ').decode('utf-8')

# open needed files
dict = codecs.open('cleaned_dictionary.txt', 'r', 'utf-8')
dictionary = {}
for line in dict:
    split_line = line.split('\t')
    if len(split_line) == 2:
        dictionary[split_line[1]] = split_line[0]
    if len(split_line) == 3:
        dictionary[split_line[1]] = split_line[0]
        dictionary[split_line[2]] = split_line[0]
    if len(split_line) == 4:
        dictionary[split_line[1]] = split_line[0]
        dictionary[split_line[2]] = split_line[0]
        dictionary[split_line[3]] = split_line[0]
    if len(split_line) == 5:
        dictionary[split_line[1]] = split_line[0]
        dictionary[split_line[2]] = split_line[0]
        dictionary[split_line[3]] = split_line[0]
        dictionary[split_line[4]] = split_line[0]
    if len(split_line) == 6:
        dictionary[split_line[1]] = split_line[0]
        dictionary[split_line[2]] = split_line[0]
        dictionary[split_line[3]] = split_line[0]
        dictionary[split_line[4]] = split_line[0]
        dictionary[split_line[5]] = split_line[0]
    if len(split_line) == 7:
        dictionary[split_line[1]] = split_line[0]
        dictionary[split_line[2]] = split_line[0]
        dictionary[split_line[3]] = split_line[0]
        dictionary[split_line[4]] = split_line[0]
        dictionary[split_line[5]] = split_line[0]
        dictionary[split_line[6]] = split_line[0]
    if len(split_line) == 8:
        dictionary[split_line[1]] = split_line[0]
        dictionary[split_line[2]] = split_line[0]
        dictionary[split_line[3]] = split_line[0]
        dictionary[split_line[4]] = split_line[0]
        dictionary[split_line[5]] = split_line[0]
        dictionary[split_line[6]] = split_line[0]
        dictionary[split_line[7]] = split_line[0]
dict.close()

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

numb = codecs.open('numerals.txt', 'r', 'utf-8')
numerals = [line.strip() for line in numb]
numb.close()

q_prn = codecs.open('quest_pronouns.txt', 'r', 'utf-8')
quest_pronouns = [line.strip() for line in q_prn]
q_prn.close()

r_prn = codecs.open('refl_pronouns.txt', 'r', 'utf-8')
reflexive_pronouns = [line.strip() for line in r_prn]
r_prn.close()

vb = codecs.open('verbs.txt', 'r', 'utf-8')
verbs = [line.strip() for line in vb]
vb.close()

con = codecs.open('conjunctions.txt', 'r', 'utf-8')
conjunctions = [line.strip() for line in con]
con.close()

pos_prn = codecs.open('possessive_pronouns.txt', 'r', 'utf-8')
poss_pronouns = [line.strip() for line in pos_prn]
pos_prn.close()

post = codecs.open('postpositions.txt', 'r', 'utf-8')
postpositions = [line.strip() for line in post]
post.close()

###### MORPHOLOGY

### ambiguous

# check plural for nouns
if len(word) >= 2 and ((word[-1] == u'ች' or word[-1] == u'ቹ') and word[-2] in vowel_o):
    print 'PLURAL DETECTED'
    # для существительных, редко для прилагательных

# check a definite article
if len(word) >= 2 and (word[-1] == u'ው' or word[-1] == u'ዋ' or word[-1] in vowel_u or word[-1] == u'ቱ'):
    print 'DEFINITE ARTICLE DETECTED'
if len(word) >= 3 and (word[-2:] == u'ዮዋ' or word[-2:] == u'ዮው'):
    print 'DEFINITE ARTICLE DETECTED'

# check possessive prefix
if len(word) >= 2 and word[0] == u'የ':
    print 'POSSESSIVE PREFIX DETECTED'
    # может делать относительные прилагательные
    # но будем считать, что это существительные типа "дорога города", а не "городская дорога"
    # problem: может присоединятся к целой группе в начале, то есть по факту к любому слову

# check double vowels
if len(word) >= 4:
    for i in range(0, len(word) - 1):
        if word[i] == word[i + 1]:
            print 'DOUBLE LETTER DETECTED'
            break
    # для прилагательных как множ число

# check possessive suffix
if len(word) >= 4:
    if word[-1] in vowel_e or word[-1] in vowel_u or word[-1] == u'ው':
        print 'NOUN: 1 or 3mask DETECTED'
    if word[-1] == u'ህ' or word[-1] == u'ህ' or word[-1] == u'ዎ' or word[-1] == u'ዋ':
        print 'NOUN: 2 or 3fem DETECTED'
    if word[-3] in vowel_a and (word[-2:] == u'ቸው' or word[-2:] == u'ችን' or word[-2:] == u'ቸሁ'):
        print 'NOUN: 3formal and plural DETECTED'
    # после себя может присоединять множ число (множ число покажет, что это сущ)
    # могут присоединяться к местоим, числит, сущ

# check verbal past
if len(word) >= 3 and word[-2] in consonants and (word[-1] == u'ህ' or word[-1] == u'ክ' or word[-1] == u'ሁ'or word[-1] == u'ኩ' or word[-1] == u'ሽ'):
    print 'VERB: 2infromal or 1pl DETECTED'
if len(word) >= 2 and word[-1] in vowel_u:
    print 'VERB: 2formal or 3formal DETECTED'
if len(word) >= 2 and word[-1] in vowel_ae:
    print 'VERB: 3mask DETECTED'
if len(word) >= 3 and (word[-2] in vowel_ae and word[-1] == u'ች'):
    print 'VERB: 3fem DETECTED'
if len(word) >= 4 and word[-3:] == u'አችሀ':
    print 'VERB: 1sg or 2pl DETECTED'

# check accusative
if len(word) >= 2 and word[-1] == u'ን':
    print 'ACCUSATIVE DETECTED'

# check prepositions
if len(word) >= 2 and (word[0] == u'በ' or word[0] == u'ባ' or word[0] == u'ከ' or word[0] == u'ካ' or word[0] == u'እ' or word[0] == u'ለ' or word[0] == u'ስ'):
    print 'PREPOSITION DETECTED'

# check object pronoun suffix
object_suffixes = [u'ኝ', u'ህ', u'ሽ', u'ው', u'ን']
if len(word) >=2 and word[-1] in object_suffixes:
    print 'OBJECT SUFFIX DETECTED'
if len(word) >=3 and word[-2:] == u'ዎት':
    print 'OBJECT SUFFIX DETECTED'
if len(word) >=3 and word[-2] in vowel_a and word[-1] == u'ት':
    print 'OBJECT SUFFIX DETECTED'
if len(word) >=4 and word[-3] in vowel_a and (word[-2:] == u'ቸው' or word[-2:] == u'ችሁ' or word[-2:] == u'ቸው' or word[-2:] == u'ችሁ'):
    print 'OBJECT SUFFIX DETECTED'
if len(word) >=3 and word[-1] == u'ት' and word[-2] in vowel_u:
    print 'OBJECT SUFFIX DETECTED'

# check verbal negation
if len(word) >= 3 and (word[-1] == u'ም' or word[0] == u'አ'):
    print 'NEGATION DETECTED'

# check prefix of verbal present-future stem
if len(word) >= 3 and (word[0] == u'እ' or word[0] == u'ች' or word[0] == u'ይ'):
    print 'PRESENT-FUTURE PREFIX DETECTED'
    # обычно начинаются глаголы на согл, есть исключения, но их мало. поэтому только согласные проверяем

# check verbal present-future form
if len(word) >= 4 and word[-3] in vowel_a and (word[-2:] == u'ለሁ' or word[-2:] == u'ለህ' or word[-2:] == u'ለሽ' or word[-2:] == u'ለች' or word[-2:] == u'ለን' or word[-2:] == u'ችሁ'):
    print 'PRESENT-FUTURE FORM DETECTED'
if len(word) >= 3 and word[-2] in vowel_a and (word[-1] == u'ሉ' or word[-1] == u'ል'):
    print 'PRESENT-FUTURE FORM DETECTED'
    # суффикс - это вспомогательный глагол

# check question pronoun
if word in quest_pronouns:
    print 'QUESTION PRONOUN DETECTED'
if len(word) >= 3 and (word[-2] == u'ኛ' and (word[-1] == u'ው' or word[-1] == u'ዋ' or word[-1] in vowel_u)) or (word[-1] == u'ም' and (word[-2] == u'ው' or word[-2] == u'ዋ' or word[-2] in vowel_u)):
    try_word = word[:-2]
    if try_word in quest_pronouns:
        print 'QUESTION PRONOUN DETECTED'

# check infinitive
if len(word) >= 2 and word[0] == u'መ':
    print 'INFINITIVE PREFIX DETECTED'
if len(word) >= 2 and word[-1] == u'ት':
    print 'INFINITIVE SUFFIX DETECTED'
if len(word) >= 4 and word[:3] == u'አለመ':
    print 'INFINITIVE PREFIX WITH NEGATION DETECTED'

# check passive voice
if len(word) >= 2 and word[0] == u'ተ':
    print 'PASSIVE DETECTED'

# check place or instrument noun
middle_tongue_a = [u'ቻ', u'ጃ', u'ጫ', u'ኻ', u'ዣ', u'ኛ', u'ያ']
if len(word) >= 2 and word[-1] in middle_tongue_a:
    print 'INSTRUMENTAL OR PLACE NOUN DETECTED'

# check actor noun
middle_tongue = [u'ች', u'ኝ', u'ዥ', u'ጭ', u'ጅ', u'ኽ', u'ይ']
front_tongue_i = [u'ቲ', u'ዲ', u'ጢ', u'ሲ', u'ዚ', u'ኪ', u'ሊ']
if len(word) >= 2 and (word[-1] in middle_tongue or (word[-1] in vowel_i and word[-1] not in front_tongue_i)):
    print 'ACTOR NOUN DETECTED'
    # может иметь опред артикль, показатель залога и атрибутивный показатель, но окончания очень редкие - оставим так

# check causative voice
if len(word) >= 2 and word[0] == u'አ':
    print 'CAUSATIVE VOICE DETECTED'

# check attributive form of a verb
if len(word) >= 3 and (word[0] == u'የ' or word[:2] == u'የም' or word[:2] == u'ያል'):
    print 'ATTRIBUTIVE FORM DETECTED'
    # причастие

# check purpose of an action
if len(word) >= 2 and (word[0] == u'ሌ' or word[0] == u'ለ'):
    print 'PURPOSE ON A VERB DETECTED'
    #вешается на глагол

# check adverbial participle
if len(word) >= 3 and (word[-1] in vowel_e or word[-1] in vowel_a or word[-1] in vowel_o or ((word[-1] == u'ህ' or word[-1] == u'ሽ' or word[-1] == u'ሽ') and word[-2] in vowel_ae)):
    print 'ADVERBIAL PARTICIPLE 1 DETECTED'
if len(word) >= 4 and ((word[-2:] == u'ችሁ' and word[-3] in vowel_a) or (word[-2] in vowel_o and word[-1] == u'ው')):
    print 'ADVERBIAL PARTICIPLE 1 DETECTED'
if len(word) >= 3 and word[:2] == u'በመ':
    print 'ADVERBIAL PARTICIPLE 2 DETECTED'
if len(word) >= 3 and (word[:2] == u'እየ' and (word[-1] == u'ሁ' or word[-1] == u'ህ' or word[-1] == u'ሽ' or word[-1] in vowel_ae or word[-1] in vowel_u)):
    print 'ADVERBIAL PARTICIPLE 3 DETECTED'
    # второе употребляется с формой прошедшего
if len(word) >= 4 and (word[:2] == u'እየ' and ((word[-2:] == u'ችሁ' and word[-3] in vowel_a) or (word[-1] == u'ች' and word[-2] in vowel_ae) or (word[-1] == u'ን' and word[-2] in consonants))):
    print 'ADVERBIAL PARTICIPLE 3 DETECTED'
if len(word) >= 3 and (word[:2] == u'ስት' or word[:2] == u'ስን' or word[0] == u'ሲ'):
    print 'ADVERBIAL PARTICIPLE 4 DETECTED'

if word[-1] == u'ም':
    if len(word) >= 4 and (word[-2] in vowel_e or word[-2] in vowel_a or word[-2] in vowel_o or ((word[-2] == u'ህ' or word[-2] == u'ሽ' or word[-2] == u'ሽ') and word[-3] in vowel_ae)):
        print 'ADVERBIAL PARTICIPLE 1 DETECTED'
    if len(word) >= 5 and ((word[-3:] == u'ችሁ' and word[-4] in vowel_a) or (word[-3] in vowel_o and word[-2] == u'ው')):
        print 'ADVERBIAL PARTICIPLE 1 DETECTED'
    if len(word) >= 4 and (word[:2] == u'እየ' and (word[-2] == u'ሁ' or word[-2] == u'ህ' or word[-2] == u'ሽ' or word[-2] in vowel_ae or word[-2] in vowel_u)):
        print 'ADVERBIAL PARTICIPLE 3 DETECTED'
    if len(word) >= 5 and (word[:2] == u'እየ' and ((word[-3:] == u'ችሁ' and word[-4] in vowel_a) or (word[-2] == u'ች' and word[-2] in vowel_ae) or (word[-2] == u'ን' and word[-3] in consonants))):
        print 'ADVERBIAL PARTICIPLE 3 DETECTED'

# check analytic form
if u'አለሁ' in word or u'አለች' in word or u'አል' in word:
    print 'ANALYTIC FORM DTECTED'
if len(word) >= 4 and (((word[-2:] == u'ለሁ' or word[-2:] == u'ለች') and word[-3] in vowel_a) or (word[-1] == u'ል' and word[-2] in vowel_a)):
    print 'ANALYTIC FORM DTECTED'
    # слитные объектные местоимения после суф деепр и перед вспом глаг

# check order
if len(word) >= 2 and (word[-1] in consonants or word[-1] in vowel_i or word[-1] in vowel_u):
    print 'ORDER DETECTED'

# check wish
if len(word) >= 4 and (word[-1] in consonants or word[-1] in vowel_u) and (word[0] == u'ል' or word[0] == u'ይ' or word[0] == u'ት' or word[:2] == u'እን'):
    print 'WISH DETECTED'

# check subordinate of clause
if len(word) >= 3 and (word[:2] == u'ስለ' or word[:3] == u'ስለም'):
    print 'CAUSE SUBORDINATE DETECTED'

# check noun suffix
if len(word) >= 3 and ((word[-1] == u'ኛ' and (word[-2] in vowel_ae or word[-2] in consonants)) or ((word[-2:] == u'ነት' or word[-1] == u'ታ') and word[-2] in consonants)):
    print 'NOUN ENDING DETECTED'

# check noun/adjective prefix
if len(word) >= 3 and (word[:2] == u'ባለ' or word[:2] == u'ሰረ'):
    print 'NOUN/ADJECTIVE PREFIX DETECTED'
    # еще есть ቢስ который стоит перед сущ

# check adjective suffix
if len(word) >= 3 and (((word[-1] == u'ም' or word[-1] == u'ማ' or word[-1] == u'ዊ') and word[-2] in vowel_a) or (word[-1] == u'ኛ' and (word[-2] in vowel_ae or word[-2] in consonants))):
    print 'ADJECTIVE SUFFIX DETECTED'

# check adverb prefix
if len(word) >= 2 and (word[0] == u'በ' or word[0] == u'ለ' or word[:3] == u'እንደ' or word[:3] == u'በስተ' or word[:2] == u'ያለ' or word[:2] == u'በየ' or word[:3] == u'እስከ' or word[:3] == u'ከዎደ'):
    print 'ADVERB PREFIX DETECTED'

### unambiguous
if word in dictionary:
    #if ' ' in dictionary[word]:
        #tags = dictionary[word].split(' ')
    print dictionary[word], 'DETECTED'

# check auxiliary
if word in verbs:
    print 'AUXILIARY DETECTED'

# check conjunctions
if word in conjunctions:
    print 'CONJUNCTION DETECTED'

# check possessive pronouns
if word in poss_pronouns:
    print 'POSSESSIVE PRONOUN DETECTED'

# check postpositions
if word in postpositions:
    print 'POSTPOSITION DETECTED'

# check reflexive pronoun
if word in reflexive_pronouns:
    print 'REFLEXIVE PRONOUNS DETECTED'

# check demonstartives
if word in demonstratives:
    print 'DEMONSTRATIVE DETECTED'
if len(word) >= 3 and (word[:2] == u'የዚ' or word[:2] == u'በዚ' or word[:2] == u'ከዚ'):
    try_word = word[2:]
    if try_word in demonstratives:
        print 'DEMONSTRATIVE DETECTED'
    else:
        try_word = u'ይ' + word[2:]
        if try_word in demonstratives:
            print 'DEMONSTRATIVE DETECTED'

# check personal pronoun
if word in personal_pronouns:
    print 'PERSONAL PRONOUN DETECTED'
if len(word) >= 2 and (word[0] == u'የ' or word[0] == u'ለ' or word[0] == u'በ'):
    try_word = word[1:]
    if try_word in personal_pronouns:
        print 'PERSONAL PRONOUN DETECTED'
if len(word) >= 3 and word[:2] == u'ስለ':
    try_word = word[2:]
    if try_word in personal_pronouns:
        print 'PERSONAL PRONOUN DETECTED'

# check numerals
if word in numerals:
    print 'CARDINAL DETECTED'
if len(word) >= 2 and (word[-1] == u'ኛ' or word[-1] == u'ም'):
    change = [u'ህ', u'ቶ', u'ና', u'ያ', u'ባ', u'ሳ', u'ራ', u'ር', u'ኝ', u'ት', u'ድ']
    for i in change:
        try_word = word[:-2] + i
        if try_word in numerals:
            print 'ORDINAL DETECTED'
            break