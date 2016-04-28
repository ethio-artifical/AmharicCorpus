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

pref_1 = 0
suf_1 = 0
pref_2 = 0
suf_2 = 0
pref_3 = 0
suf_3 = 0

part_speech_0 = []
part_speech_1pref = []
part_speech_1suf = []
part_speech_2pref = []
part_speech_2suf = []
part_speech_3pref = []
part_speech_3suf = []

object_suffixes = [u'ኝ', u'ህ', u'ሽ', u'ው', u'ን']
middle_tongue_a = [u'ቻ', u'ጃ', u'ጫ', u'ኻ', u'ዣ', u'ኛ', u'ያ']
middle_tongue = [u'ች', u'ኝ', u'ዥ', u'ጭ', u'ጅ', u'ኽ', u'ይ']
front_tongue_i = [u'ቲ', u'ዲ', u'ጢ', u'ሲ', u'ዚ', u'ኪ', u'ሊ']

### unambiguous

print '---VERY SIGNIFICANT---'

if word in dictionary:
	#if ' ' in dictionary[word]:
		#tags = dictionary[word].split(' ')
	print dictionary[word], 'DETECTED'
	part_speech_0.append(dictionary[word])

# check auxiliary
if word in verbs:
	print 'AUXILIARY DETECTED'
	part_speech_0.append('v')

# check conjunctions
if word in conjunctions:
	print 'CONJUNCTION DETECTED'
	part_speech_0.append('conj')
	
# check possessive pronouns
if word in poss_pronouns:
	print 'POSSESSIVE PRONOUN DETECTED'
	part_speech_0.append('pron')
	
# check postpositions
if word in postpositions:
	print 'POSTPOSITION DETECTED'
	part_speech_0.append('postp')
	
# check reflexive pronoun
if word in reflexive_pronouns:
	print 'REFLEXIVE PRONOUNS DETECTED'
	part_speech_0.append('pron')

# check demonstartives
if word in demonstratives:
	print 'DEMONSTRATIVE DETECTED'
	part_speech_0.append('pron')
if len(word) >= 3 and (word[:2] == u'የዚ' or word[:2] == u'በዚ' or word[:2] == u'ከዚ'):
	try_word = word[2:]
	if try_word in demonstratives:
		print 'DEMONSTRATIVE DETECTED'
		part_speech_0.append('pron')
	else:
		try_word = u'ይ' + word[2:]
		if try_word in demonstratives:
			print 'DEMONSTRATIVE DETECTED'
			part_speech_0.append('pron')
			
# check personal pronoun
if word in personal_pronouns:
	print 'PERSONAL PRONOUN DETECTED'
	part_speech_0.append('pron')
if len(word) >= 2 and (word[0] == u'የ' or word[0] == u'ለ' or word[0] == u'በ'):
	try_word = word[1:]
	if try_word in personal_pronouns:
		print 'PERSONAL PRONOUN DETECTED'
		part_speech_0.append('pron')
if len(word) >= 3 and word[:2] == u'ስለ':
	try_word = word[2:]
	if try_word in personal_pronouns:
		print 'PERSONAL PRONOUN DETECTED'
		part_speech_0.append('pron')

# check numerals
if word in numerals:
	print 'CARDINAL DETECTED'
	part_speech_0.append('num')
if len(word) >= 2 and (word[-1] == u'ኛ' or word[-1] == u'ም'):
	change = [u'ህ', u'ቶ', u'ና', u'ያ', u'ባ', u'ሳ', u'ራ', u'ር', u'ኝ', u'ት', u'ድ']
	for i in change:
		try_word = word[:-2] + i
		if try_word in numerals:
			print 'ORDINAL DETECTED'
			part_speech_0.append('num')
			break

# check question pronoun
if word in quest_pronouns:
	print 'QUESTION PRONOUN DETECTED'
	part_speech_0.append('pron')
if len(word) >= 3 and (word[-2] == u'ኛ' and (word[-1] == u'ው' or word[-1] == u'ዋ' or word[-1] in vowel_u)) or (word[-1] == u'ም' and (word[-2] == u'ው' or word[-2] == u'ዋ' or word[-2] in vowel_u)):
	try_word = word[:-2]
	if try_word in quest_pronouns:
		print 'QUESTION PRONOUN DETECTED'
		part_speech_0.append('pron')

### ambiguous

