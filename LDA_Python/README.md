python-LDA
===
### lda模型的python实现，算法采用sampling抽样
---
### 训练和输出文本格式说明
#### 模型训练文件
    `train.dat` 用其他软件or算法分词后，再剔除停用词的最后结果文件.

#### 模型输出文件
>        `model_parameter.dat` 保存模型训练时选择的参数 
>        `wordidmap.dat` 保存词与id的对应关系，主要用作topN时查询 
>        `model_twords.dat` 输出每个类高频词topN个 
>        `model_tassgin.dat` 输出文章中每个词分派的结果，文本格式为词id:类id 
>        `model_theta.dat` 输出文章与类的分布概率，文本一行表示一篇文章，概率1   概率2 ...表示文章属于类的概率 
>        `model_phi.dat` 输出词与类的分布概率，是一个K*M的矩阵，其中K为设置分类的个数，M为所有文章的词的总数，

---
### 使用说明
* 用分好词的文本替换掉`data/train.dat`,更详细文档路径查看`setting.conf`
* cd 到lda.py所在目录，执行命令:python lda.py
