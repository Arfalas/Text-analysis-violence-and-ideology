
import spacy 
from spacy.matcher import Matcher
from spacy.tokens import Span
from datetime import datetime

months_list = ['DECEMBRA', 'FEBRUARJA', 'JANUARJA', 'MARCA', 'APRILA', 'MAJA', 'AVGUSTA', 'SEPTEMBRA', 'NOVEMBRA', 'JUNIJA', 'JULIJA', 'OKTOBRA']
c = 0 
while c < 123:
    arfa1a5 = open('C:/Users/No Name/OneDrive/Desktop/vezba/orjuna{}.txt'.format(c), 'r', encoding='utf_8')
    arfa1a5 = arfa1a5.read()
    text_list = arfa1a5.split()
    c = c + 1
# Iterating through the list and extracting dates to a single .txt file
    for i in text_list:
        for j in months_list:
            if (i == j):
                month = j
                list_index = text_list.index(j)
                dan = list_index - 1
                day = text_list[dan]
                godina = list_index + 1
                year = text_list[godina]
                datum = day + '-' + month + '-' + year
                datum = datum.replace('.', '')
                datum = datum.replace('DECEMBRA', '12')
                datum = datum.replace('JANUARJA', '1')
                datum = datum.replace('FEBRUARJA', '2')
                datum = datum.replace('MARCA', '3')
                datum = datum.replace('APRILA', '4')
                datum = datum.replace('MAJA', '5')
                datum = datum.replace('JUNIJA', '6')
                datum = datum.replace('JULIJA', '7')
                datum = datum.replace('AVGUSTA', '8')
                datum = datum.replace('SEPTEMBRA', '9')
                datum = datum.replace('OKTOBRA', '10')
                datum = datum.replace('NOVEMBRA', '11')
                datum = datum.replace('UUBIJANA_', '')
                datum = datum.replace('1824', '1924')
                datum = datum.replace(',', '')
                datum = datum.replace('V', '1924')
                datum = datum.replace('1923 ', '1923')
                datum = datum.replace('1924 ', '1924')

    # this is where the text processing beggins from Vienna2023.py
    # loading Slovenian language pack:
    
    words = open('C:/Users/No Name/OneDrive/Desktop/vezba/wordlist.txt', 'r', encoding='utf_8')
    words = words.read()
    wordlist = words.split()

    
    
    
    my_list = []
    for i in wordlist:
        processing_words_dict = [{'LOWER' : i}]
        my_list.append(processing_words_dict)

    # loading Slovenian language pack:
    nlp = spacy.load("sl_core_news_sm")


    # text input:
    doc = nlp(arfa1a5)

    # tokenizing the text:
    slo_tokens = []
                
    for i in doc:
        slo_tokens.append(i)
    #print('Tokens are: ', slo_tokens)
    token_numbers = len(slo_tokens)
    token_number = ('Number of tokens: {}'.format(token_numbers))
         
    # loading Matcher and setting search words:
    slo_matcher = Matcher(nlp.vocab)
    slo_matcher.add('TokenMatch', my_list)
    matches = slo_matcher(doc)


    # extracting matched results:
    results_full = ''
    for m_id, start, end in matches:
        string_id = nlp.vocab.strings[m_id]
        span = doc[start:end]
        results = 'match_id:{}, string_id:{}, Start:{}, End:{}, Text:{}'.format(m_id, string_id, start, end, span.text)
        #print(results)
        results_full = results_full + results  
    
    matches = len(matches)
    match_number = 'The number of matches is:{}'.format(matches)
    match_number_csv = str(matches)

    final_result = datum + ',' + token_number + ',' + results_full + ',' + match_number + '\n'
    # write results to file
    with open("C:/Users/No Name/OneDrive/Desktop/vezba/full_analysis.txt", "a", encoding="utf_8") as f:
        f.write(final_result)

    csv_file = datum + ' ' + match_number_csv + ' '

    with open("C:/Users/No Name/OneDrive/Desktop/vezba/dict_datetime.txt", "a", encoding="utf_8") as f:
        f.write(csv_file)
                    
print('Done!')


'''
f = open("C:/Users/No Name/OneDrive/Desktop/vezba/vezba1.txt", 'r')
string = f.read()
list = string.split('\n')
print(list)
'''
# create a dictionary (datetime as key) (number of words occurences are values), and then order the data by date
# create the final .csv file for data visualization
# for next itterations maybe remove noise from the text and use FUZZY