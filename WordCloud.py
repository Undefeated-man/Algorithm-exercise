"""
	###########################################################################
	#		                                                                  #
	#		Project: WordCloud                                                #
	#		                                                                  #
	#		Filename: WordCloud.py                                            #
	#		                                                                  #
	#		Programmer: Linj                                                  #
	#		                                                                  #
	#		Description: 阿洁的第一个python项目                               #
	#		                                                                  #
	#		Start_date: 2020-08-02                                            #
	#		                                                                  #
	#		Last_update: 2020-08-02                                           #
	#		                                                                  #
	###########################################################################
"""


import wordcloud
import numpy as np
from matplotlib import pyplot as plt
import io
import sys

################################## 函数 ##################################

# 输入文本内容作为参数，统计出每个词的出现频数
def calculate_frequencies(file_contents):
    # 去掉一些咱不感兴趣的词(包括标点符号)
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just",\
    "in"]
    
    # 开始统计(记得把英文的字母全部化作小写)代码写在下面
    
    
    # 生成词云
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequency)
    return cloud.to_array()

################################## 调用区 ###############################

# 生成并显示词云
if __name__ == "__main__":
    # 打开文件并读取字符串
    
    # 调用函数calculate_frequencies
    
    # 显示词云
    plt.imshow(myimage, interpolation = 'nearest')
    plt.axis('off')
    plt.show()