print '---SIGNIFICANT---'

if len(word) >= 5:
	# check adverbial participle
	if word[:2] == u'እየ' and ((word[-3:] == u'ችሁም' and word[-4] in vowel_a) or (word[-2:] == u'ችም' and word[-3] in vowel_ae) or (word[-2:] == u'ንም' and word[-3] in consonants) or (word[-3] in vowel_o and word[-2:] == u'ውም')):
		print 'ADVERBIAL PARTICIPLE DETECTED'
		part_speech_1pref.append('v')
		part_speech_1suf.append('v')

if len(word) >= 4:
	# check double vowels
	for i in range(0, len(word) - 1):
		if word[i] == word[i + 1]:
			print 'DOUBLE LETTER DETECTED'
			part_speech_0.append('adj')
			break
		# для прилагательных как множ число

	# check object pronoun suffix
	if word[-3] in vowel_a and (word[-2:] == u'ቸው' or word[-2:] == u'ችሁ' or word[-2:] == u'ቸው' or word[-2:] == u'ችሁ'):
		print 'OBJECT SUFFIX DETECTED'
		part_speech_1suf.append('v')
		# после себя может присоединять множ число (множ число покажет, что это сущ)
		# могут присоединяться к местоим, числит, сущ
	
	# check verbal past
	if word[-3:] == u'አችሀ':
		print 'VERB: 1sg or 2pl DETECTED'
		part_speech_1suf.append('v')
	
	# check verbal present-future form
	if (word[0] == u'እ' or word[0] == u'ች' or word[0] == u'ይ') and (word[-3] in vowel_a and (word[-2:] == u'ለሁ' or word[-2:] == u'ለህ' or word[-2:] == u'ለሽ' or word[-2:] == u'ለች' or word[-2:] == u'ለን' or word[-2:] == u'ችሁ')):
		print 'PRESENT-FUTURE FORM DETECTED'
		part_speech_1suf.append('v')
		part_speech_1pref.append('v')
	elif (word[0] == u'እ' or word[0] == u'ች' or word[0] == u'ይ') and (word[-2] in vowel_a and (word[-1] == u'ሉ' or word[-1] == u'ል')):
		part_speech_1suf.append('v')
		# суффикс - это вспомогательный глагол
		
	# check infinitive
	if word[:3] == u'አለመ':
		print 'INFINITIVE PREFIX WITH NEGATION DETECTED'
		part_speech_1pref.append('v')
	
	# check analytic form
	if u'አለሁ' in word or u'አለች' in word or u'አል' in word:
		print 'ANALYTIC FORM DTECTED'
		part_speech_0.append('v')
		
	# check subordinate of clause
	if word[:2] == u'ስለ' or word[:3] == u'ስለም':
		print 'CAUSE SUBORDINATE DETECTED'
		part_speech_1pref.append('v')
	
	# check noun/adjective prefix
	if word[:2] == u'ባለ' or word[:2] == u'ሰረ':
		print 'NOUN/ADJECTIVE PREFIX DETECTED'
		part_speech_1pref.append('n')
		part_speech_1pref.append('adj')
		# еще есть ቢስ который стоит перед сущ
	
	# check adverbial participle
	if (word[-2:] == u'ችሁ' and word[-3] in vowel_a) or (word[-2] in vowel_o and word[-1] == u'ው'):
		print 'ADVERBIAL PARTICIPLE 1 DETECTED'
		part_speech_1suf.append('v')
	elif word[:2] == u'እየ' and ((word[-2:] == u'ችሁ' and word[-3] in vowel_a) or (word[-1] == u'ች' and word[-2] in vowel_ae) or (word[-1] == u'ን' and word[-2] in consonants)):
		print 'ADVERBIAL PARTICIPLE 3 DETECTED'
		part_speech_1suf.append('v')
		part_speech_1pref.append('v')

	# check adverbial participle with negation
	if (word[-1] == u'ም' and word[-2] in vowel_e or word[-2] in vowel_a or word[-2] in vowel_o) or ((word[-2:] == u'ህም' or word[-2:] == u'ሽም' or word[-2:] == u'ሽም') and word[-3] in vowel_ae):
		print 'ADVERBIAL PARTICIPLE 1 DETECTED'
		part_speech_1suf.append('v')
	elif word[-1] == u'ም' and (word[:2] == u'እየ' and (word[-2] == u'ሁ' or word[-2] == u'ህ' or word[-2] == u'ሽ' or word[-2] in vowel_ae or word[-2] in vowel_u)):
		print 'ADVERBIAL PARTICIPLE 3 DETECTED'
		part_speech_1suf.append('v')
		part_speech_1pref.append('v')

