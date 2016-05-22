# -*- coding: utf-8 -*-

import os
import codecs
import re
import json
from clustering import Aglomerative_cl, K_means
from features_extractor_3 import feat_extract
from classification import linear_class, linear_train

# gather file for clustering
def gather_big_file(path):
	names = os.listdir(path)
	res = re.compile(u'<text>\n((.+\n)+)</text>')
	w = codecs.open('training_file.txt', 'w', 'utf-8')
	for name in names:
		f = codecs.open(path + name, 'r', 'utf-8')
		xml = f.read()
		f.close()
		se = res.search(xml)
		w.write(se.group(1))
	w.close()

def prepare_files_classif(path, name):
	hash_dict = {}
	f = codecs.open(path + name, 'r', 'utf-8')
	text = f.read()
	f.close()
	csv_name = name.replace('.txt', '.csv')
	w = codecs.open('targets_' + csv_name, 'w', 'utf-8')
	text = re.sub(u'<.+?>\n?', '', text)
	text = re.sub(u'\. ?\. ?\.', '', text)
	text = re.sub(u' \. http://books\.google\.com/books\?id=pCEWAQAAIAAJ\. \n', '', text)
	text = re.sub(u'[ \s\t]+', ' ', text)
	feat_name, freq_dictionary, words = feat_extract(name, text)
	tags = Aglomerative_cl(feat_name)
	i = 0
	for word in words:
		if freq_dictionary[word] > 5:
			hash_dict[word] = tags[i]
		w.write(word + u';' + unicode(tags[i]) + u'\n')
		i += 1
	w.close()
	h = codecs.open('.\\train_data\\hash.json', 'w', 'utf-8')
	json.dump(hash_dict, h, ensure_ascii = False, indent=2)
	h.close()

# function: create xml file with words and their part of speech tag
def create_prs(path):
	id = re.compile(u'<id>([0-9]+)</id>\n')
	author = re.compile(u'<author>(.+)</author>\n')
	title = re.compile(u'<title>(.+)</title>\n')
	date = re.compile(u'<date>(.+)</date>\n')
	source = re.compile(u'<link>(.+)</link>')
	txt = re.compile(u'<text>\n((.+|[\r\n])+)</text>')
	clf = linear_train('.\\train_data\\features_training.csv', '.\\train_data\\targets_training.csv')
	h = codecs.open('.\\train_data\\hash.json')
	hash_dict = json.load(h)
	h.close()
	names = os.listdir(path)
	numb_of_words = 0
	for name in names:
		prs_name = name.replace('.xml', '.prs')
		p = codecs.open(u'prs_files\\' + prs_name, 'w', 'utf-8')
		f = codecs.open(path + name, 'r', 'utf-8')
		xml = f.read()
		f.close()
		p.write(u'#sentno	#wordno	#lang	#graph	#word	#indexword	#nvars	#nlems	#nvar	#lem	#trans	#lex	#gram	#flex	#punctl	#punctr	#sent_pos\n')

		def markers(m, xml = xml):
			if m.search(xml):
				n = m.search(xml)
				mark = n.group(1)
			else:
				mark = ''
			return mark

		id_t = markers(id)
		auth_t = markers(author)
		dat_t = markers(date)
		tit_t = markers(title)
		sour_t = markers(source)

		p.write(u'#meta.docid	' + id_t + '\n')
		p.write(u'#meta.source	' + sour_t + '\n')
		p.write(u'#meta.author	' + auth_t + '\n')
		p.write(u'#meta.title	' + tit_t + '\n')
		p.write(u'#meta.date_displayed	' + dat_t + '\n')
		t_t = txt.search(xml)
		text = t_t.group(1)
		feat_name, freq_dictionary, words, numb_sent, whole_words = feat_extract(name, text)
		p.write(u'#meta.words	' + str(len(words)) + '\n')
		p.write(u'#mta.sentences	' + str(numb_sent-1) + '\n')
		for line in linear_class(clf, feat_name, hash_dict):
			p.write(line + '\n')
		p.close()
		numb_of_words += whole_words
		print numb_of_words

#gather_big_file('.\\files\\')
#prepare_files_classif('.\\train_data\\', 'training.txt')
create_prs('.\\corpus_files\\')