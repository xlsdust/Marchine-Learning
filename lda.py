# coding=utf-8
import os
import string
import sys
import numpy as np
import matplotlib
import scipy
import matplotlib.pyplot as plt
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import pandas as pd
import numpy as np
import lda
if __name__ == "__main__":
    tian_file =open('./. tianlongbabu.txt').readlines()
    tian_par1 = tian_file[0]
    tian_par2 = tian_file[1]
    tian_par3 = tian_file[2]
    tian_par4 = tian_file[3]
    tian_par5 = tian_file[4]

    corpus = []
    corpus.append(tian_par1.split(','))
    corpus.append(tian_par2.split(','))
    corpus.append(tian_par3.split(','))
    corpus.append(tian_par4.split(','))
    corpus.append(tian_par5.split(','))
    print(corpus)

    '得到字典'
    tianwords = []
    for i in range(len(corpus)):
        tempwords = corpus[i]
        for word in tempwords:
            if len(word) >=6:
                tianwords.append(word)
    tianwords =pd.DataFrame(tianwords,columns=['segment'])

    '移除停用词语'
    stopuserwords =pd.read_csv('stopusewords.txt',encoding= 'utf-8')
    stopuserwords =pd.DataFrame(list(set(stopuserwords['stopusewords'])),columns=['stopusewords'])

    final_stopuse_words = []
    for stopuse in stopuserwords['stopusewords']:
        final_stopuse_words.append(str(stopuse))

    final_tianwords =tianwords[~tianwords['segment'].isin(final_stopuse_words)]

    tianwords =list(set(final_tianwords['segment']))
    tianwords.sort()

    weight =  [[0 for col in range(len(tianwords))]forrow in range(len(corpus))]
    for i in range(len(weight)):
        for j in range(len(weight[i])):
            weight[i][j] =corpus[i].count(tianwords[j])
    weight = np.array(weight)

    model = lda.LDA(n_topics=20,n_iter=1500, random_state=1)
    model.fit(weight)
    topic_word = model.topic_word_  # 得到每个词语在该篇文档中的权重
    n_top_words = 20 #每个主题选择20个单词

#整体的主题分布
    for i, topic_dist in enumerate(topic_word):
        topic_words =np.array(tianwords)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
       print('主题 {}: {}'.format(i, ' '.join(topic_words)))


    titles = ['第一部分','第二部分','第三部分','第四部分','第五部分']
#每篇文档的主题分布
    doc_topic = model.doc_topic_
    for i in range(5):
        print("{} (top 主题: {})".format(titles[i], doc_topic[i].argmax()))
