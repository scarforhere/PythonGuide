# Programmed by Scar
"""
pyyaml模块：
    文本文件
    服务配置文件

常见内置格式
    xxx.yaml
        name:       ---> key
            Scar    ---> value
        age:
            24
        xinqing:    ---> 列表
            - haha
            - heiehi
        new:        ---> dict
            a: b
            c: 1

方法介绍：
    f = open(yaml_file,'r')         只读模式打开文件
    data = yaml.load(f.read())      导入数据
    f.close()                       关闭文件

返回值：
    字典类型：
    {
        'name':'Scar',
        'age':10,
        'xinqing':['haha','heihei'],
        'new':{'a':'b','c':1}
    }
"""
import yaml


def read(path):
    with open(path, 'r') as f:
        data = f.read()
    result = yaml.load(data, Loader=yaml.FullLoader)
    return result


if __name__ == '__main__':
    result = read("Yaml.yaml")
    print(result)
    print(type(result))
    print(dir(yaml))
