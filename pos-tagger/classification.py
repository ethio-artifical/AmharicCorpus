# -*- coding: utf-8 -*-

import numpy
import pandas
import codecs
import re
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import Perceptron
from features_extractor import open_dict, opening
from sklearn.preprocessing import scale
from clastering import feature_selection, validate_with_mappings

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
	d = pandas.read_csv(features_test, header=None, sep=';')
	data = codecs.open(features_test, 'r', 'utf-8')

	# getting targets for evaluation
	data_target = pandas.read_csv('.\\temp\\test_ml.csv', header=None, sep=';')
	target = data_target.iloc[:, 1]

	# create arrays for applying rule based algorithm
	dictionary = open_dict()
	demonstratives = opening('.\\used_files\\demonstratives.txt')
	personal_pronouns = opening('.\\used_files\\pers_pronouns.txt')
	numerals = opening('.\\used_files\\numerals.txt')
	quest_pronouns = opening('.\\used_files\\quest_pronouns.txt')
	reflexive_pronouns = opening('.\\used_files\\refl_pronouns.txt')
	verbs = opening('.\\used_files\\verbs.txt')
	conjunctions = opening('.\\used_files\\conjunctions.txt')
	poss_pronouns = opening('.\\used_files\\possessive_pronouns.txt')
	postpositions = opening('.\\used_files\\postpositions.txt')

	i = 0
	tags = []
	for line in data:
		line_sp = line.split(';')
		word = line_sp.pop(0)
		features = d.iloc[i, 1:]
		features = scale(features)
		if word in hash_dict:
			tags.append(str(hash_dict[word]))
			yield word + '\t' + str(hash_dict[word])
		elif word in dictionary:
			if dictionary[word] == 'n':
				tags.append(6)
				yield word + '\tn'
			if dictionary[word] == 'adj':
				tags.append(0)
				yield word + '\tadj'
			if dictionary[word] == 'pron':
				tags.append(5)
				yield word + '\tpron'
			if dictionary[word] == 'v':
				tags.append(7)
				yield word + '\tv'
			if dictionary[word] == 'adv':
				tags.append(1)
				yield word + '\tadv'
			if dictionary[word] == 'prep':
				tags.append(3)
				yield word + '\tprep'
			if dictionary[word] == 'conj':
				tags.append(2)
				yield word + '\tconj'
			if dictionary[word] == 'num':
				tags.append(4)
				yield word + '\tnum'
		elif word in verbs:
			tags.append(7)
			yield word + '\tv'
		elif word in conjunctions:
			tags.append(2)
			yield word + '\tconj'
		elif word in poss_pronouns:
			tags.append(5)
			yield word + '\tpron'
		elif word in reflexive_pronouns:
			tags.append(5)
			yield word + '\tpron'
		elif word in postpositions:
			tags.append(3)
			yield word + '\tprep'
		elif word in demonstratives:
			tags.append(5)
			yield word + '\tpron'
		elif word in personal_pronouns:
			tags.append(5)
			yield word + '\tpron'
		elif word in numerals:
			tags.append(4)
			yield word + '\tnum'
		elif word in quest_pronouns:
			tags.append(5)
			yield word + '\tpron'
		elif re.search('[0-9]', word):
			tags.append(4)
			yield word + '\tnum'
		else:
			pred = perc.predict(features)
			tags.append(int(re.sub('[\[\]]', '', str(pred))))
			yield word + '\t' + re.sub('[\[\]]', '', str(pred))
		i += 1

	val_tags = validate_with_mappings(tags, target, features)

	print 'Accuracy ', accuracy_score(target, val_tags)
	print 'Precision ', precision_score(target, val_tags)
	print 'Recall ', recall_score(target, val_tags)
	print 'F1 ', f1_score(target, val_tags)


#clf = linear_train('features_training.csv', 'targets_training.csv')