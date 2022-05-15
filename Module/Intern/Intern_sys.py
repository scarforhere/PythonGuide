# Programmed by Scar
"""
sys模块：
    sys.modules()           Py启动时加载的模块               别表
    sys.path()              返回但钱Py的环境路径             列表
    sys.exit(0)             退出程序
    sys.getdefaultencoding  或取系统编码                    字符串
    sys.platform            或取当前系统平台                字符串
    sys.version             或取Python版本                 字符串
    sys.argv                程序外部获取参数                列表
"""
import sys

# Py启动时加载的模块
modeles = sys.modules
print(modeles)
print()

# 返回但钱Py的环境路径
path = sys.path
print(path)
print()

# 退出程序
# sys.exit(0)
# sys.exit(1)

# 或取系统编码
code = sys.getdefaultencoding()
print(code)
print()

# 或取当前系统平台\
print(sys.platform)
print()

# 或取Python版本
print(sys.version)
print()

# 程序外部获取参数
print(sys.argv)
