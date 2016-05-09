# coding: utf-8

import pandas
import codecs
import re
import itertools
import time
from rule_based import opening, return_word, open_dict
from clastering import Aglomerative_cl
from features_extractor import feat_extract
from sklearn.cluster import KMeans, MiniBatchKMeans, AgglomerativeClustering
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.feature_selection import VarianceThreshold

def rule_ml(text, feat_name, m, n):
	# apply machine learning algorithm
	# feat_name -- the name of csv-file of features
	tags, words = Aglomerative_cl(feat_name, m, n)

	# create arrays for applying rule based algorithm
	dictionary = open_dict()
	letters = opening('.\\used_files\\amhletters.txt')
	demonstratives = opening('.\\used_files\\demonstratives.txt')
	personal_pronouns = opening('.\\used_files\\pers_pronouns.txt')
	numerals = opening('.\\used_files\\numerals.txt')
	quest_pronouns = opening('.\\used_files\\quest_pronouns.txt')
	reflexive_pronouns = opening('.\\used_files\\refl_pronouns.txt')
	verbs = opening('.\\used_files\\verbs.txt')
	conjunctions = opening('.\\used_files\\conjunctions.txt')
	poss_pronouns = opening('.\\used_files\\possessive_pronouns.txt')
	postpositions = opening('.\\used_files\\postpositions.txt')

	# apply rule based algorithm
	part_speech = []
	for word in return_word(text, letters):
		if word in dictionary:
			if dictionary[word] == 'n':
				part_speech.append(0)
			if dictionary[word] == 'adj':
				part_speech.append(1)
			if dictionary[word] == 'pron':
				part_speech.append(2)
			if dictionary[word] == 'v':
				part_speech.append(3)
			if dictionary[word] == 'adv':
				part_speech.append(4)
			if dictionary[word] == 'prep':
				part_speech.append(5)
			if dictionary[word] == 'conj':
				part_speech.append(6)
			if dictionary[word] == 'num':
				part_speech.append(7)
		elif word in verbs:
			part_speech.append(3)
		elif word in conjunctions:
			part_speech.append(6)
		elif word in poss_pronouns:
			part_speech.append(5)
		elif word in reflexive_pronouns:
			part_speech.append(2)
		elif word in postpositions:
			part_speech.append(5)
		elif word in demonstratives:
			part_speech.append(2)
		elif word in personal_pronouns:
			part_speech.append(2)
		elif word in numerals:
			part_speech.append(7)
		elif word in quest_pronouns:
			part_speech.append(2)
		elif re.search('[0-9]', word):
			part_speech.append(7)
		else:
			part_speech.append(9)

	# merge results of two algorithms and get set of tags
	i = 0
	for part in part_speech[m:n]:
		if part != 9:
			tags[i] = part
		i += 1
	'''
	print accuracy_score(target, tags)
	print f1_score(target, tags)
	'''
	return tags, words

#rule_ml('features.csv')