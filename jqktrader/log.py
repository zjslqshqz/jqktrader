import logging
from datetime import datetime

# 获取当前时间并格式化为字符串
current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# 创建日志文件名
log_filename = f'app_{current_time}.log'

# 配置日志记录器
logger = logging.getLogger("jqktrader")
logger.setLevel(logging.DEBUG)  # 设置logger级别，可以根据需要调整

# 文件处理器
fh = logging.FileHandler(log_filename, mode='a', encoding='utf-8')  # 使用追加模式 ('a') 避免覆盖日志
fh.setFormatter(logging.Formatter(
    "%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d: %(message)s"
))

# 控制台处理器
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)  # 控制台只输出INFO及以上级别的日志
ch.setFormatter(logging.Formatter(
    "%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d: %(message)s"
))

# 添加处理器到logger
logger.addHandler(fh)
logger.addHandler(ch)
