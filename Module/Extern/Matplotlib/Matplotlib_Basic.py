# coding: utf-8
"""
-------------------------------------------------
   Project :       PythonGuide
   File Name :     Matplotlib_Basic
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-12 10:54 AM
-------------------------------------------------
Description : 

    Description

"""
import matplotlib.pyplot as plt
import numpy as np

alpha = np.linspace(0, 6.28, 100)
y = np.sin(alpha)

mm = 1./25.4 # mm --> zoll
fig = plt.figure(figsize=(250*mm, 180*mm)) # 设置图像大小

plt.plot(alpha, y, label=r'$\sin(\alpha)$')
plt.xlabel(r'$\alpha$ in rad')  # 设置x轴注解
plt.ylabel('$y$')   # 设置y轴注解
plt.title('Sinusfunktion')  # 设置图像标题
plt.legend() # 插入线段注解
plt.grid() # 插入背景网格



xx = np.linspace(-2, 2, 100)

mm = 1./25.4 # mm --> zoll
scale = 0.5 # 设置比例缩放
fs = np.array([250*mm, 180*mm])*scale

# 调整右侧空白大小
plt.rcParams['figure.subplot.right'] = .98

# 设置子图模式：1行2列
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=fs);

ax1.plot(xx, xx**2)
ax1.set_title("Subplot 1: $y=x^2$") # 设置子图标题

ax2.plot(xx, xx**3, lw=3)
ax2.set_title("Subplot 2: $y=x^3$")

ax1.plot(xx, xx*0+3, ":k") # 黑色线条 描点 bei y=3

# plt.savefig('test.pdf') # 保存为PDF矢量图形文件
plt.show() # 显示图像

