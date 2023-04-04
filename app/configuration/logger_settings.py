import logging
from logging.handlers import RotatingFileHandler

from app.pkg.settings import settings

log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

logFile = f'{settings.FILE_NAME}.log'

my_handler = RotatingFileHandler(
    filename=logFile,
    mode='a',
    maxBytes=10*1024*1024,
    backupCount=3,
    encoding=None,
    delay=False
)

my_handler.setFormatter(log_formatter)
my_handler.setLevel(settings.LEVEL)

app_log = logging.getLogger('BUILD_LOGGER')
app_log.setLevel(settings.LEVEL)

app_log.addHandler(my_handler)

app_log = app_log
