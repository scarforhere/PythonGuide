# Programmed by Scar
import math

class Circle(object):
    def __init__(self,r):
        self.r=r

    def get_area(self):
        return math.pi*math.pow(self.r,2)

    def get_perimeter(self):
        return 2*math.pi*self.r

if __name__ == '__main__':
    r=float(input("请输入半径："))
    print(f'圆的面积为：{Circle(r).get_area():.4f}')
    print(f'圆的周长为：{Circle(r).get_perimeter():.4f}')