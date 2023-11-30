import logging
import os
import datetime
from common import sharedValue

class Logger:
    def __init__(self, tag):
        try:
            start_time = sharedValue.getInstance().get('time')

            if start_time == -1:
                start_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                sharedValue.getInstance().set('time', start_time)

            log_file = './log/' + str(start_time) + '/' + str(tag) + '.log' 
            if not os.path.exists('./log/' + start_time):
                os.makedirs('./log/' + start_time)

            # 创建一个日志记录器
            self.logger = logging.getLogger(tag)
            self.logger.setLevel(logging.DEBUG)

            # 创建一个文件处理器，用于将日志写入文件
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)

            # 创建一个控制台处理器，用于将日志打印到控制台
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)

            # 创建一个日志格式器
            formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')

            # 将格式器添加到处理器
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # 将处理器添加到日志记录器
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)
            self.__flag = True
        except FileNotFoundError:
            print("File[", log_file, "]: Not Found Error")
            self.__flag = False
        except PermissionError:
            print("File[", log_file, "]: Permission Error")
            self.__flag = False
        except Exception as e:
            print("File[", log_file, "]: ", str(e))
            self.__flag = False
        if self.__flag:
            self.logger.info('/********** START [' + tag + '] **********/')


    def info(self, message):
        if self.__flag:
            self.logger.info(message)

    def warning(self, message):
        if self.__flag:
            self.logger.warning(message)

    def error(self, message):
        if self.__flag:
            self.logger.error(message)

    def debug(self, message):
        if self.__flag:
            self.logger.debug(message)