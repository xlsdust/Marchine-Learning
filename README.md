LDA实验
===
### 
---
#### 实验内容
1、Python实现LDA算法，并对天龙八部数据及建立主题模型
2、对比各种分词工具的不同，比较了分词速度、准确度等关键因素
3、运行论文中提出来的基于密度的LDA主题确定算法，该算法是开源的，对论文中的英文播报数据集进行主题划分
4、运行曾大军团队提出来的HDP算法对同一数据集进行建模，该算法也是开源算法，在GitHub上有代码实现，是用JAVA实现的。
5、运行基于困惑度的模型评价算法对主题模型进行评价，确定主题模型的分词的好坏。

#### 结论
1、分词结论写入到大作业中了。
2、基于密度的LDA主题确定算法和基于HDP的主题确定算法对同一数据集进行建模，基于主题密度的建模算法确定的主题数目在80左右，基于HDP的主题确定算法确定的最佳主题数目是80和180，可能是我的参数有些问题。
### 使用说明
1、数据包data中的数据是基于密度的LDA算法使用的数据集合，使用Jupyter可以运行开源的代码，需要自己把数据转化为词频向量。
2、HDP_LDA文件中是曾大军团队的HDP算法实现，使用Eclipse运行，需要自己把数据集标注运行，我使用Excel进行标注的，没有用代码实现，具体用法代码里面的注释给出来了详细解释，基于密度的算法是用包实现的，需要自己去中科大官网下载代码包，这里我之给出了运行时的主函数，DBSCAN_LDA.py
3、LDA_Python是实现的LDA算法，并对天龙八部进行了主题划分，需要自己指定主题数目，具体细节在注释标注了。
4、外面的python文件是之前讲课ppt里面的实验内容。
# Marchine-Learning
