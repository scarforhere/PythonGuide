# Programmed by Scar
'''
with语句可以自动管理上下文资源，不论什么愿意跳出with块，都能确保文件正确关闭，以此来达到释放资源的目的

语法：
    with open( 'logo.png' , 'rb' ) as src_file:
        src_file.read()                                  # with语句体
'''
print(type(open('a.txt', 'r')))
with open('a.txt', 'r') as file:
    print(file.read())

'''
MyContentMgr实现了特殊方法__enter()__,__exit()__称为该类对象遵守了上下文管理器协议
该类对象的实例对象，成文上下文管理器        

MyContentMgr()
'''
class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')
    def show(self):
        print('shou方法被调用执行了')
        #print('shou方法被调用执行了',1/0)      # 上下文管理器中无论是否产生异常，都将执行enter和exit方法来释放资源

with MyContentMgr() as file:        # 相当于file=MyContentMgr()
    file.show()

# 使用with语句进行文件的复制
with open('Unbenannt.png', 'rb') as src_file:
    with open('copy2.png', 'wb') as target_file:
        target_file.write(src_file.read())
# 不需要手动写文件关闭过程