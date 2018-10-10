# coding=utf-8

import io
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

#设置要过滤掉的停用词
STOPWORDS.add("Java")
STOPWORDS.add("Boss")
STOPWORDS.add("doc")
STOPWORDS.add("docx")
STOPWORDS.add("Web")
STOPWORDS.add("jpg")
STOPWORDS.add("png")
STOPWORDS.add("pdf")
STOPWORDS.add("J2EE")
wc = WordCloud(background_color="white",
                      stopwords=STOPWORDS,
                      max_words=200,
                      font_path='C:/Windows/Fonts/simkai.ttf',
                      width=2000,
                      height=1800,
                      margin=2)
#python2.7 显示中文设置
# f = io.open('D:\\temp\\all.txt', 'r',encoding='utf-8').read()
f = open('D:\\temp\\all.txt', 'r').read()

wc.generate(f)
plt.imshow(wc)
plt.axis("off")
plt.show()
wc.to_file('D:\\temp\\result.png')