print '---LESS SIGNIFIANT---'
		
if len(word) >= 3:
	# check a definite article
	if word[-2:] == u'ዮዋ' or word[-2:] == u'ዮው':
		print 'DEFINITE ARTICLE DETECTED'
		part_speech_2suf.append('n')
		
	# check verbal past
	if word[-2] in consonants and (word[-1] == u'ህ' or word[-1] == u'ክ' or word[-1] == u'ሁ'or word[-1] == u'ኩ' or word[-1] == u'ሽ'):
		print 'VERB: 2infromal or 1pl DETECTED'
		part_speech_2suf.append('v')
	elif word[-2] in vowel_ae and word[-1] == u'ች':
		print 'VERB: 3fem DETECTED'
		part_speech_2suf.append('v')
		
	# check object pronoun suffix
	if word[-2:] == u'ዎት':
		print 'OBJECT SUFFIX DETECTED'
		part_speech_2suf.append('v')
	elif word[-2] in vowel_a and word[-1] == u'ት':
		print 'OBJECT SUFFIX DETECTED'
		part_speech_2suf.append('v')
	elif word[-1] == u'ት' and word[-2] in vowel_u:
		print 'OBJECT SUFFIX DETECTED'
		part_speech_2suf.append('v')

	# check verbal negation
	if word[-1] == u'ም':
		print 'NEGATION DETECTED'
		part_speech_2suf.append('v')
	if word[0] == u'አ':
		part_speech_2pref.append('v')

	# check prefix of verbal present-future stem
	if word[0] == u'እ' or word[0] == u'ች' or word[0] == u'ይ':
		print 'PRESENT-FUTURE PREFIX DETECTED'
		part_speech_2pref.append('v')
		# обычно начинаются глаголы на согл, есть исключения, но их мало. поэтому только согласные проверяем

	# check attributive form of a verb
	if word[0] == u'የ' or word[:2] == u'የም' or word[:2] == u'ያል':
		print 'ATTRIBUTIVE FORM DETECTED'
		part_speech_2pref.append('adj')
		# причастие
		
	# check wish
	if (word[-1] in consonants or word[-1] in vowel_u) and (word[0] == u'ል' or word[0] == u'ይ' or word[0] == u'ት' or word[:2] == u'እን'):
		print 'WISH DETECTED'
		part_speech_2suf.append('v')
		part_speech_2pref.append('v')
		
	# check noun suffix
	if (word[-1] == u'ኛ' and (word[-2] in vowel_ae or word[-2] in consonants)) or ((word[-2:] == u'ነት' or word[-1] == u'ታ') and word[-2] in consonants):
		print 'NOUN ENDING DETECTED'
		part_speech_2suf.append('n')
		
	# check adverbial participle
	if word[-1] in vowel_e or word[-1] in vowel_a or word[-1] in vowel_o or ((word[-1] == u'ህ' or word[-1] == u'ሽ' or word[-1] == u'ሽ') and word[-2] in vowel_ae):
		print 'ADVERBIAL PARTICIPLE 1 DETECTED'
		part_speech_2suf.append('v')
	
	# check adverbial participle
	if word[:2] == u'በመ':
		print 'ADVERBIAL PARTICIPLE 2 DETECTED'
		part_speech_2pref.append('v')
	elif word[:2] == u'እየ' and (word[-1] == u'ሁ' or word[-1] == u'ህ' or word[-1] == u'ሽ' or word[-1] in vowel_ae or word[-1] in vowel_u):
		print 'ADVERBIAL PARTICIPLE 3 DETECTED'
		part_speech_2suf.append('v')
		part_speech_1suf.append('v')
		# второе употребляется с формой прошедшего
	elif word[:2] == u'ስት' or word[:2] == u'ስን' or word[0] == u'ሲ':
		print 'ADVERBIAL PARTICIPLE 4 DETECTED'
		part_speech_2pref.append('v')
		
	# check adjective suffix
	if ((word[-1] == u'ም' or word[-1] == u'ማ' or word[-1] == u'ዊ') and word[-2] in vowel_a) or (word[-1] == u'ኛ' and (word[-2] in vowel_ae or word[-2] in consonants)):
		print 'ADJECTIVE SUFFIX DETECTED'
		part_speech_2suf.append('v')

