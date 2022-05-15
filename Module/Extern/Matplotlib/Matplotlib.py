 # Programmed by Scar
"""
matpilotlib：
    输出图像

python -m pip install -U pip
pip install numpy
python -m pip install -U pip setuptools
python -m pip install matplotlib


Matplotlib ist sehr umfangreich und komplex
    --> http://matplotlib.org/contents.html

    Tipp 1: Gallery
        Sehr viele Beispiele (Bilder und Code)
        --> http://matplotlib.org/gallery.html
    Tipp 2: Dokumentationen der Axes-Klasse
        --> http://matplotlib.org/api/axes_api.html?matplotlib.axes.Axes
"""
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.pylab import *  # Matlab-artige Umgebung

ion()  # 交互模式启用  需要在最后使用ioff()，否则闪退

plt.figure()

# 生成数列.linspace(start,end,length)
x = np.linspace(-3, 3, 50)

y1 = 2 * x + 1
y2 = x ** 2

# 选择横纵坐标轴显示范围
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# 设置标题
plt.title('Titel')

# 添加横纵坐标轴的Label
x_lb = plt.xlabel('I am x', fontsize=14)
plt.ylabel('I am y')

# 更换单位小标，设置截断距离
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],
           ['really bad', 'bad', '&normal', 'good', 'really good'])

# 调整右侧空白大小
plt.rcParams['figure.subplot.right'] = .98

# 添加曲线，设置曲线颜色、宽度和样式
l1, = plt.plot(x, y1, label='up')
l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='down')
# # Plot mit Optionen (kurz)
# l1,=plot(x,y1, 'ro:',label='up')    # 短注解
# # Plot mit Optionen (lang)
# l2,=plot(x,y2, color='#FF0000', ls=':', lw=2, marker='o',label='down')    # 长注解

# 插入背景网格
grid()

# 线条注解
leg = plt.legend(handles=[l1, l2], labels=['aaa', r'$\frac{\sin(\phi)}{\phi}$'], loc='best')
# 需要在绘制图形时给定label
# handle= 需要在添加曲线时给实例名称加逗号
# label= 将覆盖之前添加曲线时的label
# 支持LATEX语句

# 设置字体大小
setp(l1, linewidth=5)  # 单独设置字体宽度
setp(x_lb, fontsize=20)  # 设置坐标轴注解字体大小
setp(leg.texts, fontsize=20)  # 设置线条注释字体大小

# 移动坐标轴
# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', -1))  # outward,axis(定位到轴的百分之几)
ax.spines['left'].set_position(('data', 0))

"""
添加子图像
"""
xx = np.linspace(-2, 2, 100)

mm = 1. / 25.4  # mm --> zoll
scale = 0.5  # 设置比例缩放
fs = np.array([250 * mm, 180 * mm]) * scale

# 调整右侧空白大小
plt.rcParams['figure.subplot.right'] = .98

# 设置子图模式：1行2列
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=fs);

ax1.plot(xx, xx ** 2)
ax1.set_title("Subplot 1: $y=x^2$")  # 设置子图标题

ax2.plot(xx, xx ** 3, lw=3)
ax2.set_title("Subplot 2: $y=x^3$")

ax1.plot(xx, xx * 0 + 3, ":k")  # 黑色线条 描点 bei y=3

"""
散点图
"""
plt.figure()
n = 1024

# 生成横纵坐标
X = np.random.normal(0, 1, n)  # 中位数为0，方差为1
Y = np.random.normal(0, 1, n)

# 配置颜色
T = np.arctan2(Y, X)  # for color value

# 插入散点图
plt.scatter(X, Y, s=75, c=T, alpha=0.5)
# s= size
# c= color
# alpha= 透明度

# 去除坐标轴
plt.xticks(())
plt.xticks(())

plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))

"""
数目统计
"""
x=np.array([0,9,2,2,8,8,3,3,3,7,7,7,4,4,4,4,6,6,6,6,5,5,5,5,5])
plt.figure()
plt.hist(x)

"""
Image图片
"""
plt.figure()
# 设置颜色
a=np.array([0.313660827978,0.365348418405,0.423733120134,
            0.365348418405,0.439599930621,0.525083754405,
            0.423733120134,0.525083754405,0.651536351379]).reshape(3,3)

plt.xticks(())
plt.yticks(())

plt.imshow(a,interpolation='nearest',cmap='bone',origin='lower')
# interpolation=
# cmap= 边界模糊效果 https://matplotlib.org/stable/gallery/images_contours_and_fields/interpolation_methods
# origin= 上下颠倒 'lower' 'upper'(默认)

# 颜色注释
plt.colorbar(shrink=0.9)
# shrink= 压缩至百分比


# 保存图像
# plt.savefig('./test2.jpg')

# 关闭交互模式
ioff()

# 显示图像
plt.show()


"""
所有的绘图和输出功能同通过axes类进行操作
– ax.plot() , ax.bar() , ax.scatter() , ax.arrow() , . . .
– 注意: 关键字定义

ax.set\_aspect('equal')             页面缩放比 1:1
ax.set\_xlim(0, 10)                 x轴显示范围Wertebereich der X-Achse
ax.set\_xticklabels(['a', 'b'])     设置各自的轴注解
ax.legend(loc=1)                    设置线条注解位置
ax.tick\_params(**kwargs)           替换坐标刻度

设置函数
    setp() 设置某一属性
    getp() 使用**kwargs设置某一属性
        setp(getp(leg, "texts"), fontsize=10)
"""

# import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import scipy.stats as st
matplotlib.rcParams.update({'font.size': 12})

# generate dataset
data_points = 50
sample_points = 10000
Mu = (np.linspace(-5, 5, num=data_points)) ** 2
Sigma = np.ones(data_points) * 8
data = np.random.normal(loc=Mu, scale=Sigma, size=(100, data_points))

# predicted expect and calculate confidence interval
predicted_expect = np.mean(data, 0)
low_CI_bound, high_CI_bound = st.t.interval(0.95, data_points - 1,
                                            loc=np.mean(data, 0),
                                            scale=st.sem(data))

# plot confidence interval
x = np.linspace(0, data_points - 1, num=data_points)
plt.plot(predicted_expect, linewidth=3., label='estimated value')
plt.plot(Mu, color='r', label='grand truth')
plt.fill_between(x, low_CI_bound, high_CI_bound, alpha=0.5,
                label='confidence interval')
plt.legend()
plt.title('Confidence interval')
plt.show()
