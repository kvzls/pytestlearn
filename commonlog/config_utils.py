import configparser
import os

#configparser资料： https://blog.csdn.net/SYTyu/article/details/122959749


current_path = os.path.dirname(__file__)
cfg_path = os.path.join(current_path, '../config/config.ini')
# cfg = configparser.ConfigParser()
# cfg.read(cfg_path, encoding='utf-8')
# log_path = cfg.get('log', 'log_path')
# print(log_path)
# log_level = cfg.get('log', 'log_level')
# print(log_level)


class CfgUtils():
    def __init__(self):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(cfg_path, encoding='utf-8')

    def logPath(self):
        log_path = self.cfg.get('log', 'log_path')
        return log_path

    def logLevel(self):
        log_level = self.cfg.getint('log', 'log_level')
        return log_level


local_config = CfgUtils()

# if __name__ == '__main__':
#     local_config = CfgUtils()
#     print(local_config.logPath())
#     print(local_config.logLevel())
