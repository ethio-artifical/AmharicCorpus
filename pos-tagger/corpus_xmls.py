# -*- coding: utf-8 -*-

import os
import codecs
import re
from hybrid import rule_ml
from features_extractor import feat_extract

# function: create xml file with words and their part of speech tag
def create_xml(path):
	names = os.listdir(path)
	for name in names:
		f = codecs.open(path + name, 'r', 'utf-8')
		xml = f.read()
		f.close()
		xml_name = name.replace('.txt', '.xml')
		w = codecs.open(xml_name, 'w', 'utf-8')
		w.write('<body><se>')
		text = re.sub('<.+?>\n?', '', xml)
		text = re.sub(u'\. ?\. ?\.', '', text)
		text = re.sub(u' \. http://books\.google\.com/books\?id=pCEWAQAAIAAJ\. \n', '', text)
		text = re.sub(u'[ \s\t]+', ' ', text)
		feat_name, feat_n = feat_extract(name, text)
		m = 0
		if feat_n > 10000:
			n = 10000
			while feat_n > n:
				tags, words = rule_ml(text, feat_name, m , n)
				i = 0
				for word in words:
					w.write(u'<w>' + u'<ana gr="' + str(tags[i]) + u'" />' + word + u'</w>')
					i += 1
				m = n
				n += 10000
		if m == 0:
			n = -1
		tags, words = rule_ml(text, feat_name, m, n)
		i = 0
		for word in words:
			w.write(u'<w>' + u'<ana gr="' + str(tags[i]) + u'" />' + word + u'</w>')
			i += 1
		w.write('</body></se>')
		w.close()

create_xml('.\\wiki\\')