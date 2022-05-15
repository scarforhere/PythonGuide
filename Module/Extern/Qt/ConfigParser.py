# coding: utf-8
"""
-------------------------------------------------
   File Name:      ConfigParser
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-05-21 10:29 AM
-------------------------------------------------
Description : 

    Print info with under format:

"""
import configparser
"""
写入Parameter
"""
c = configparser.SafeConfigParser()
c.add_section('Parameter')
c.set('Parameter', 'm1', '1.5')
c.set('Parameter', 'm2', '5')

with open('paramerters.ini', 'w') as fid:
    c.write(fid)

"""
读取Parameter
"""
c = configparser.SafeConfigParser()
c.read('paramerters.ini')
print(c.sections())

m1 = c.get('Parameter', 'm1')
m2 = c.get('Parameter', 'm2')

print(m1)
print(m2)