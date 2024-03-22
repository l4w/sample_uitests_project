from loguru import logger

logger.add('logs/log_{time:YYYY_MM_DD}.log',
           format='{time:YYYY-MM-DD at HH:mm:ss}, {level}: {message}',
           level='INFO',
           retention=1)
