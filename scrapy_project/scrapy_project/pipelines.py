# -*- coding: utf-8 -*-

import codecs


class JsonWithEncodingPipeline(object):

    def process_item(self, item, spider):
        with codecs.open('./files/' + str(item['id']) + '.xml', 'w', 'utf-8') as f:
            text = '<?xml version="1.0" encoding="UTF-8"?>\n<meta>\n<id>' + \
                   str(item['id']) + '</id>\n<link>' + item['link'] + '</link>\n<title>' + \
                   item['title'] + '</title>\n<author>' + item['author'] + '</author>\n<date>' + \
                   item['date'] + '</date>\n</meta>\n<text>\n' + item['doc'] + '\n</text>'
            f.write(text)
        f2 = codecs.open('./files/table.csv', 'a', 'utf-8')
        text = str(item['id']) + ';' + item['link'] + ';' + item['author'] + \
                ';' + item['date'] + ';' + item['title'] + ';\n'
        f2.write(text)
        f2.close()

        return item