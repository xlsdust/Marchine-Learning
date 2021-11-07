from sklearn.cluster import KMeans
km_cluster = KMeans(n_clusters=3, max_iter=300, n_init=40,init='k-means++', n_jobs=-1)
result = km_cluster.fit_predict(data)#对句子进行聚类时,data是一个二维的nparray,每个内层的nparray代表每个句子的语义向量，示例  data = np.array([[1.12486,-2.1483,0.1482],[-0.1473,-1.2564,3.1452]])
import numpy as np  # 数据结构
import sklearn.cluster as skc  # 密度聚类
from sklearn import metrics  # 评估模型
result = skc.DBSCAN(eps=1.5, min_samples=3).fit(data)#对句子进行聚类时,data是一个二维的nparray,每个内层的nparray代表每个句子的语义向量，示例  data = np.array([[1.12486,-2.1483,0.1482],[-0.1473,-1.2564,3.1452]])
labels = result.labels_.tolist()
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import jieba
import numpy as np
#使用LDA对文档中的多个句子进行聚类

#读文件分词
with open(filepath,'r') as rf:
    lines = rf.readlines()
split_words = []
for line in lines:
    words = jieba.lcut(line)
    split_words.append(' '.join(words))#split_words用于训练LDA模型，其数据格式为列表
    
#构造词频向量
vectorizer = CountVectorizer()
vec_ft = vectorizer.fit_transform(split_words)

#创建LDA对象
lda = LatentDirichletAllocation(n_components=3, learning_offset=50, random_state=0,n_jobs=-1,max_iter=1000)
#训练LDA模型，得到聚类结果
lda_result = lda.fit_transform(vec_ft)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
vec = np.array([0.1457,0.2496,0.3548],[0.1259,0.1473,0.2846],[5.1478,5.2896,6.2484])
target = np.array([0,0,1])

tsne = TSNE(n_components = 2,init = 'pca',random_state = 0,n_jobs = -1)
output = tsne.fit_transform(vec)
plt.rcParam['figure.figsize'] = 20,20#画布大小
plt.scatter(output[:,0],output[:,1],c=target)
plt.title('cluster result')
plt.save(filepath,bbox_inches = 'tight')
plt.show()

