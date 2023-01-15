# 日志工具类封装
import os
import logging
import time
from pytestlearn.commonlog.config_utils import local_config

current_path = os.path.dirname(__file__)
# log_path = os.path.join(current_path, '../logs')
log_path = os.path.join(current_path, '../%s' % local_config.logPath())


class LogUtils():
    def __init__(self, logPath=log_path):
        self.log_path = logPath
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=local_config.logLevel())
        self.log_name = os.path.join(log_path, 'apiTest_%s.log' % time.strftime('%Y_%m_%d'))

        # 创建控制台对象
        console = logging.StreamHandler()
        # 设置控制台日志输出格式
        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s')
        # 把日志的格式给控制台对象
        console.setFormatter(formatter)
        # 把控制台日志传给logger
        self.logger.addHandler(console)

        # 创建一个log文件日志对象
        file_log = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        # 设置文件日志输出格式
        formatter = logging.Formatter('file:%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s')
        # 把日志的格式给log文件日志对象
        file_log.setFormatter(formatter)
        # 把文件日志传给logger
        self.logger.addHandler(file_log)

    def get_log(self):
        return self.logger


logger = LogUtils().get_log()
