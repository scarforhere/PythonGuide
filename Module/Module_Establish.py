# Programmed by Scar
"""
在制作发布压缩包的步骤
    1. 创建setup.py文件
        from distutils.core import setup

        setup(name="Module_Establish",  # 包名
              version="1.0",  # 版本
              description="Module_Establish.py包发布演示"，  # 描述信息
              long_description="完整的描述信息",
              author="Scar",  # 作者
              url="www.scar.com",  # 主页
              py_modules=["Module_Establish.demo1",
                          "Module_Establish.demo2"])
        关于字典参数的纤细信息，可以参阅官方网站:
            https://docs.python.org/2/distutils/apiref.html\

    2. 构建模块
        $ python3 setup.py build
        注意： 在Terminal中发布

    3. 生成发布压缩包
        $ python3 setup.py sdist
        注意： 在Terminal中发布

安装模块：
        $ tar -zxvf Module_Establish-1.0.tar.gz
        $ sudo python3 setup.py install

卸载模块：
        $ cd /usr/local/lib/python3.9/dist-packages/
        $ sudo rm -r Module_Establish*
"""