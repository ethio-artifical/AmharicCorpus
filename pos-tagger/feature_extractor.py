if len(word) >= 2 and ((word[-1] == u'ች' or word[-1] == u'ቹ') and word[-2] in vowel_o):

if len(word) >= 2 and (word[-1] == u'ው' or word[-1] == u'ዋ' or word[-1] in vowel_u or word[-1] == u'ቱ'):

if len(word) >= 3 and (word[-2:] == u'ዮዋ' or word[-2:] == u'ዮው'):

if len(word) >= 2 and word[0] == u'የ':

if len(word) >= 4:
    for i in range(0, len(word) - 1):
        if word[i] == word[i + 1]:
            print 'DOUBLE LETTER DETECTED'
            break

if len(word) >= 3 and (word[:2] == u'የዚ' or word[:2] == u'በዚ' or word[:2] == u'ከዚ'):

if len(word) >= 2 and word[0] == u'ከ':

if len(word) >= 2 and (word[-1] == u'ኛ' or word[-1] == u'ም'):

if len(word) >= 3 and word[-2] in consonants and (word[-1] == u'ህ' or word[-1] == u'ክ' or word[-1] == u'ሁ'or word[-1] == u'ኩ' or word[-1] == u'ሽ'

if len(word) >= 2 and word[-1] in vowel_u:

if len(word) >= 2 and word[-1] in vowel_ae:

if len(word) >= 3 and (word[-2] in vowel_ae and word[-1] == u'ች'):

if len(word) >= 4 and word[-3:] == u'አችሀ':

if len(word) >= 2 and word[-1] == u'ን':

if len(word) >= 2 and (word[0] == u'በ' or word[0] == u'ባ' or word[0] == u'ከ' or word[0] == u'ካ' or word[0] == u'እ' or word[0] == u'ለ' or word[0] == u'ስ'

object_suffixes = [u'ኝ', u'ህ', u'ሽ', u'ው', u'ን']
if len(word) >=2 and word[-1] in object_suffixes:
    print 'OBJECT SUFFIX DETECTED'
if len(word) >=3 and word[-2:] == u'ዎት':
    print 'OBJECT SUFFIX DETECTED'
if len(word) >=3 and word[-2] in vowel_a and word[-1] == u'ት':
    print 'OBJECT SUFFIX DETECTED'
if len(word) >=4 and word[-3] in vowel_a and (word[-2:] == u'ቸው' or word[-2:] == u'ችሁ' or word[-2:] == u'ቸው' or word[-2:] == u'ችሁ'):
    print 'OBJECT SUFFIX DETECTED'
if len(word) >=3 and word[-1] == u'ት' and word[-2] in vowel_u:
    print 'OBJECT SUFFIX DETECTED'

if len(word) >= 3 and (word[-1] == u'ም' or word[0] == u'አ'):

if len(word) >= 3 and (word[0] == u'እ' or word[0] == u'ች' or word[0] == u'ይ'):

if len(word) >= 4 and word[-3] in vowel_a and (word[-2:] == u'ለሁ' or word[-2:] == u'ለህ' or word[-2:] == u'ለሽ' or word[-2:] == u'ለች' or word[-2:] == u'ለን' or word[-2:] == u'ችሁ'):

if len(word) >= 3 and word[-2] in vowel_a and (word[-1] == u'ሉ' or word[-1] == u'ል'):

if len(word) <= 3 and (word[-2] == u'ኛ' and (word[-1] == u'ው' or word[-1] == u'ዋ' or word[-1] in vowel_u)) or (word[-1] == u'ም' and (word[-2] == u'ው' or word[-2] == u'ዋ' or word[-2] in vowel_u)):

if len(word) >= 2 and word[0] == u'መ':
    print 'INFINITIVE PREFIX DETECTED'
if len(word) >= 2 and word[-1] == u'ት':
    print 'INFINITIVE SUFFIX DETECTED'
if len(word) >= 4 and word[:3] == u'አለመ':
    print 'INFINITIVE PREFIX WITH NEGATION DETECTED'

if len(word) >= 2 and word[0] == u'ተ':

middle_tongue_a = [u'ቻ', u'ጃ', u'ጫ', u'ኻ', u'ዣ', u'ኛ', u'ያ']
if len(word) >= 2 and word[-1] in middle_tongue_a:

middle_tongue = [u'ች', u'ኝ', u'ዥ', u'ጭ', u'ጅ', u'ኽ', u'ይ']
front_tongue_i = [u'ቲ', u'ዲ', u'ጢ', u'ሲ', u'ዚ', u'	ኪ', u'ሊ']
if len(word) >= 2 and (word[-1] in middle_tongue or (word[-1] in vowel_i and word[-1] not in front_tongue_i)):

if len(word) >=2 and word[0] == u'አ':

if word[0] == u'የ' or word[:2] == u'የም' or word[:2] == u'ያል':

if len(word) >= 3 and (word[0] == u'የ' or word[:2] == u'የም' or word[:2] == u'ያል'):

if len(word) >= 2 and (word[0] == u'ሌ' or word[0] == u'ለ'):

if len(word) >= 3 and (word[-1] in vowel_e or word[-1] in vowel_a or word[-1] in vowel_o or ((word[-1] == u'ህ' or word[-1] == u'ሽ' or word[-1] == u'ሽ') and word[-2] in vowel_ae)):
    print 'ADVERBIAL PARTICIPLE 1 DETECTED'
if len(word) >= 4 and ((word[-2:] == u'ችሁ' and word[-3] in vowel_a) or (word[-2] in vowel_o and word[-1] == u'ው')):
    print 'ADVERBIAL PARTICIPLE 1 DETECTED'
if len(word) >= 3 and word[:2] == u'በመ':
    print 'ADVERBIAL PARTICIPLE 2 DETECTED'
if len(word) >= 3 and (word[:2] == u'እየ' and (word[-1] == u'ሁ' or word[-1] == u'ህ' or word[-1] == u'ሽ' or word[-1] in vowel_ae or word[-1] in vowel_u)):
    print 'ADVERBIAL PARTICIPLE 3 DETECTED'
    # второе употребляется с формой прошедшего
if len(word) >= 4 and (word[:2] == u'እየ' and ((word[-2:] == u'ችሁ' and word[-3] in vowel_a) or (word[-1] == u'ች' and word[-2] in vowel_ae) or (word[-1] == u'ን' and word[-2] in consonants))):
    print 'ADVERBIAL PARTICIPLE 3 DETECTED'
if len(word) >= 3 and (word[:2] == u'ስት' or word[:2] == u'ስን' or word[0] == u'ሲ'):

if word[-1] == u'ም':
    if len(word) >= 4 and (word[-2] in vowel_e or word[-2] in vowel_a or word[-2] in vowel_o or ((word[-2] == u'ህ' or word[-2] == u'ሽ' or word[-2] == u'ሽ') and word[-3] in vowel_ae)):
        print 'ADVERBIAL PARTICIPLE 1 DETECTED'
    if len(word) >= 5 and ((word[-3:] == u'ችሁ' and word[-4] in vowel_a) or (word[-3] in vowel_o and word[-2] == u'ው')):
        print 'ADVERBIAL PARTICIPLE 1 DETECTED'
    if len(word) >= 4 and (word[:2] == u'እየ' and (word[-2] == u'ሁ' or word[-2] == u'ህ' or word[-2] == u'ሽ' or word[-2] in vowel_ae or word[-2] in vowel_u)):
        print 'ADVERBIAL PARTICIPLE 3 DETECTED'
    if len(word) >= 5 and (word[:2] == u'እየ' and ((word[-3:] == u'ችሁ' and word[-4] in vowel_a) or (word[-2] == u'ች' and word[-2] in vowel_ae) or (word[-2] == u'ን' and word[-3] in consonants))):
        print 'ADVERBIAL PARTICIPLE 3 DETECTED'

if u'አለሁ' in word or u'አለች' in word or u'አል' in word:

if len(word) >= 4 and (((word[-2:] == u'ለሁ' or word[-2:] == u'ለች') and word[-3] in vowel_a) or (word[-1] == u'ል' and word[-2] in vowel_a)):

if len(word) >= 4 and (word[-1] in consonants or word[-1] in vowel_i or word[-1] in vowel_u):

if len(word) >= 4 and (word[-1] in consonants or word[-1] in vowel_u) and (word[0] == u'ል' or word[0] == u'ይ' or word[0] == u'ት' or word[:2] == u'እን'):

if len(word) >= 4 and (word[:2] == u'ስለ' or word[:2] == u'ስለም'):

if len(word) >= 4 and ((word[-1] == u'ኛ' and (word[-2] in vowel_ae or word[-2] in consonants)) or ((word[-2:] == u'ነት' or word[-1] == u'ታ') and word[-2] in consonants)):

