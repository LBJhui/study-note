# _*_ coding: utf-8 _*_
# @Time: 2024/3/27 10:48
# @Author: LBJ辉
# @File: test_loguru
# @Project: nxops
import sys
from loguru import logger

logger.debug("debug message")
logger.info("info level message")
logger.warning("warning level message")
logger.critical("critical level message")

# Loguru支持丰富的配置选项，能够根据项目的需求进行定制。
logger.add("output.log", rotation="500 MB", level="INFO")
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")

# Loguru不仅能记录简单的信息，还可以捕获和记录异常追踪信息，有助于更快地定位问题
try:
    result = 1 / 0
except Exception as e:
    logger.exception("An error occurred: {e}")

# Loguru支持灵活的消息格式化，可以轻松地添加自定义信息、时间戳等

logger.info("User {user} logged in at {time}", user="Alice", time="2023-01-01 12:00:00")

# 为了避免日志文件变得过大，Loguru支持日志旋转。可以根据文件大小或时间来触发日志旋转
logger.add("rotating_log.log", rotation="100 MB", retention="10 days", level="INFO")
# logger.add("test.log", rotation="10 MB")  # 文件大于10M会重新生成一个文件
# logger.add("test.log", rotation="00:00")  # 每天0点创建新文件
# logger.add("test.log", rotation="1 week")  # 每过一周就会创建新文件
# logger.add("test.log", retention="5 days")  # 只保留最近五天的日志文件
# logger.add("test.log", compression="zip")  # 以zip格式对日志进行保存

# Loguru可以轻松地切换到异步模式，提高日志记录的性能
logger.add("async_log.log", level="INFO", enqueue=True)