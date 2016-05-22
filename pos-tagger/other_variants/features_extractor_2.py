# coding:utf-8

import codecs
import re
from features_extractor import opening, open_dict, return_sent

# function: feature extraction
def feat_extract(name, text):
	# crate file for writing
	f_name = name.replace('.txt', '')
	feat_name = 'features_' + f_name + '.csv'
	w = codecs.open(feat_name, 'w', 'utf-8')

	# open needed files
	dictionary = open_dict()
	consonants = opening('.\\used_files\\consonants.txt')
	vowel_o = opening('.\\used_files\\vowel_o.txt')
	vowel_u = opening('.\\used_files\\vowel_u.txt')
	vowel_e = opening('.\\used_files\\vowel_e.txt')
	vowel_i = opening('.\\used_files\\vowel_i.txt')
	vowel_a = opening('.\\used_files\\vowel_a.txt')
	vowel_ae = opening('.\\used_files\\vowel_ae.txt')
	pronouns = opening('.\\used_files\\pronouns.txt')
	numerals = opening('.\\used_files\\numerals.txt')
	verbs = opening('.\\used_files\\verbs.txt')
	conjunctions = opening('.\\used_files\\conjunctions.txt')
	adpositions = opening('.\\used_files\\adpositions.txt')
	particles = opening('.\\used_files\\particles.txt')
	demonstratives = opening('.\\used_files\\demonstratives.txt')
	quest_pronouns = opening('.\\used_files\\quest_pronouns.txt')
	personal_pronouns = opening('.\\used_files\\pers_pronouns.txt')

	freq_dictionary ={}

	# function: create frequency dictionary
	def freq_dict(word, freq_dictionary = freq_dictionary):
		if word in freq_dictionary:
			freq_dictionary[word] += 1
		else:
			freq_dictionary[word] = 1

	words_out = []
	threshold = 0

	# get features and write in the file
	for sent in return_sent(text):
		words = re.split(u'[፡ ]+', sent)
		numb_word = 1
		for word in words:
			# outcomment when clastering
			if threshold == 11500:
				break
			# add or word in freq_dictionary when clastering
			if word == '':
				continue
			if word[-1] in u'፣፤፥':
				punct = 1
			else:
				punct = 0

			word = re.sub(u'[-_:;\'\"\#*«»)(\]\[^$@}{‘’><.,?!%፠፡፣፤፥፧።፨፦]', '', word)
			if word == '':
				continue



			'''
			if word in verbs:
				continue
			if word in conjunctions:
				continue
			if word in pronouns:
				continue
			if word in adpositions:
				continue
			if re.search('[0-9]', word):
				continue
			if word in particles:
				continue
			if word in numerals:
				continue

			if len(word) >= 3 and (word[:2] == u'የዚ' or word[:2] == u'በዚ' or word[:2] == u'ከዚ'):
				try_word = word[2:]
				if try_word in demonstratives:
					continue
				else:
					try_word = u'ይ' + word[2:]
					if try_word in demonstratives:
						continue
			if len(word) >= 2 and (word[0] == u'የ' or word[0] == u'ለ' or word[0] == u'በ'):
				try_word = word[1:]
				if try_word in personal_pronouns:
					continue
				elif len(word) >= 3 and word[:2] == u'ስለ':
					try_word = word[2:]
					if try_word in personal_pronouns:
						continue
			if len(word) >= 2 and (word[-1] == u'ኛ' or word[-1] == u'ም'):
				change = [u'ህ', u'ቶ', u'ና', u'ያ', u'ባ', u'ሳ', u'ራ', u'ር', u'ኝ', u'ት', u'ድ']
				for i in change:
					try_word = word[:-2] + i
					if try_word in numerals:
						continue
			if len(word) >= 3 and ((word[-2] == u'ኛ' and (word[-1] == u'ው' or word[-1] == u'ዋ' or word[-1] in vowel_u)) or (word[-1] == u'ም' and (word[-2] == u'ው' or word[-2] == u'ዋ' or word[-2] in vowel_u))):
				try_word = word[:-2]
				if try_word in quest_pronouns:
					continue

			'''


			w.write(word + ';')
			freq_dict(word)
			words_out.append(word)

			# check punct
			if punct == 1:
				w.write('1;')
			else:
				w.write('0;')

			# check word length
			#w.write(str(len(word)) + ';')

			# check first word
			if numb_word == 1:
				w.write('1;')
			else:
				w.write('0;')

			# check last word
			if numb_word == len(words):
				w.write('1;')
			else:
				w.write('0;')

			# needed functions
			def check(letter, word_i, w = w):
				if word_i == letter:
					w.write('1;')
				else:
					w.write('0;')

			def check_groups(group, word_i, w = w):
				if word_i in group:
					w.write('1;')
				else:
					w.write('0;')

			def check_vowels(group, w = w, word = word):
				count = 0
				for letter in word:
					if letter in group:
						count += 1
				w.write(str(count) + ';')

			def check_in(group, word = word, w = w):
				if word in group:
					w.write('1;')
				else:
					w.write('0;')


			'''
			# check numerals
			if re.search('[0-9]', word):
				w.write('1;')
			else:
				w.write('0;')

			# check auxiliary
			check_in(verbs)

			# check conjunctions
			check_in(conjunctions)

			# check pronouns
			check_in(pronouns)

			# check postpositions
			check_in(adpositions)

			# check partiles
			check_in(particles)

			# check demonstartives
			if word in demonstratives:
				w.write('1;')
			elif len(word) >= 3 and (word[:2] == u'የዚ' or word[:2] == u'በዚ' or word[:2] == u'ከዚ'):
				try_word = word[2:]
				if try_word in demonstratives:
					w.write('1;')
				else:
					try_word = u'ይ' + word[2:]
					if try_word in demonstratives:
						w.write('1;')
					else:
						w.write('0;')
			else:
				w.write('0;')

			# check personal pronoun
			if word in personal_pronouns:
				w.write('1;')
			elif len(word) >= 2 and (word[0] == u'የ' or word[0] == u'ለ' or word[0] == u'በ'):
				try_word = word[1:]
				if try_word in personal_pronouns:
					w.write('1;')
				else:
					w.write('0;')
			elif len(word) >= 3 and word[:2] == u'ስለ':
				try_word = word[2:]
				if try_word in personal_pronouns:
					w.write('1;')
				else:
					w.write('0;')
			else:
				w.write('0;')

			# check numerals
			if word in numerals:
				w.write('1;')
			elif len(word) >= 2 and (word[-1] == u'ኛ' or word[-1] == u'ም'):
				change = [u'ህ', u'ቶ', u'ና', u'ያ', u'ባ', u'ሳ', u'ራ', u'ር', u'ኝ', u'ት', u'ድ']
				count = 0
				for i in change:
					try_word = word[:-2] + i
					if try_word in numerals:
						w.write('1;')
						count = 1
						break
				if count == 0:
					w.write('0;')
			else:
				w.write('0;')

			# check question pronoun
			if word in quest_pronouns:
				w.write('1;')
			elif len(word) >= 3 and ((word[-2] == u'ኛ' and (word[-1] == u'ው' or word[-1] == u'ዋ' or word[-1] in vowel_u)) or (word[-1] == u'ም' and (word[-2] == u'ው' or word[-2] == u'ዋ' or word[-2] in vowel_u))):
				try_word = word[:-2]
				if try_word in quest_pronouns:
					w.write('1;')
				else:
					w.write('0;')
			else:
				w.write('0;')
			'''

			if len(word) >= 2:
				check(u'በ', word[0])
				check(u'ባ', word[0])
				check(u'ከ', word[0])
				check(u'ካ', word[0])
				check(u'እ', word[0])
				check(u'ለ', word[0])
				check(u'ስ', word[0])
				check(u'መ', word[0])
				check(u'የ', word[0])
				check(u'ተ', word[0])
				check(u'አ', word[0])
				check(u'ሌ', word[0])
				check(u'ች', word[0])
				check(u'ይ', word[0])
				check(u'ሲ', word[0])
				check(u'ል', word[0])
				check(u'ት', word[0])

				check(u'ች', word[-1])
				check(u'ቹ', word[-1])
				check(u'ው', word[-1])
				check(u'ዋ', word[-1])
				check(u'ቱ', word[-1])
				check(u'ኛ', word[-1])
				check(u'ም', word[-1])
				check(u'ን', word[-1])
				check(u'ኝ', word[-1])
				check(u'ህ', word[-1])
				check(u'ሽ', word[-1])
				check(u'ት', word[-1])
				check(u'ቻ', word[-1])
				check(u'ጃ', word[-1])
				check(u'ጫ', word[-1])
				check(u'ኻ', word[-1])
				check(u'ዣ', word[-1])
				check(u'ያ', word[-1])
				check(u'ዥ', word[-1])
				check(u'ጭ', word[-1])
				check(u'ጅ', word[-1])
				check(u'ኽ', word[-1])
				check(u'ይ', word[-1])
				check(u'ክ', word[-1])
				check(u'ሁ', word[-1])
				check(u'ክ', word[-1])
				check(u'ኩ', word[-1])
				check(u'ሉ', word[-1])
				check(u'ል', word[-1])
				check(u'ው', word[-1])
				check(u'ታ', word[-1])
				check(u'ማ', word[-1])
				check(u'ዊ', word[-1])
				check(u'ና', word[-1])

				check_groups(consonants, word[-1])
				check_groups(vowel_i, word[-1])
				check_groups(vowel_u, word[-1])
				check_groups(vowel_e, word[-1])
				check_groups(vowel_a, word[-1])
				check_groups(vowel_o, word[-1])
				check_groups(vowel_ae, word[-1])
			else:
				for i in range(0, 58):
					w.write('0;')

			if len(word) >= 3:
				check(u'ዮዋ', word[-2:])
				check(u'ዮው', word[-2:])
				check(u'ዎት', word[-2:])
				check(u'ነት', word[-2:])
				check(u'ቸው', word[-2:])
				check(u'ችሁ', word[-2:])
				check(u'ለሁ', word[-2:])
				check(u'ለህ', word[-2:])
				check(u'ለሽ', word[-2:])
				check(u'ለች', word[-2:])
				check(u'ለን', word[-2:])
				check(u'ችም', word[-2:])
				check(u'ውም', word[-2:])
				check(u'ንም', word[-2:])

				check(u'ስት', word[:2])
				check(u'ስን', word[:2])
				check(u'የዚ', word[:2])
				check(u'በዚ', word[:2])
				check(u'ከዚ', word[:2])
				check(u'የም', word[:2])
				check(u'ያል', word[:2])
				check(u'ሰረ', word[:2])
				check(u'ባለ', word[:2])
				check(u'በመ', word[:2])
				check(u'እየ', word[:2])
				check(u'እን', word[:2])
				check(u'ስለ', word[:2])
				check(u'ያለ', word[:2])
				check(u'በየ', word[:2])

				check_groups(vowel_a, word[-2])
				check_groups(vowel_u, word[-2])
				check_groups(vowel_o, word[-2])
				check_groups(vowel_ae, word[-2])
				check_groups(vowel_e, word[-2])
				check_groups(consonants, word[-2])

				check(u'ኛ', word[-2])
				check(u'ው', word[-2])
				check(u'ዋ', word[-2])
				check(u'ህ', word[-2])
				check(u'ሽ', word[-2])
				check(u'ሁ', word[-2])
			else:
				for i in range(0, 41):
					w.write('0;')

			if len(word) >= 4:
				check_groups(vowel_ae, word[-3])
				check_groups(vowel_o, word[-3])
				check_groups(vowel_a, word[-3])
				check_groups(consonants, word[-3])

				check(u'እንደ', word[:3])
				check(u'በስተ', word[:3])
				check(u'እስከ', word[:3])
				check(u'ከዎደ', word[:3])
				check(u'ስለም', word[:3])
				check(u'አለመ', word[:3])

				check(u'አችሀ', word[-3:])
				check(u'ችሁም', word[-3:])

				count = 0
				for i in range(0, len(word) - 1):
					if word[i] == word[i + 1]:
						w.write('1;')
						count += 1
						break
				if count == 0:
					w.write('0;')
			else:
				for i in range(0, 13):
					w.write('0;')

			if len(word) >= 5:
				check_groups(vowel_a, word[-4])
			else:
				w.write('0;')

			if u'አለሁ' in word or u'አለች' in word or u'አል' in word:
				w.write('1')
			else:
				w.write('0')
			'''
			check_vowels(vowel_a)
			check_vowels(vowel_e)
			check_vowels(vowel_o)
			check_vowels(vowel_u)
			check_vowels(vowel_i)
			check_vowels(vowel_ae)
			count = 0
			for letter in word:
				if letter in consonants:
					count += 1
			w.write(str(count))
			'''
			w.write('\n')
			numb_word += 1
			threshold += 1
	w.close()
	return feat_name, freq_dictionary, words_out