# Programmed by Scar
"""
logging模块：
    日志模块
    日志作用：
        日记
        记录程序的行为
        重要信息记录
    日志等级：
        debug
        info
        warnning
        error
        critical
常用方法：
    logging.basicConfig()
        参数名:
            level       日志输出等级         level=logging.DEBUG
            format      日志输出格式
            filename    存储位置            filename='d://back.log'
            filemode    输入模式            filemode="w"
        format具体格式:
            %(levelname)s   日志级别名称
            %(pathname)s    执行程序的路径
            %(filename)s    执行程序组名
            %(lineno)d      日志当前行号
            %(asctime)s    打印日志的时间
            %(message)s     日志信息
        常用format格式符方案：
            format="%(asctime)s %(filename)s[line: %(lineno)d] %(levelname)s %(message)s"
"""
import logging
import os

def init_log(path):
    if os.path.exists(path):
        mode='a'
    else:
        mode='w'
    logging.basicConfig(
        level=logging.INFO,         # 低于Info的等级不会被触发
        format="%(asctime)s:\n\t%(filename)s [line: %(lineno)d] : %(levelname)s %(message)s",
        filename=path,
        filemode=mode
    )
    return logging

current_path=os.getcwd()
path=os.path.join(current_path,"LogInfo.log")
log=init_log(path)

# logging.basicConfig(level=logging.ERROR,format="%(asctime)s:\n\t%(filename)s [line: %(lineno)d] : %(levelname)s %(message)s")
# logging.basicConfig(level=logging.warn,format="%(asctime)s:\n\t%(filename)s [line: %(lineno)d] : %(levelname)s %(message)s")
log.debug("这是一个DEBUG")
log.info("这是一个信息")
log.warning("这是一个警告")
log.error("这是一个重大错误信息")
