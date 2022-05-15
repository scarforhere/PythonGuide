# coding: utf-8
"""
-------------------------------------------------
   File Name：     Extern_sympy
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-09 10:18 AM
-------------------------------------------------
Description :

    Symbolic Mathematics

    计算机代数模块Computer Algebra Systems(CAS)

    化简公式
    打印公式

    • http://docs.sympy.org/latest/tutorial/index.html
    • http://docs.sympy.org/latest/tutorial/gotchas.html (Fallstricke)
    • Modul-Referenz (Bsp: solve -Funktion)

"""
import sympy as sp

# 添加新符号
x = sp.Symbol('x')
a, b, c = sp.symbols('a b c')

# 计算公式展开,输出变量表达式
z = a * b * x * b + b ** 2 * a * x - c * b * (2 * a / c * x * b - 1 / (b * 2))
print(z)  # -> -b*c*(-1/(2*b) + 2*a*b*x/c) + 2*a*x*b**2
print(z.expand())  # -> c/2 (Ausmutiplizieren)
print()

# 通分,显示分子分母
q=a+b/c
q.as_numer_denom()  # (a*c + b, c)


# 书写数学公式
y = sp.sin(x) * sp.exp(3 * x) * sp.sqrt(a)
print(y)  # -> a**(1/2)*exp(x)*sin(x)
print()

# 计算公式中的三角函数
t=sp.cos(10).evalf()    # -0.839071529076452

# 定义函数
f1 = sp.Function('f')  # -> sympy.core.function.f (nicht ausgewertet)
g1 = sp.Function('g')(x)  # -> g(x)    (Funktion ausgewertet bei x)

# 求导
print(y.diff(x))  # -> 3*sqrt(a)*exp(3*x)*sin(x) + sqrt(a)*exp(3*x)*cos(x)
# 求2阶导数
print(g1.diff(x, 2))  # -> Derivative(g(x), x)
print()

# 双曲函数化简
print(sp.trigsimp(sp.sin(x) ** 2 + sp.cos(x) ** 2))  # -> 1
print()

# 变量替换
# <expr>.subs([(alt1, neu1), (alt2, neu2), ...])
term1 = a * b * sp.exp(c * x)
term2 = term1.subs(a, 1 / b)
print(term2)  # -> exp(c*x)
print()

# 求固定点导数
f = a * sp.sin(b * x)
df_xa = f.diff(x)
# Funktion erzeugen
df_xa_fnc = sp.lambdify((a, b, x), df_xa, modules='numpy')
# Funktion auswerten
print(df_xa_fnc(1.2, 0.5, 3.14))
print()

# 生成矩阵
M=sp.Matrix([[x,a+b],[c*x,sp.sin(x)]])

# 矩阵求导
M.diff(a)   # Matrix([[0, 1], [0, 0]])
M.diff(b)   # Matrix([[0, 1], [0, 0]])

# 取出矩阵元素
M[0,1]      # a + b
M[:,1]      # Matrix([[a + b], [sin(x)]])\

# 求雅各比矩阵
s1=M[:,1]
s1.jacobian([a,x])      # Matrix([[1, 0], [0, cos(x)]])

# 积分
sp.integrate(x+x**3/5,x)
print(sp.integrate(x+x**3/5,x)) # x**4/20 + x**2/2

# 方程求解
# res = <expr>.solve([Eq1, Eq2], [target1, target2])
x, y = sp.symbols('x y')
Eq1=x-y-1               # x-y-1=0
res=sp.solve(Eq1, x)    # [y + 1]

# 生成方程
Eq1a = sp.Eq(y, x+1)


# 使用Latex输出数学公式
def preview(expr, **kwargs):
    """
     Hilfsfunktion zur "schönen" Anzeige umfangreicher Ausdrücke
     """

    import matplotlib.pyplot as plt
    latex_str = "$ %s $" % sp.latex(expr, **kwargs)
    latex_str = latex_str.replace("operatorname", "mathrm")
    plt.figure(figsize=(20, 5))  # 20x5 Zoll
    plt.text(0.5, 0.5, latex_str, fontsize=30, horizontalalignment='center')
    plt.axis('off')
    plt.show()

preview(Eq1a)

import sympy as sp

