import logging


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('[%(name)s] - %(levelname)s: %(message)s')

    if not logger.handlers:
        # 日志输出到屏幕
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger