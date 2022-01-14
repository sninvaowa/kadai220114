import numpy as np
import matplotlib.pyplot as plt
 
# データ格納
x = 1452, 1796, 1894, 2584, 2735, 3447
y = 3231, 3747, 3726, 5853, 8866, 10913
a = ["2014年度","2015年度","2016年度","2017年度","2018年度", "2019年度"]
 
# 散布図を描画
plt.scatter(x, y)

plt.title ("散布図", fontname="MS Gothic")
plt.xlabel("オープンキャンパス参加者数(人)", fontname="MS Gothic")
plt.ylabel("志願者数(人)", fontname="MS Gothic")
for i, label in enumerate(a):
    plt.text(x[i], y[i], label)

plt.show()

"""
年度	オープンキャンパス参加者数(人）	志願者数（人）
2014年度	1452	3231
2015年度	1796	3747
2016年度	1894	3726
2017年度	2584	5853
2018年度	2735	8866
2019年度	3447	10913
"""