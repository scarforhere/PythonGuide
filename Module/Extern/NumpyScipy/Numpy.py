# coding: utf-8
"""
-------------------------------------------------
   Project :       PythonGuide
   File Name :     Numpy
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-09 10:00 PM
-------------------------------------------------
Description : 

    大数据处理
    回归

"""
import numpy as np
from numpy import array

zahlen = [3.0, 4.0, 5.0] # Liste mit Gleitkommazahlen

# 定义Array
x = array(zahlen)
res1 = x*1.5        # -> array([ 4.5, 6. , 7.5]
print(res1)
res2 = x**2         # -> array([ 9., 16., 25.]
print(res2)
res3 = res1 - res2  # -> array([ -4.5., -10., -18.5]
print(res3)
print()

# 定义多维Array
arr_2d = array( [[1., 2, 3], [4, 5, 6]] )*1.0
print(arr_2d)
print()

# 显示数组维度
print(arr_2d.shape)
print()

# 将数据转化为特定维度
arr_1d=np.arange(12)
arr_set=arr_1d.reshape(3,4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
arr_1d.reshape(4,-1)   # 当参数为-1时，自动按照零一参数进行分配
arr_1d.reshape(-1,3)

# 从多维Array中提取数据
arr_set[2,2]    # 10
arr_set[:2,:2]
# [[0 1]
#  [4 5]]

# Array内元素重组生成新Array
x = np.array([7.5, 8.1, 12.4])
indices = np.array([1, 2, 2, 1, 0])
y = x[indices] # -> array([8.1, 12.4, 12.4, 8.1, 7.5])

# Array内元素判断并生成新Array
x = np.arange(5)
# Alle Werte die kleiner 10 sind negieren:
x[x<2]*=-1  # -> array([ 0, -1,  2,  3,  4])


# 判断Array内元素的正负
array1=np.array([0,2,-2,1.3,-1.3])
array2=np.sign(array1)  # --> array([ 0.,  1., -1.,  1., -1.])

import numpy as np
# 定义包含10个元素的Array，类比于range()
x0 = np.arange(10)
# 定义一个Array从[-10,10)内的200步: array([-10., -9.899497, ..., 10])
x1 = np.linspace(-10, 10, 200)
# x2 = np.logspace(1,100, 1e4) # 10000 Werte, immer gleicher Quotient
# 生乘包含10个0.元素的Array
x3 = np.zeros(10) # np.ones analog
# 生乘包含15个0.元素shape=(3, 5)的Array
x4 = np.zeros( (3, 5) ) # Achtung: nur ein Argument! (=shape)
# 生成shape=(3, 3)的单位矩阵
x5 = np.eye(3)
# 生成3x3对角矩阵Diagonalmatrix
x6 = np.diag( (1, 2, 3) )
# Array内生成5个随机数
x7 = np.random.rand(5)
# Array内生成维度为shape=(4, 2)的8个随机数
x8 = np.random.rand(4, 2)

# 使用r_, c_定义Array行列
from numpy import r_, c_
# 行拼接
x9 = r_[6, 5, 4.]           # array([ 6., 5., 4.])
x10 = r_[x9, -84, x3[:2]]   # array([ 6., 5., 4., -84, 0., 0.])
# 列拼接
x11 = c_[x9, x6 , x5]
# [[6. 1. 0. 0. 1. 0. 0.]
#  [5. 0. 2. 0. 0. 1. 0.]
#  [4. 0. 0. 3. 0. 0. 1.]]


# Array的切片
import numpy as np
a = np.arange(18)*2.0
A = np.array( [ [0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11] ] )
x1 = a[3]       # Element Nr. "3" (-> 6.0)
x2 = a[3:6]     # Elemente 3 bis 5 -> array([ 6., 8., 10.])
x3 = a[-3:]     # Vom 3.-letzten bis Ende -> array([30.,32.,34.])
a[-2:] *= -1    # [-32. -34.]

y1 = A[:, 0] # erste Spalte von A
y2 = A[1, :3 ] # ersten drei Elemente der zweiten Zeile


# 多Array计算维度限制: Broadcasting
import numpy as np
import time
E = np.ones((4, 3)) # -> shape=(4, 3)
print(E)
b = np.array([-1, 2, 7]) # -> shape=(3,)
print(b)
print(E*b) # -> shape=(4, 3)
b_13 = b.reshape((1, 3))
print(b_13)
print(E*b_13) # -> shape=(4, 3)
# print("\n"*2, "Achtung, die nächste Anweisung erzeugt einen Fehler.")
# time.sleep(2)
# b_31 = b_13.T # Transponieren -> shape=(3,1)
# print(b_31)
# print(E*b_31) # broadcasting error


# 对Array内数据处理不需要进行循环
import numpy as np
from numpy import sin, pi            # Tipparbeit sparen
t = np.linspace(0, 2*pi, 1000)
x = sin(t)          # analog: cos, exp, sqrt, log, log2, ...
xd = np.diff(x)     # numerisch differenzieren
# Achtung: xd hat einen Eintrag weniger!
X = np.cumsum(x)    # 累加计算

# Array内进行比较操作
# Elementweise:
y1 = np.arange(3) >= 2  # -> array([False, False, True], dtype=bool)
# Array-weit:
y2 = np.all( np.arange(3) >= 0) # -> True
y3 = np.any( np.arange(3) < 0) # -> False



# 矩阵计算
A=np.arange(4).reshape(2,2)
B=np.arange(6).reshape(2,3)

# 元素内乘
A*A
# array([[0, 1],
#        [4, 9]])

# 矩阵乘法
np.dot(A,A)
# array([[ 2,  3],
#        [ 6, 11]])
np.dot(B.T,A)
# array([[ 6,  9],
#        [ 8, 13],
#        [10, 17]])

# Regression Example 1
import numpy as np
import matplotlib.pyplot as plt
N = 25
xx = np.linspace(0, 5, N)
m, n = 2 , -1 # Doppelzuweisung
# Geradengleichung y = m*x + n auswerten
yy = np.polyval([m, n], xx)
yy_noisy = yy + np.random.randn(N) # Rauschen addieren
# Regressionsgerade
mr, nr = np.polyfit(xx, yy_noisy, 1) # fitten
yyr = np.polyval([mr, nr], xx) # auswerten
plt.plot(xx, yy, 'go--', label="original")
plt.plot(xx, yy_noisy,'k.', label="verrauscht")
plt.plot(xx, yyr,'r-', label="Regression")
plt.legend()
# plt.savefig("regression.png")


# Regression Example 2
# neues Bild
# Bildgröße wird in Zoll erwartet -> Umrechnungsfaktor
mm = 1. / 25.4  # mm to inch
fs = [90 * mm, 60 * mm]
plt.figure(figsize=fs)  # benutzerdef. Bildgröße erzwingen
# Sample data creation
# number of points
n = 10
t = np.linspace(-5, 5, n)
# parameters
a = 0.02;
b = 0.8;
c = -1
x = np.polyval([a, b, c], t)  # alternativ: x = a*t+b
# add some noise
x_noise = x + 0.4 * np.random.randn(n)
# Linear regressison -polyfit - polyfit can be used other orders polys
(ar, br) = np.polyfit(t, x_noise, 1)
xr = np.polyval([ar, br], t)
# Quadratische Regression:
q2, q1, q0 = np.polyfit(t, x_noise, 2)
xqr = np.polyval([q2, q1, q0], t)
# Bildgröße wird in Zoll erwartet -> Umrechnungsfaktor
mm = 1. / 25.4  # mm to inch
fs = [90 * mm, 60 * mm]
plt.figure(figsize=fs)  # benutzerdef. Bildgröße erzwingen
plt.plot(t, x_noise, 'ro')  # Daten
# pl.savefig('bsp3_1.pdf')
plt.plot(t, xr, lw=2)  # lw = linewidth
# pl.savefig('bsp3_2.pdf')
plt.plot(t, xqr, 'g--', lw=2)
# pl.savefig('bsp3_3.pdf')

plt.show()

"""
Numpy相关计算：
    min, max, argmin, argmax, sum (! Skalare)
    abs, real, imag (! Arrays)
    Shape ändern: .T (transponieren), reshape, flatten, vstack, hstack
Lineare Algebra:
    Matrix-Multiplikation:
    dot(a, b) (推荐使用)
    a@b (@-Operator in Python 3.5 eingeführt)
    np.matrix(a)*np.matrix(b) (不推荐)
Submodul: numpy.linalg:
    det, inv, solve (LGS lösen), eig (Eigenwerte u. -vektoren),
    pinv (Pseudoinverse), svd (Singulärwertzerlegung), ...
"""