from utils.logger import log
from utils.exception import  handle_exception

import sys

try:
    log("Application started")
    x = 1 / 0
except Exception as e:
    handle_exception(e, sys)
