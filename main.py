import pandas as pd
import spacy

ex_data = pd.read_excel('data.xlsx')


nlp = spacy.load('ru_core_news_sm')

f = open('res.txt', 'w', encoding='utf-8')
incr = 1
for text in ex_data['text'].values:
    doc = nlp(text)
    news_list = []
    textToWrite = 'Новость ' +  str(incr) + '\n'
    f.write(textToWrite)
    f.write('Действующие лица:\n')

    for ent in doc.ents:
        if ent.label_ == 'ORG' or ent.label_ == 'PER':
           news_list.append(str(ent.text))

    news_list = list(dict.fromkeys(news_list))
    for item in news_list:
        f.write(item)
        f.write('\n')
    f.write('\n') 
    print(incr)
    incr+=1
f.close()