print '---ALMOST INSIGNIFICANT---'
	
if len(word) >= 2:
	# check plural for nouns
	if (word[-1] == u'ች' or word[-1] == u'ቹ') and word[-2] in vowel_o:
		print 'PLURAL DETECTED'
		part_speech_0.append('n')
		# для существительных, редко для прилагательных

	# check a definite article
	if word[-1] == u'ው' or word[-1] == u'ዋ' or word[-1] in vowel_u or word[-1] == u'ቱ':
		print 'DEFINITE ARTICLE DETECTED'
		part_speech_3suf.append('n')
	
	# check possessive suffix
	if word[-1] in vowel_e or word[-1] in vowel_u or word[-1] == u'ው' or word[-1] == u'ህ' or word[-1] == u'ህ' or word[-1] == u'ዎ' or word[-1] == u'ዋ':
		print 'NOUN: 1/2/3 DETECTED'
		part_speech_3suf.append('n')
		part_speech_3suf.append('pron')
		part_speech_3suf.append('v')
		
	# check possessive prefix
	if word[0] == u'የ':
		print 'POSSESSIVE PREFIX DETECTED'
		part_speech_3pref.append('n')
		# может делать относительные прилагательные
		# но будем считать, что это существительные типа "дорога города", а не "городская дорога"
		# problem: может присоединятся к целой группе в начале, то есть по факту к любому слову
		
	# check verbal past
	if word[-1] in vowel_u:
		print 'VERB: 2formal or 3formal DETECTED'
		part_speech_3suf.append('v')
	elif word[-1] in vowel_ae:
		print 'VERB: 3mask DETECTED'
		part_speech_3suf.append('v')
		
	# check accusative
	if word[-1] == u'ን':
		print 'ACCUSATIVE DETECTED'
		part_speech_3suf.append('v')
		
	# check prepositions
	if word[0] == u'በ' or word[0] == u'ባ' or word[0] == u'ከ' or word[0] == u'ካ' or word[0] == u'እ' or word[0] == u'ለ' or word[0] == u'ስ':
		print 'PREPOSITION DETECTED'
		part_speech_3pref.append('n')
		part_speech_3pref.append('pron')
		part_speech_3pref.append('v')

	# check object pronoun suffix
	if word[-1] in object_suffixes:
		print 'OBJECT SUFFIX DETECTED'
		part_speech_3suf.append('v')
	
	# check infinitive
	if word[0] == u'መ':
		print 'INFINITIVE PREFIX DETECTED'
		part_speech_3pref.append('v')
	elif word[-1] == u'ት':
		print 'INFINITIVE SUFFIX DETECTED'
		part_speech_3suf.append('v')
	
	# check passive voice
	if word[0] == u'ተ':
		print 'PASSIVE DETECTED'
		part_speech_3pref.append('v')
	
	# check place or instrument noun
	if word[-1] in middle_tongue_a:
		print 'INSTRUMENTAL OR PLACE NOUN DETECTED'
		part_speech_3suf.append('n')
	
	# check actor noun
	if word[-1] in middle_tongue or (word[-1] in vowel_i and word[-1] not in front_tongue_i):
		print 'ACTOR NOUN DETECTED'
		part_speech_3suf.append('n')
		# может иметь опред артикль, показатель залога и атрибутивный показатель, но окончания очень редкие - оставим так
	
	# check causative voice
	if word[0] == u'አ':
		print 'CAUSATIVE VOICE DETECTED'
		part_speech_3pref.append('v')
	
	# check purpose of an action
	if word[0] == u'ሌ' or word[0] == u'ለ':
		print 'PURPOSE ON A VERB DETECTED'
		part_speech_3pref.append('v')
		#вешается на глагол
	
	# check analytic form
	if ((word[-2:] == u'ለሁ' or word[-2:] == u'ለች') and word[-3] in vowel_a) or (word[-1] == u'ል' and word[-2] in vowel_a):
		print 'ANALYTIC FORM DTECTED'
		part_speech_3suf.append('v')
		# слитные объектные местоимения после суф деепр и перед вспом глаг
	
	# check adverb prefix
	if word[0] == u'በ' or word[0] == u'ለ' or word[:3] == u'እንደ' or word[:3] == u'በስተ' or word[:2] == u'ያለ' or word[:2] == u'በየ' or word[:3] == u'እስከ' or word[:3] == u'ከዎደ':
		print 'ADVERB PREFIX DETECTED'
		part_speech_3pref.append('adv')

	# check order
	if word[-1] in consonants or word[-1] in vowel_i or word[-1] in vowel_u:
		print 'ORDER DETECTED'
		part_speech_3pref.append('v')

