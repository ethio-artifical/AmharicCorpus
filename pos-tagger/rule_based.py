# coding:utf-8

import codecs
import re

# function: open different files
def opening(file_name):
	f = codecs.open(file_name, 'r', 'utf-8')
	array = [line.strip() for line in f]
	f.close()
	return array

# fucnction: opend dictionary
def open_dict():
	dict = codecs.open('.\\used_files\\cleaned_dictionary.txt', 'r', 'utf-8')
	dictionary = {}
	for line in dict:
		split_line = line.split('\t')
		if len(split_line) == 2:
			dictionary[split_line[1]] = split_line[0]
		else:
			i = 1
			while i != 8:
				try:
					dictionary[split_line[i]] = split_line[0]
				except:
					pass
				i += 1
	dict.close()
	return dictionary

# function: clear words
def return_word(text, letters):
	sents = re.split(u'[.!?።፨፠\r\n\t] ', text)
	for sent in sents:
		sent = re.sub(u'(^[.፡ ]+|[.፡ ]+$)', '', sent)
		if sent == '':
			continue
		words = re.split(u'[፡ ]+', sent)
		for word in words:
			if word[0] not in letters:
				continue
			word = re.sub(u'[-_:;\'\"\#*«»)(\]\[^$@}{.,?!%፠፡፣፤፥፧።፨፦]', '', word)
			yield word

