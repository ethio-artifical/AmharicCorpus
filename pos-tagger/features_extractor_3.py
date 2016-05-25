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

def return_sent(text):
	text = re.sub(u'\t+', '', text)
	text = re.sub(u'፡፡', u'።', text)
	text = re.sub(u'([.!?።፨፠]|\r\n)', u'\\1 %%%%', text)
	sents = re.split(u'%%%%', text)
	for sent in sents:
		sent = re.sub(u'[\r\n]', '', sent)
		sent = re.sub(u'(^[.፡ ]+|[.፡ ]+$)', '', sent)
		if sent == '':
			continue
		sent = '<bos>' + sent + '<eos>'
		yield sent

# function: feature extraction
def feat_extract(name, text):
	# crate file for writing
	f_name = name.replace('.txt', '')
	feat_name = u'features_files\\' + 'features_' + f_name + '.csv'
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
	whole_words = 0
	numb_sent = 1
	for sent in return_sent(text):
		words = re.split(u'[፡  ]+', sent)
		numb_word = 1
		for actual_word in words:
			# outcomment when clastering
			if threshold == 11500:
				break
			# add or word in freq_dictionary when clastering
			if actual_word == '':
				continue
			if actual_word[-1] in u'፣፤፥':
				punct = 1
			else:
				punct = 0

			if ';' in actual_word:
				actual_word = actual_word.replace(';', '<&***&>')

			word = re.sub(u'<.+?>', '', actual_word )
			word = re.sub(u'[-_:;\'\"\#*«»)(\]\[^$@}{‘’><.,?!%፠፡፣፤፥፧።፨፦]', '', word)
			if word == '':
				continue

			actual_word = actual_word + '<numb_sent_' + str(numb_sent) + '_>' + '<numb_word_' + str(numb_word) + '_>'

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



			w.write(actual_word + ';')
			freq_dict(word)
			words_out.append(word)

			# check punct
			if punct == 1:
				w.write('1;')
			else:
				w.write('0;')

			# check word length
			w.write(str(len(word)) + ';')

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

			def check_in(group, word = word, w = w):
				if word in group:
					write('1;')
				else:
					w.write('0;')

			# check plural for nouns
			if len(word) >= 2 and ((word[-1] == u'ች' or word[-1] == u'ቹ') and word[-2] in vowel_o):
				w.write('1;')
			else:
				w.write('0;')

			# check a definite article
			if len(word) >= 2 and (word[-1] == u'ው' or word[-1] == u'ዋ' or word[-1] in vowel_u or word[-1] == u'ቱ'):
				w.write('1;')
			elif len(word) >= 3 and (word[-2:] == u'ዮዋ' or word[-2:] == u'ዮው'):
				w.write('1;')
			else:
				w.write('0;')

			# check possessive prefix
			if len(word) >= 2 and word[0] == u'የ':
				w.write('1;')
			else:
				w.write('0;')

			# check double vowels
			count = 0
			if len(word) >= 4:
				for i in range(0, len(word) - 1):
					if word[i] == word[i + 1]:
						w.write('1;')
						count += 1
						break
				if count == 0:
					w.write('0;')
			else:
				w.write('0;')

			# check possessive suffix
			if len(word) >= 4:
				if word[-1] in vowel_e or word[-1] in vowel_u or word[-1] == u'ው':
					w.write('1;')
				elif word[-1] == u'ህ' or word[-1] == u'ህ' or word[-1] == u'ዎ' or word[-1] == u'ዋ':
					w.write('1;')
				elif word[-3] in vowel_a and (word[-2:] == u'ቸው' or word[-2:] == u'ችን' or word[-2:] == u'ቸሁ'):
					w.write('1;')
				else:
					w.write('0;')
			else:
				w.write('0;')

			# check verbal past
			if len(word) >= 3 and word[-2] in consonants and (word[-1] == u'ህ' or word[-1] == u'ክ' or word[-1] == u'ሁ'or word[-1] == u'ኩ' or word[-1] == u'ሽ'):
				w.write('1;')
			elif len(word) >= 2 and word[-1] in vowel_u:
				w.write('1;')
			elif len(word) >= 2 and word[-1] in vowel_ae:
				w.write('1;')
			elif len(word) >= 3 and (word[-2] in vowel_ae and word[-1] == u'ች'):
				w.write('1;')
			elif len(word) >= 4 and word[-3:] == u'አችሀ':
				w.write('1;')
			else:
				w.write('0;')

			# check accusative
			if len(word) >= 2 and word[-1] == u'ን':
				w.write('1;')
			else:
				w.write('0;')

			# check prepositions
			if len(word) >= 2 and (word[0] == u'በ' or word[0] == u'ባ' or word[0] == u'ከ' or word[0] == u'ካ' or word[0] == u'እ' or word[0] == u'ለ' or word[0] == u'ስ'):
				w.write('1;')
			else:
				w.write('0;')

			# check object pronoun suffix
			object_suffixes = [u'ኝ', u'ህ', u'ሽ', u'ው', u'ን']
			if len(word) >=2 and word[-1] in object_suffixes:
				w.write('1;')
			elif len(word) >=3 and word[-2:] == u'ዎት':
				w.write('1;')
			elif len(word) >=3 and word[-2] in vowel_a and word[-1] == u'ት':
				w.write('1;')
			elif len(word) >=4 and word[-3] in vowel_a and (word[-2:] == u'ቸው' or word[-2:] == u'ችሁ' or word[-2:] == u'ቸው' or word[-2:] == u'ችሁ'):
				w.write('1;')
			elif len(word) >=3 and word[-1] == u'ት' and word[-2] in vowel_u:
				w.write('1;')
			else:
				w.write('0;')

			# check verbal negation
			if len(word) >= 3 and (word[-1] == u'ም' or word[0] == u'አ'):
				w.write('1;')
			else:
				w.write('0;')

			# check prefix of verbal present-future stem
			if len(word) >= 3 and (word[0] == u'እ' or word[0] == u'ች' or word[0] == u'ይ'):
				w.write('1;')
			else:
				w.write('0;')

			# check verbal present-future form
			if len(word) >= 4 and word[-3] in vowel_a and (word[-2:] == u'ለሁ' or word[-2:] == u'ለህ' or word[-2:] == u'ለሽ' or word[-2:] == u'ለች' or word[-2:] == u'ለን' or word[-2:] == u'ችሁ'):
				w.write('1;')
			elif len(word) >= 3 and word[-2] in vowel_a and (word[-1] == u'ሉ' or word[-1] == u'ል'):
				w.write('1;')
			else:
				w.write('0;')

			# check question pronoun
			if word in quest_pronouns:
				w.write('1;')
			elif len(word) >= 3  and ((word[-2] == u'ኛ' and (word[-1] == u'ው' or word[-1] == u'ዋ' or word[-1] in vowel_u)) or (word[-1] == u'ም' and (word[-2] == u'ው' or word[-2] == u'ዋ' or word[-2] in vowel_u))):
				try_word = word[:-2]
				if try_word in quest_pronouns:
					w.write('1;')
				else:
					w.write('0;')
			else:
				w.write('0;')

			# check infinitive
			if len(word) >= 2 and word[0] == u'መ':
				w.write('1;')
			elif len(word) >= 2 and word[-1] == u'ት':
				w.write('1;')
			elif len(word) >= 4 and word[:3] == u'አለመ':
				w.write('1;')
			else:
				w.write('0;')

			# check passive voice
			if len(word) >= 2 and word[0] == u'ተ':
				w.write('1;')
			else:
				w.write('0;')

			# check place or instrument noun
			middle_tongue_a = [u'ቻ', u'ጃ', u'ጫ', u'ኻ', u'ዣ', u'ኛ', u'ያ']
			if len(word) >= 2 and word[-1] in middle_tongue_a:
				w.write('1;')
			else:
				w.write('0;')

			# check actor noun
			middle_tongue = [u'ች', u'ኝ', u'ዥ', u'ጭ', u'ጅ', u'ኽ', u'ይ']
			front_tongue_i = [u'ቲ', u'ዲ', u'ጢ', u'ሲ', u'ዚ', u'ኪ', u'ሊ']
			if len(word) >= 2 and (word[-1] in middle_tongue or (word[-1] in vowel_i and word[-1] not in front_tongue_i)):
				w.write('1;')
			else:
				w.write('0;')

			# check causative voice
			if len(word) >= 2 and word[0] == u'አ':
				w.write('1;')
			else:
				w.write('0;')

			# check attributive form of a verb
			if len(word) >= 3 and (word[0] == u'የ' or word[:2] == u'የም' or word[:2] == u'ያል'):
				w.write('1;')
			else:
				w.write('0;')

			# check purpose of an action
			if len(word) >= 2 and (word[0] == u'ሌ' or word[0] == u'ለ'):
				w.write('1;')
			else:
				w.write('0;')

			# check adverbial participle
			if len(word) >= 3 and (word[-1] in vowel_e or word[-1] in vowel_a or word[-1] in vowel_o or ((word[-1] == u'ህ' or word[-1] == u'ሽ' or word[-1] == u'ሽ') and word[-2] in vowel_ae)):
				w.write('1;')
			elif len(word) >= 4 and ((word[-2:] == u'ችሁ' and word[-3] in vowel_a) or (word[-2] in vowel_o and word[-1] == u'ው')):
				w.write('1;')
			elif len(word) >= 3 and word[:2] == u'በመ':
				w.write('1;')
			elif len(word) >= 3 and (word[:2] == u'እየ' and (word[-1] == u'ሁ' or word[-1] == u'ህ' or word[-1] == u'ሽ' or word[-1] in vowel_ae or word[-1] in vowel_u)):
				w.write('1;')
			elif len(word) >= 4 and (word[:2] == u'እየ' and ((word[-2:] == u'ችሁ' and word[-3] in vowel_a) or (word[-1] == u'ች' and word[-2] in vowel_ae) or (word[-1] == u'ን' and word[-2] in consonants))):
				w.write('1;')
			elif len(word) >= 3 and (word[:2] == u'ስት' or word[:2] == u'ስን' or word[0] == u'ሲ'):
				w.write('1;')
			else:
				w.write('0;')

			if word[-1] == u'ም':
				if len(word) >= 4 and (word[-2] in vowel_e or word[-2] in vowel_a or word[-2] in vowel_o or ((word[-2] == u'ህ' or word[-2] == u'ሽ' or word[-2] == u'ሽ') and word[-3] in vowel_ae)):
					w.write('1;')
				elif len(word) >= 5 and ((word[-3:] == u'ችሁ' and word[-4] in vowel_a) or (word[-3] in vowel_o and word[-2] == u'ው')):
					w.write('1;')
				elif len(word) >= 4 and (word[:2] == u'እየ' and (word[-2] == u'ሁ' or word[-2] == u'ህ' or word[-2] == u'ሽ' or word[-2] in vowel_ae or word[-2] in vowel_u)):
					w.write('1;')
				elif len(word) >= 5 and (word[:2] == u'እየ' and ((word[-3:] == u'ችሁ' and word[-4] in vowel_a) or (word[-2] == u'ች' and word[-2] in vowel_ae) or (word[-2] == u'ን' and word[-3] in consonants))):
					w.write('1;')
				else:
					w.write('0;')
			else:
				w.write('0;')

			# check analytic form
			if u'አለሁ' in word or u'አለች' in word or u'አል' in word:
				w.write('1;')
			elif len(word) >= 4 and (((word[-2:] == u'ለሁ' or word[-2:] == u'ለች') and word[-3] in vowel_a) or (word[-1] == u'ል' and word[-2] in vowel_a)):
				w.write('1;')
			else:
				w.write('0;')

			# check order
			if len(word) >= 2 and (word[-1] in consonants or word[-1] in vowel_i or word[-1] in vowel_u):
				w.write('1;')
			else:
				w.write('0;')

			# check wish
			if len(word) >= 4 and (word[-1] in consonants or word[-1] in vowel_u) and (word[0] == u'ል' or word[0] == u'ይ' or word[0] == u'ት' or word[:2] == u'እን'):
				w.write('1;')
			else:
				w.write('0;')

			# check subordinate of clause
			if len(word) >= 3 and (word[:2] == u'ስለ' or word[:3] == u'ስለም'):
				w.write('1;')
			else:
				w.write('0;')

			# check noun suffix
			if len(word) >= 3 and ((word[-1] == u'ኛ' and (word[-2] in vowel_ae or word[-2] in consonants)) or ((word[-2:] == u'ነት' or word[-1] == u'ታ') and word[-2] in consonants)):
				w.write('1;')
			else:
				w.write('0;')

			# check noun/adjective prefix
			if len(word) >= 3 and (word[:2] == u'ባለ' or word[:2] == u'ሰረ'):
				w.write('1;')
			else:
				w.write('0;')

			# check adjective suffix
			if len(word) >= 3 and (((word[-1] == u'ም' or word[-1] == u'ማ' or word[-1] == u'ዊ') and word[-2] in vowel_a) or (word[-1] == u'ኛ' and (word[-2] in vowel_ae or word[-2] in consonants))):
				w.write('1;')
			else:
				w.write('0;')

			# check adverb prefix
			if len(word) >= 2 and (word[0] == u'በ' or word[0] == u'ለ' or word[:3] == u'እንደ' or word[:3] == u'በስተ' or word[:2] == u'ያለ' or word[:2] == u'በየ' or word[:3] == u'እስከ' or word[:3] == u'ከዎደ'):
				w.write('1')
			else:
				w.write('0')

			w.write('\n')
			numb_word += 1
			threshold += 1
		numb_sent += 1
		whole_words += numb_word
	w.close()
	return feat_name, freq_dictionary, words_out, numb_sent, whole_words



