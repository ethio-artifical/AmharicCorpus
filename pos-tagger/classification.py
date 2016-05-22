# -*- coding: utf-8 -*-

import numpy
import pandas
import codecs
import re
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import Perceptron
from features_extractor import open_dict, opening
from sklearn.preprocessing import scale
from clustering import feature_selection, validate_with_mappings

def linear_train(features_train, target_train):
	data_f = pandas.read_csv(features_train, header=None, sep=';')
	features = data_f.iloc[:, 1:]
	features = scale(features)

	data_t = pandas.read_csv(target_train, header=None, sep=';')
	target = data_t.iloc[:, 1]

	perc = Perceptron(random_state=242)
	perc.fit(features, target)
	return perc

def linear_class(perc, features_test, hash_dict):
	data = codecs.open(features_test, 'r', 'utf-8')

	# getting targets for evaluation
	#data_target = pandas.read_csv('.\\test_data\\test_ml.csv', header=None, sep=';')
	#target = data_target.iloc[:, 1]

	# create arrays for applying rule based algorithm
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

	count = 0
	tags = []
	for line in data:
		e_bos = ''
		line_sp = line.split(';')
		word = line_sp.pop(0)
		line_sp[-1] = re.sub('\n', '', line_sp[-1])
		alm_df = pandas.DataFrame(line_sp)
		df = alm_df.transpose()
		features = scale(df)

		if '<bos>' in word:
			e_bos = 'bos'
		elif '<eos>' in word:
			e_bos = 'eos'

		if '<&***&>' in word:
			word = word.replace('<&***&>', ';')

		numb_sent = re.findall(u'<numb_sent_([0-9]+)_>', word)
		numb_word = re.findall(u'<numb_word_([0-9]+)_>', word)

		word = re.sub(u'<.+?>', '', word)

		punctl = re.findall(u'^[-_:;\'\"\#*«»)(\]\[^$@}{‘’><.,?!%፠፡፣፤፥፧።፨፦]', word)
		punctr = re.findall(u'[-_:;\'\"\#*«»)(\]\[^$@}{‘’><.,?!%፠፡፣፤፥፧።፨፦]$', word)
		word = re.sub(u'(^[-_:;\'\"\#*«»)(\]\[^$@}{‘’><.,?!%፠፡፣፤፥፧።፨፦]|[-_:;\'\"\#*«»)(\]\[^$@}{‘’><.,?!%፠፡፣፤፥፧።፨፦]$)', '', word)

		def for_yield(PS, numb_sent = numb_sent, numb_word = numb_word, word = word, punctl = punctl, punctr = punctr, e_bos = e_bos):
			return ''.join(numb_sent) + '\t' + ''.join(numb_word) + '\tamh\t\t' + word + '\t\t\t\t1\t\t\t\t' + PS +'\t\t' + ''.join(punctl) + '\t' + ''.join(punctr) + '\t' + e_bos

		if word in dictionary:
			if dictionary[word] == 'n':
				tags.append(6)
				string = for_yield('N')
				yield string
			if dictionary[word] == 'adj':
				tags.append(0)
				string = for_yield('ADJ')
				yield string
			if dictionary[word] == 'pron':
				tags.append(5)
				string = for_yield('PRON')
				yield string
			if dictionary[word] == 'v':
				tags.append(7)
				string = for_yield('V')
				yield string
			if dictionary[word] == 'adv':
				tags.append(1)
				string = for_yield('ADV')
				yield string
			if dictionary[word] == 'prep':
				tags.append(3)
				string = for_yield('ADL')
				yield string
			if dictionary[word] == 'conj':
				tags.append(2)
				string = for_yield('CONJ')
				yield string
			if dictionary[word] == 'num':
				tags.append(4)
				string = for_yield('NUM')
				yield string
			if dictionary[word] == 'part':
				tags.append(8)
				string = for_yield('PART')
				yield string
		elif word in verbs:
			tags.append(7)
			string = for_yield('V')
			yield string
		elif word in conjunctions:
			tags.append(2)
			string = for_yield('CONJ')
			yield string
		elif word in pronouns:
			tags.append(5)
			string = for_yield('PRON')
			yield string
		elif word in adpositions:
			tags.append(3)
			string = for_yield('ADL')
			yield string
		elif re.search('[0-9]', word):
			tags.append(4)
			string = for_yield('NUM')
			yield string
		elif word in particles:
			tags.append(8)
			string = for_yield('PART')
			yield string
		elif word in numerals:
			tags.append(4)
			string = for_yield('NUM')
			yield string
		elif len(word) >= 3 and (word[:2] == u'የዚ' or word[:2] == u'በዚ' or word[:2] == u'ከዚ') and word[2:] in demonstratives:
			tags.append(5)
			string = for_yield('PRON')
			yield string
		elif len(word) >= 3 and (word[:2] == u'የዚ' or word[:2] == u'በዚ' or word[:2] == u'ከዚ') and u'ይ' + word[2:] in demonstratives:
			tags.append(5)
			string = for_yield('PRON')
			yield string
		elif len(word) >= 2 and (word[0] == u'የ' or word[0] == u'ለ' or word[0] == u'በ') and word[1:] in personal_pronouns:
			tags.append(5)
			string = for_yield('PRON')
			yield string
		elif len(word) >= 3 and word[:2] == u'ስለ' and word[2:] in personal_pronouns:
			tags.append(5)
			string = for_yield('PRON')
			yield string
		elif len(word) >= 3 and ((word[-2] == u'ኛ' and (word[-1] == u'ው' or word[-1] == u'ዋ' or word[-1] in vowel_u)) or (word[-1] == u'ም' and (word[-2] == u'ው' or word[-2] == u'ዋ' or word[-2] in vowel_u))) and word[:-2] in quest_pronouns:
			tags.append(5)
			string = for_yield('PRON')
			yield string
		elif word in hash_dict:
			tags.append(str(hash_dict[word]))
			tag = str(hash_dict[word])
			if tag == 0:
				string = for_yield('V')
				yield string
			if tag == 1:
				string = for_yield('ADJ')
				yield string
			if tag == 2:
				string = for_yield('ADV')
				yield string
			if tag == 3:
				string = for_yield('N')
				yield string
		else:
			pred = perc.predict(features)
			tag =  int(re.sub('[\[\]]', '', str(pred)))
			tags.append(tag)
			if tag == 0:
				string = for_yield('V')
				yield string
			if tag == 1:
				string = for_yield('ADJ')
				yield string
			if tag == 2:
				string = for_yield('ADV')
				yield string
			if tag == 3:
				string = for_yield('N')
				yield string

		count += 1
	'''
	val_tags = validate_with_mappings(tags, target, features)

	print 'Accuracy ', accuracy_score(target, val_tags)
	#print 'Precision ', precision_score(target, val_tags)
	#print 'Recall ', recall_score(target, val_tags)
	print 'F1 ', f1_score(target, val_tags)
	'''