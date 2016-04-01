# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy_project.items import AmhItem
import codecs, re


i = 1
f = codecs.open('C:\\Users\\Maria\\OneDrive\\MyProjects\\scrapy_project\\scrapy_project\\spiders\\urls.txt', 'r', 'utf-8')
urls = []
domains = []
for line in f:
    url = line.strip()
    allowed_dom = re.sub('https?://(www\.)?', '', url)
    allowed_dom = re.sub('/.+$', '', allowed_dom)
    urls.append(url)
    domains.append(allowed_dom)
f.close()

a = codecs.open('C:\\Users\\Maria\\OneDrive\\MyProjects\\scrapy_project\\scrapy_project\\spiders\\amhletters.txt', 'r', 'utf-8')
letters = []
for line in a:
    line = line.strip()
    letters.append(line)
a.close()

class AmhSpider(CrawlSpider):

    global i

    name = u'amharic'
    allowed_domains = domains #[u'amharic.voanews.com']
    start_urls = urls
    '''[
        u'http://amharic.voanews.com/',
    ]'''

    rules = (
        Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=(u'//a',)), callback=u'parse_items', follow=True),
    )

    def parse_items(self, response):

        global i
        hxs = HtmlXPathSelector(response)
        paragraphs = hxs.xpath(u'//div/p/text()').extract()

        title = hxs.xpath(u'//h1/text()').extract()
        if not title or len(title) > 1:
            title = hxs.xpath(u'//title/text()').extract()

        date = hxs.xpath(u'//*[@class="date"]/text()').extract()
        if not date:
            date = hxs.xpath('//*[@class="postDate"]/text()').extract()
            if not date == '':
                date = hxs.xpath('//*[@class="tie-date"]/text()').extract()
                if not date:
                    date = hxs.xpath('//*[@class="article_date"]/text()').extract()

        author = hxs.xpath(u'//*[@class="author"]/text()').extract()
        if not author:
            author = hxs.xpath(u'//*[@rel="author"]/text()').extract()
            if not author:
                author = hxs.xpath(u'//*[@name="author"]/@content').extract()

        item = AmhItem()
        doc = []
        for p in paragraphs:
            amh = 0
            oth = 0
            content = re.sub(' +', ' ', p)

            for let in content:
                if let not in letters:
                    oth += 1
                else:
                    amh += 1
            if amh > oth and amh > 100:
                doc += [content]

        if doc:
            item['doc'] = u'\n'.join(doc)
            item['id'] = i
            item['link'] = response.url
            i += 1
            if title:
                title = re.sub('[\r\n]', '', title[0])
                title = re.sub('[\s\t]+', ' ', title)
                item['title'] = title
            else:
                item['title'] = ''
            if date:
                date = re.sub('[\r\n]', '', date[0])
                date = re.sub('[\s\t]+', ' ', date)
                item['date'] = date
            else:
                item['date'] = ''
            if author:
                author = re.sub('[\r\n]', '', author[0])
                author = re.sub('[\s\t]+', ' ', author)
                item['author'] = author
            else:
                item['author'] = ''
            yield item