# fucntion: apply rules and get tags
def rules(text):
	# open needed files
	t = codecs.open('.\\test_data\\test_rules.csv', 'r', 'utf-8')

	dictionary = open_dict()
	letters = opening('.\\used_files\\amhletters.txt')
	consonants = opening('.\\used_files\\consonants.txt')
	vowel_o = opening('.\\used_files\\vowel_o.txt')
	vowel_u = opening('.\\used_files\\vowel_u.txt')
	vowel_e = opening('.\\used_files\\vowel_e.txt')
	vowel_i = opening('.\\used_files\\vowel_i.txt')
	vowel_a = opening('.\\used_files\\vowel_a.txt')
	vowel_ae = opening('.\\used_files\\vowel_ae.txt')
	demonstratives = opening('.\\used_files\\demonstratives.txt')
	personal_pronouns = opening('.\\used_files\\pers_pronouns.txt')
	numerals = opening('.\\used_files\\numerals.txt')
	quest_pronouns = opening('.\\used_files\\quest_pronouns.txt')
	reflexive_pronouns = opening('.\\used_files\\refl_pronouns.txt')
	verbs = opening('.\\used_files\\verbs.txt')
	conjunctions = opening('.\\used_files\\conjunctions.txt')
	poss_pronouns = opening('.\\used_files\\possessive_pronouns.txt')
	postpositions = opening('.\\used_files\\postpositions.txt')

	out = []

	# check morphological formants
	for word in return_word(text, letters):
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

		# ---VERY SIGNIFICANT---

		def check_in(group, note, word = word, part_speech_0 = part_speech_0):
			if word in group:
				part_speech_0.append(note)

		if word in dictionary:
			part_speech_0.append(dictionary[word])

		# check auxiliary
		check_in(verbs, 'v')

		# check conjunctions
		check_in(conjunctions, 'conj')

		# check possessive pronouns
		check_in(poss_pronouns, 'pron')

		# check postpositions
		check_in(postpositions, 'prep')

		# check reflexive pronoun
		check_in(reflexive_pronouns, 'pron')

		# check demonstartives
		if word in demonstratives:
			part_speech_0.append('pron')
		if len(word) >= 3 and (word[:2] == u'የዚ' or word[:2] == u'በዚ' or word[:2] == u'ከዚ'):
			try_word = word[2:]
			if try_word in demonstratives:
				part_speech_0.append('pron')
			else:
				try_word = u'ይ' + word[2:]
				if try_word in demonstratives:
					part_speech_0.append('pron')

		# check personal pronoun
		if word in personal_pronouns:
			part_speech_0.append('pron')
		if len(word) >= 2 and (word[0] == u'የ' or word[0] == u'ለ' or word[0] == u'በ'):
			try_word = word[1:]
			if try_word in personal_pronouns:
				part_speech_0.append('pron')
		if len(word) >= 3 and word[:2] == u'ስለ':
			try_word = word[2:]
			if try_word in personal_pronouns:
				part_speech_0.append('pron')

		# check numerals
		if word in numerals:
			part_speech_0.append('num')
		if len(word) >= 2 and (word[-1] == u'ኛ' or word[-1] == u'ም'):
			change = [u'ህ', u'ቶ', u'ና', u'ያ', u'ባ', u'ሳ', u'ራ', u'ር', u'ኝ', u'ት', u'ድ']
			for i in change:
				try_word = word[:-2] + i
				if try_word in numerals:
					part_speech_0.append('num')
					break

		# check question pronoun
		if word in quest_pronouns:
			part_speech_0.append('pron')
		if len(word) >= 3 and ((word[-2] == u'ኛ' and (word[-1] == u'ው' or word[-1] == u'ዋ' or word[-1] in vowel_u)) or (word[-1] == u'ም' and (word[-2] == u'ው' or word[-2] == u'ዋ' or word[-2] in vowel_u))):
			try_word = word[:-2]
			if try_word in quest_pronouns:
				part_speech_0.append('pron')

		### ambiguous

		# ---SIGNIFICANT---

		if len(word) >= 5:
			# check adverbial participle
			if word[:2] == u'እየ' and ((word[-3:] == u'ችሁም' and word[-4] in vowel_a) or (word[-2:] == u'ችም' and word[-3] in vowel_ae) or (word[-2:] == u'ንም' and word[-3] in consonants) or (word[-3] in vowel_o and word[-2:] == u'ውም')):
				part_speech_1pref.append('adv_part')
				part_speech_1suf.append('adv_part')

		if len(word) >= 4:
			# check double vowels
			for i in range(0, len(word) - 1):
				if word[i] == word[i + 1]:
					part_speech_0.append('adj')
					break

			# check object pronoun suffix
			if word[-3] in vowel_a and (word[-2:] == u'ቸው' or word[-2:] == u'ችሁ' or word[-2:] == u'ቸው' or word[-2:] == u'ችሁ'):
				part_speech_1suf.append('v')

			# check verbal past
			if word[-3:] == u'አችሀ':
				part_speech_1suf.append('v')

			# check verbal present-future form
			if (word[0] == u'እ' or word[0] == u'ች' or word[0] == u'ይ') and (word[-3] in vowel_a and (word[-2:] == u'ለሁ' or word[-2:] == u'ለህ' or word[-2:] == u'ለሽ' or word[-2:] == u'ለች' or word[-2:] == u'ለን' or word[-2:] == u'ችሁ')):
				part_speech_1suf.append('v')
				part_speech_1pref.append('v')
			elif (word[0] == u'እ' or word[0] == u'ች' or word[0] == u'ይ') and (word[-2] in vowel_a and (word[-1] == u'ሉ' or word[-1] == u'ል')):
				part_speech_1suf.append('v')

			# check infinitive
			if word[:3] == u'አለመ':
				part_speech_1pref.append('inf')

			# check analytic form
			if u'አለሁ' in word or u'አለች' in word or u'አል' in word:
				part_speech_0.append('inf')

			# check subordinate of clause
			if word[:2] == u'ስለ' or word[:3] == u'ስለም':
				part_speech_1pref.append('v')

			# check noun/adjective prefix
			if word[:2] == u'ባለ' or word[:2] == u'ሰረ':
				part_speech_1pref.append('n')
				part_speech_1pref.append('adj')

			# check adverbial participle
			if (word[-2:] == u'ችሁ' and word[-3] in vowel_a) or (word[-2] in vowel_o and word[-1] == u'ው'):
				part_speech_1suf.append('adv_part')
			elif word[:2] == u'እየ' and ((word[-2:] == u'ችሁ' and word[-3] in vowel_a) or (word[-1] == u'ች' and word[-2] in vowel_ae) or (word[-1] == u'ን' and word[-2] in consonants)):
				part_speech_1suf.append('adv_part')
				part_speech_1pref.append('adv_part')

			# check adverbial participle with negation
			if (word[-1] == u'ም' and word[-2] in vowel_e or word[-2] in vowel_a or word[-2] in vowel_o) or ((word[-2:] == u'ህም' or word[-2:] == u'ሽም' or word[-2:] == u'ሽም') and word[-3] in vowel_ae):
				part_speech_1suf.append('adv_part')
			elif word[-1] == u'ም' and (word[:2] == u'እየ' and (word[-2] == u'ሁ' or word[-2] == u'ህ' or word[-2] == u'ሽ' or word[-2] in vowel_ae or word[-2] in vowel_u)):
				part_speech_1suf.append('adv_part')
				part_speech_1pref.append('adv_part')

		# ---LESS SIGNIFIANT---

		if len(word) >= 3:
			# check a definite article
			if word[-2:] == u'ዮዋ' or word[-2:] == u'ዮው':
				part_speech_0.append('n')

			# check verbal past
			if word[-2] in consonants and (word[-1] == u'ህ' or word[-1] == u'ክ' or word[-1] == u'ሁ'or word[-1] == u'ኩ' or word[-1] == u'ሽ'):
				part_speech_2suf.append('v')
			elif word[-2] in vowel_ae and word[-1] == u'ች':
				part_speech_2suf.append('v')

			# check object pronoun suffix
			if word[-2:] == u'ዎት':
				part_speech_1suf.append('v')
			elif word[-2] in vowel_a and word[-1] == u'ት':
				part_speech_1suf.append('v')
			elif word[-1] == u'ት' and word[-2] in vowel_u:
				part_speech_1suf.append('v')

			# check verbal negation
			if word[-1] == u'ም':
				part_speech_2suf.append('v')
			if word[0] == u'አ':
				part_speech_2pref.append('v')

			# check prefix of verbal present-future stem
			if word[0] == u'እ' or word[0] == u'ች' or word[0] == u'ይ':
				part_speech_2pref.append('v')

			# check attributive form of a verb
			if word[0] == u'የ' or word[:2] == u'የም' or word[:2] == u'ያል':
				part_speech_2pref.append('adj')

			# check wish
			if (word[-1] in consonants or word[-1] in vowel_u) and (word[0] == u'ል' or word[0] == u'ይ' or word[0] == u'ት' or word[:2] == u'እን'):
				part_speech_2suf.append('v')
				part_speech_2pref.append('v')

			# check noun suffix
			if (word[-1] == u'ኛ' and (word[-2] in vowel_ae or word[-2] in consonants)) or ((word[-2:] == u'ነት' or word[-1] == u'ታ') and word[-2] in consonants):
				part_speech_2suf.append('n')

			# check adverbial participle
			if word[-1] in vowel_e or word[-1] in vowel_a or word[-1] in vowel_o or ((word[-1] == u'ህ' or word[-1] == u'ሽ' or word[-1] == u'ሽ') and word[-2] in vowel_ae):
				part_speech_2suf.append('adv_part')

			# check adverbial participle
			if word[:2] == u'በመ':
				part_speech_2pref.append('adv_part')
			elif word[:2] == u'እየ' and (word[-1] == u'ሁ' or word[-1] == u'ህ' or word[-1] == u'ሽ' or word[-1] in vowel_ae or word[-1] in vowel_u):
				part_speech_2suf.append('adv_part')
				part_speech_1suf.append('adv_part')
			elif word[:2] == u'ስት' or word[:2] == u'ስን' or word[0] == u'ሲ':
				part_speech_2pref.append('adv_part')

			# check adjective suffix
			if ((word[-1] == u'ም' or word[-1] == u'ማ' or word[-1] == u'ዊ') and word[-2] in vowel_a) or (word[-1] == u'ኛ' and (word[-2] in vowel_ae or word[-2] in consonants)):
				part_speech_2suf.append('adj')

		# ---ALMOST INSIGNIFICANT---

		if len(word) >= 2:
			# check plural for nouns
			if (word[-1] == u'ች' or word[-1] == u'ቹ') and word[-2] in vowel_o:
				part_speech_0.append('n')

			# check a definite article
			if word[-1] == u'ው' or word[-1] == u'ዋ' or word[-1] in vowel_u or word[-1] == u'ቱ':
				part_speech_1suf.append('n')

			# check possessive suffix
			if word[-1] in vowel_e or word[-1] in vowel_u or word[-1] == u'ው' or word[-1] == u'ህ' or word[-1] == u'ህ' or word[-1] == u'ዎ' or word[-1] == u'ዋ':
				part_speech_3suf.append('n')
				part_speech_3suf.append('pron')
				part_speech_3suf.append('v')

			# check possessive prefix
			if word[0] == u'የ':
				part_speech_3pref.append('n')

			# check verbal past
			if word[-1] in vowel_u:
				part_speech_3suf.append('v')
			elif word[-1] in vowel_ae:
				part_speech_3suf.append('v')

			# check accusative
			if word[-1] == u'ን':
				part_speech_3suf.append('v')

			# check prepositions
			if word[0] == u'በ' or word[0] == u'ባ' or word[0] == u'ከ' or word[0] == u'ካ' or word[0] == u'እ' or word[0] == u'ለ' or word[0] == u'ስ':
				part_speech_3pref.append('n')
				part_speech_3pref.append('pron')
				part_speech_3pref.append('v')

			# check object pronoun suffix
			if word[-1] in object_suffixes:
				part_speech_1suf.append('v')

			# check infinitive
			if word[0] == u'መ':
				part_speech_3pref.append('inf')
			elif word[-1] == u'ት':
				part_speech_3suf.append('inf')

			# check passive voice
			if word[0] == u'ተ':
				part_speech_3pref.append('v')

			# check place or instrument noun
			if word[-1] in middle_tongue_a:
				part_speech_3suf.append('n')

			# check actor noun
			if word[-1] in middle_tongue or (word[-1] in vowel_i and word[-1] not in front_tongue_i):
				part_speech_3suf.append('n')

			# check causative voice
			if word[0] == u'አ':
				part_speech_3pref.append('v')

			# check purpose of an action
			if word[0] == u'ሌ' or word[0] == u'ለ':
				part_speech_3pref.append('v')

			# check analytic form
			if ((word[-2:] == u'ለሁ' or word[-2:] == u'ለች') and word[-3] in vowel_a) or (word[-1] == u'ል' and word[-2] in vowel_a):
				part_speech_3suf.append('aux')

			# check adverb prefix
			if word[0] == u'በ' or word[0] == u'ለ' or word[:3] == u'እንደ' or word[:3] == u'በስተ' or word[:2] == u'ያለ' or word[:2] == u'በየ' or word[:3] == u'እስከ' or word[:3] == u'ከዎደ':
				part_speech_3pref.append('adv')

			# check order
			if word[-1] in consonants or word[-1] in vowel_i or word[-1] in vowel_u:
				part_speech_3pref.append('v')

		part_speech = []

		# fucntion: add intersection to part_speech
		def output(ps1, ps2, part_speech = part_speech):
			if set(ps1)&set(ps2):
				part_speech += list(set(ps1)&set(ps2))

		# make choice what tag to attribute using hierarchy
		if part_speech_0:
			part_speech += part_speech_0
		output(part_speech_1pref, part_speech_1suf)
		output(part_speech_1pref, part_speech_2suf)
		output(part_speech_1pref, part_speech_3suf)
		output(part_speech_1suf, part_speech_1pref)
		output(part_speech_1suf, part_speech_2pref)
		output(part_speech_1suf, part_speech_3pref)
		output(part_speech_2pref, part_speech_1suf)
		output(part_speech_2pref, part_speech_2suf)
		output(part_speech_2pref, part_speech_3suf)
		output(part_speech_2suf, part_speech_1pref)
		output(part_speech_2suf, part_speech_2pref)
		output(part_speech_2suf, part_speech_3pref)
		output(part_speech_3pref, part_speech_1suf)
		output(part_speech_3pref, part_speech_2suf)
		output(part_speech_3pref, part_speech_3suf)
		output(part_speech_3suf, part_speech_1pref)
		output(part_speech_3suf, part_speech_2pref)
		output(part_speech_3suf, part_speech_3pref)
		if part_speech == []:
			if part_speech_1pref or part_speech_2pref or part_speech_3pref:
				part_speech += part_speech_1pref
			if part_speech_1suf or part_speech_2suf or part_speech_3suf:
				part_speech += part_speech_1suf
		if part_speech == []:
			if part_speech_2pref or part_speech_3pref:
				part_speech += part_speech_2pref
			if part_speech_2suf or part_speech_3suf:
				part_speech += part_speech_2suf
		if part_speech == []:
			if part_speech_3pref:
				part_speech += part_speech_3pref
			if part_speech_3suf:
				part_speech += part_speech_3suf

		target = list(set(part_speech))

		# function: change tags to more universal format
		def remove_append(a, b, target = target):
			if a in target:
				target.remove(a)
				target.append(b)

		remove_append('adv_part', 'v')
		remove_append('inf', 'v')
		remove_append('aux', 'v')

		out.append(list(set(target)))

	# compare manually tagged text and authomatically tagged text
	i = 0
	ok = 0
	for line in t:
		line = line.strip()
		line_sp = line.split(';')
		if ', ' in line_sp[-1]:
			tags_test = line_sp[-1].split(', ')
			if set(tags_test) & set(out[i]):
				ok += 1
		else:
			if line_sp[-1] in out[i]:
				ok += 1
		i += 1

	#print 'Accuracy:', float(ok)/i

#rules('.\\test_data\\test_text.txt')