# making choice
part_speech = []
if part_speech_0 or part_speech_1suf or part_speech_2suf or part_speech_3suf or part_speech_1pref or part_speech_2pref or part_speech_3pref:
	if part_speech_0:
		part_speech += part_speech_0
	if part_speech_1pref:
		if set(part_speech_1pref)&set(part_speech_1suf):
			part_speech += list(set(part_speech_1pref)&set(part_speech_1suf))
		if set(part_speech_1pref)&set(part_speech_2suf):
			part_speech += list(set(part_speech_1pref)&set(part_speech_2suf))
		if set(part_speech_1pref)&set(part_speech_3suf):
			part_speech += list(set(part_speech_1pref)&set(part_speech_3suf))
	if part_speech_1suf:
		if set(part_speech_1suf)&set(part_speech_1pref):
			part_speech += list(set(part_speech_1suf)&set(part_speech_1pref))
		if set(part_speech_1suf)&set(part_speech_2pref):
			part_speech += list(set(part_speech_1suf)&set(part_speech_2pref))
		if set(part_speech_1suf)&set(part_speech_3pref):
			part_speech += list(set(part_speech_1suf)&set(part_speech_3pref))
	if part_speech_2pref:
		if set(part_speech_2pref)&set(part_speech_1suf):
			part_speech += list(set(part_speech_2pref)&set(part_speech_1suf))
		if set(part_speech_2pref)&set(part_speech_2suf):
			part_speech += list(set(part_speech_2pref)&set(part_speech_2suf))
		if set(part_speech_2pref)&set(part_speech_3suf):
			part_speech += list(set(part_speech_2pref)&set(part_speech_3suf))
	if part_speech_2suf:
		if set(part_speech_2suf)&set(part_speech_1pref):
			part_speech += list(set(part_speech_2suf)&set(part_speech_1pref))
		if set(part_speech_2suf)&set(part_speech_2pref):
			part_speech += list(set(part_speech_2suf)&set(part_speech_2pref))
		if set(part_speech_2suf)&set(part_speech_3pref):
			part_speech += list(set(part_speech_2suf)&set(part_speech_3pref))
	if part_speech_3pref:
		if set(part_speech_3pref)&set(part_speech_1suf):
			part_speech += list(set(part_speech_3pref)&set(part_speech_1suf))
		if set(part_speech_3pref)&set(part_speech_2suf):
			part_speech += list(set(part_speech_3pref)&set(part_speech_2suf))
		if set(part_speech_3pref)&set(part_speech_3suf):
			part_speech += list(set(part_speech_3pref)&set(part_speech_3suf))
	if part_speech_3suf:
		if set(part_speech_3suf)&set(part_speech_1pref):
			part_speech += list(set(part_speech_3suf)&set(part_speech_1pref))
		if set(part_speech_3suf)&set(part_speech_2pref):
			part_speech += list(set(part_speech_3suf)&set(part_speech_2pref))
		if set(part_speech_3suf)&set(part_speech_3pref):
			part_speech += list(set(part_speech_3suf)&set(part_speech_3pref))
elif (part_speech_1pref and part_speech_2pref and part_speech_3pref) or (part_speech_1suf and part_speech_2suf and part_speech_3suf):
	if part_speech_1pref and part_speech_2pref and part_speech_3pref:
		part_speech += part_speech_1pref
	if part_speech_1suf and part_speech_2suf and part_speech_3suf:
		part_speech += part_speech_1suf
elif part_speech_2pref or part_speech_2suf:
	if part_speech_2pref and part_speech_3pref:
		part_speech += part_speech_2pref
	if part_speech_2suf and part_speech_3suf:
		part_speech += part_speech_2suf
else:
	if part_speech_3pref:
		part_speech += part_speech_3pref
	if part_speech_3suf:
		part_speech += part_speech_3suf
print list(set(part_speech))

