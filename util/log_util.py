import logging
from datetime import datetime
from util.global_var import *


dt = datetime.strftime(datetime.now(), "%Y_%m_%d")
logging.basicConfig(filename=PROJECT_ROOT_DIR + '/log/' + 'interface_auto_test_' + dt + '.log.',
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    level=logging.INFO,
                    filemode='a',
                    datefmt='%Y-%m-%d %H:%M:%S')


def info(message):
    logging.info(message)


def error(message):
    logging.error(message)


def warning(message):
    logging.warning(message)


def debug(message):
    logging.debug(message)


def critical(message):
    logging.critical(message)


if __name__ == "__main__":
    info("hippop")

