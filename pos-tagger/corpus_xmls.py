# -*- coding: utf-8 -*-

import os
import codecs
import re
import json
from clastering import Aglomerative_cl
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
	h = codecs.open('hash.json', 'w', 'utf-8')
	json.dump(hash_dict, h, ensure_ascii = False, indent=2)
	h.close()

# function: create xml file with words and their part of speech tag
def create_prs(path):
	id = re.compile(u'<id>([0-1]+)</id>')
	author = re.compile(u'<author>\n((.+\n)+)</author>')
	title = re.compile(u'<title>\n((.+\n)+)</title>')
	date = re.compile(u'<date>\n((.+\n)+)</date>')
	clf = linear_train('features_training.csv', 'targets_training.csv')
	h = codecs.open('hash.json')
	hash_dict = json.load(h)
	h.close()
	names = os.listdir(path)
	for name in names:
		prs_name = name.replace('.txt', '.prs')
		p = codecs.open(prs_name, 'w', 'utf-8')
		f = codecs.open(path + name, 'r', 'utf-8')
		xml = f.read()
		f.close()
		p.write(u'#word\t#part\n')

		def markers(m, xml = xml):
			if m.search(xml):
				n = m.search(xml)
				mark = n.group(1)
			else:
				mark = '--'
				return mark

		id_t = markers(id)
		auth_t = markers(author)
		dat_t = markers(date)
		tit_t = markers(title)
		p.write(u'#meta.docid\t' + id_t + '\n')
		p.write(u'#meta.author\t' + auth_t + '\n')
		p.write(u'#meta.date\t' + dat_t + '\n')
		p.write(u'#meta.title\t' + tit_t + '\n')
		text = re.sub('<.+?>\n?', '', xml)
		text = re.sub(u'\. ?\. ?\.', '', text)
		text = re.sub(u' \. http://books\.google\.com/books\?id=pCEWAQAAIAAJ\. \n', '', text)
		text = re.sub(u'[ \s\t]+', ' ', text)
		feat_name, freq_dictionary, words = feat_extract(name, text)
		for line in linear_class(clf, feat_name, hash_dict):
			p.write(line + '\n')
		p.close()

#gather_big_file('.\\files\\')
#prepare_files_classif('.\\train_data\\', 'training.txt')
create_prs('.\\test_data\\')