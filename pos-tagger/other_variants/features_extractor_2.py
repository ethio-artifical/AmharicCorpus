# coding:utf-8

import codecs
import re
from texts_parse import wiki_words

# open needed filesimport codecs
import re
from texts_parse import wiki_words
w = codecs.open('features_11.csv', 'w', 'utf-8')

def opening(file_name):
	f = codecs.open(file_name, 'r', 'utf-8')
	array = [line.strip() for line in f]
	f.close()
	return array

dict = codecs.open('cleaned_dictionary.txt', 'r', 'utf-8')
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

letters = opening('amhletters.txt')
consonants = opening('consonants.txt')
vowel_o = opening('vowel_o.txt')
vowel_u = opening('vowel_u.txt')
vowel_e = opening('vowel_e.txt')
vowel_i = opening('vowel_i.txt')
vowel_a = opening('vowel_a.txt')
vowel_ae = opening('vowel_ae.txt')
vowels = list(set(letters) - set(consonants))
demonstratives = opening('demonstratives.txt')
personal_pronouns = opening('pers_pronouns.txt')
numerals = opening('numerals.txt')
quest_pronouns = opening('quest_pronouns.txt')
reflexive_pronouns = opening('refl_pronouns.txt')
verbs = opening('verbs.txt')
conjunctions = opening('conjunctions.txt')
poss_pronouns = opening('possessive_pronouns.txt')
postpositions = opening('postpositions.txt')

# material to parse

#word = raw_input('Enter a word: ').decode('utf-8')
#w.write(word + ';')

for text in wiki_words():
	# some difficulties in files
	sents = re.split(u'[.!?።፨፠\r\n\t] ', text)
	for sent in sents:
		if sent == '':
			continue
		sent = re.sub(u'(^[.፡ ]+|[.፡ ]+$)', '', sent)
		words = re.split(u'[፡ ]+', sent)
		numb_word = 1
		for word in words:
			if word[0] not in letters:
				continue
			if word[-1] in u'፣፤፥':
				w.write('1;')
			else:
				w.write('0;')
			word = re.sub(u'[-_:;\'\"\#*«»)(\]\[^$@}{.,?!%፠፡፣፤፥፧።፨፦]', '', word)
			w.write(word + ';')
			w.write(str(len(words)) + ';')
			w.write(str(len(word)) + ';')
			if numb_word == 1:
				w.write('1;')
			else:
				w.write('0;')
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

			# checking
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
				w.write('1;')
			else:
				w.write('0;')

			check_vowels(vowel_a)
			check_vowels(vowel_e)
			check_vowels(vowel_o)
			check_vowels(vowel_u)
			check_vowels(vowel_i)
			check_vowels(vowel_ae)
			check_vowels(consonants)

			def unambig(word = word, w = w):
				if word in dictionary:
					w.write(dictionary[word] + ';')

				# check auxiliary
				elif word in verbs:
					w.write('v;')

				# check conjunctions
				elif word in conjunctions:
					w.write('conj;')

				# check possessive pronouns
				elif word in poss_pronouns:
					w.write('pron;')

				# check postpositions
				elif word in postpositions:
					w.write('prep')

				# check reflexive pronoun
				elif word in reflexive_pronouns:
					w.write('pron;')

				# check demonstartives
				elif word in demonstratives:
					w.write('pron;')
				elif len(word) >= 3 and (word[:2] == u'የዚ' or word[:2] == u'በዚ' or word[:2] == u'ከዚ'):
					try_word = word[2:]
					if try_word in demonstratives:
						w.write('pron;')
					else:
						try_word = u'ይ' + word[2:]
						if try_word in demonstratives:
							w.write('pron;')
						else:
							w.write('-;')

				# check personal pronoun
				elif word in personal_pronouns:
					w.write('pron;')
				elif len(word) >= 2 and (word[0] == u'የ' or word[0] == u'ለ' or word[0] == u'በ'):
					try_word = word[1:]
					if try_word in personal_pronouns:
						w.write('pron;')
					else:
						w.write('-;')
				elif len(word) >= 3 and word[:2] == u'ስለ':
					try_word = word[2:]
					if try_word in personal_pronouns:
						w.write('pron;')
					else:
						w.write('-;')

				# check numerals
				elif word in numerals:
					w.write('num;')
				elif len(word) >= 2 and (word[-1] == u'ኛ' or word[-1] == u'ም'):
					change = [u'ህ', u'ቶ', u'ና', u'ያ', u'ባ', u'ሳ', u'ራ', u'ር', u'ኝ', u'ት', u'ድ']
					count = 0
					for i in change:
						try_word = word[:-2] + i
						if try_word in numerals:
							w.write('num;')
							count += 1
							break
					if count == 0:
						w.write('-;')
				else:
					w.write('-;')

			unambig()
			try:
				unambig(words[numb_word-2])
				unambig(words[numb_word+2])
			except:
				w.write('-;')

			w.write('\n')
			numb_word += 1

w.close()