import time

testCases=["汽水不如果汁好喝 ", "小白痴痴地在门前等小黑回来" , ]

#中文分词
print("_____________jieba___________")
import  jieba
t1 =time.time()
# 精确模式
for sentence in testCases:
    seg_list = jieba.cut(sentence)
    print(seg_list )
    print("Default Mode: " + "/ ".join(seg_list)) # 精确模式
t2 = time.time()
print("jieba time",t2-t1)
print("_____________thulac___________")
import thulac
t1 =time.time()
thu1 = thulac.thulac()  # 默认模式
for sentence in testCases:
    text = thu1.cut(sentence, text=True)  # 进行一句话分词
    print(text)
t2 = time.time()
print("thulac time",t2-t1)
print("_____________fool___________")
import fool
t1 =time.time()
for sentence in testCases:
    print(fool.cut(sentence))
t2 = time.time()
print("fool time",t2-t1)

print("_____________HanLP___________")
from pyhanlp import *
t1 =time.time()
for sentence in testCases:
    print(HanLP.segment(sentence))
t2 = time.time()
print("hanlp time",t2-t1)

print("_____________中科院nlpir___________")
import pynlpir  # 引入依赖包
pynlpir.open()  # 打开分词器
t1 =time.time()
for sentence in testCases:
    print(pynlpir.segment(sentence, pos_tagging=False) )  # 使用pos_tagging来关闭词性标注
t2 = time.time()
print("中科院nlpir time",t2-t1)
#使用结束后释放内存：
pynlpir.close()

print("_____________哈工大ltp___________")
from pyltp import Segmentor
LTP_DATA_DIR = 'E:\MyLTP\ltp_data'  # ltp模型目录的路径、
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
segmentor = Segmentor()  # 初始化实例
segmentor.load(cws_model_path)  # 加载模型
t1 =time.time()
for sentence in testCases:
    words = segmentor.segment(sentence)  # 分词结果,pyltp.VectorOfString object
    # s_fenci = list(words)
    # print('分词结果',list(words))
    s_fenci_str = '\t'.join(words)  # str
    print("哈工大",s_fenci_str)
t2 = time.time()
print("哈工大ltp",)
segmentor.release()  # 释放模型

thu1 = thulac.thulac()  # 默认模式
pynlpir.open()  # 打开中科院分词器
segmentor = Segmentor()  # 哈工大分词器初始化实例
segmentor.load(cws_model_path)  # 加载模型
for sentence in testCases:
    print("_______****___________")
    seg_list = jieba.cut(sentence)
    print("jieba: " + "/ ".join(seg_list)) # 精确模式
    text = thu1.cut(sentence, text=True)  # 进行一句话分词
    print("thulac",text)
    print("fool",fool.cut(sentence))
    print("HanLP",HanLP.segment(sentence))
    print("中科院",pynlpir.segment(sentence, pos_tagging=False))  # 使用pos_tagging来关闭词性标注
    #哈工大
    words = segmentor.segment(sentence)  # 分词结果,pyltp.VectorOfString object
    s_fenci_str = '\t'.join(words)  # str
    print("哈工大",s_fenci_str)
pynlpir.close()
segmentor.release()  # 释放模型

