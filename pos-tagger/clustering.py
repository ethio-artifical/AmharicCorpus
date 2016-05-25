# coding: utf-8

import pandas
import codecs
import re
import itertools
from sklearn.cluster import KMeans, MiniBatchKMeans, AgglomerativeClustering
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import scale

# function: opening tables
def opening_data_target(feat_name):
	# getting features
	data = pandas.read_csv(feat_name, header=None, sep=';')
	features = data.iloc[:, 1:]

	# getting targets
	#data_target = pandas.read_csv('.\\test_data\\test_ml.csv', header=None, sep=';')
	#target = data_target.iloc[:, 1]

	return features

# function: features selection
def feature_selection(features):
	sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
	features = sel.fit_transform(features)
	return features

# function: finding the best values of tags
def validate_with_mappings(preds, target, dataset):
	arr = []
	map_preds = []
	permutations = itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 0])
	for a, b, c, d, e, f, g, h, i in permutations:
		mapping = {8: i, 7: a, 6: b, 5: c, 4: d, 3: e, 2: f, 1: g, 0: h}
		mapped_preds = [mapping[pred] for pred in preds]
		map_preds.append(mapped_preds)
		arr.append(float(sum(mapped_preds != target)) / len(target))
	return map_preds[arr.index(min(arr))]

# function: k-means clustering algorithm
def K_means(feat_name):
	features = opening_data_target(feat_name)
	features = scale(features)

	km = KMeans(n_clusters=9, random_state=242)

	km_preds = km.fit_predict(features)

	# getting k-mans tags
	#km_tags = validate_with_mappings(km_preds, target, features)

	# K-means results
	''''
	print 'Accuracy ', accuracy_score(target, km_tags)
	print 'Precision ', precision_score(target, km_tags)
	print 'Recall ', recall_score(target, km_tags)
	print 'F1 ', f1_score(target, km_tags)
	'''
	return km_preds

# function: aglomerative clustering algorithm
def Aglomerative_cl(feat_name):
	features = opening_data_target(feat_name)
	features = scale(features)

	ac = AgglomerativeClustering(n_clusters=4, linkage='average', affinity='cosine') #cosine

	ac_preds = ac.fit_predict(features)

	# getting aglomerative tags
	# need only for evaluation
	#ac_tags = validate_with_mappings(ac_preds, target, features)

	# Aglomerative results
	'''
	print 'Accuracy ', accuracy_score(target, ac_tags)
	print 'Precision ', precision_score(target, ac_tags)
	print 'Recall ', recall_score(target, ac_tags)
	print 'F1 ', f1_score(target, ac_tags)
	'''
	return ac_preds

#K_means('.\\test_data\\features.csv')
#Aglomerative_cl('.\\test_data\\features.csv')
