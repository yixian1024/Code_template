# utility.py
import os
import shutil
import logging

REDUNDENT = ['.git', '.gitattributes', 'README.md', 'MD5']
logger = logging.getLogger(__name__)


def move(source, target):
    
    # move files from source to target
    try:
        list = os.listdir(source)
        for file in list:
            if file not in REDUNDENT:
                file_path = os.path.join(source, file)
                logging.info(f'Copy {file}')
                shutil.move(file_path, target)
        shutil.rmtree(source)
    except Exception as e:
        logging.warning(f'Can not move file from {source} to {target}')
        raise e

class CustomFormatter(logging.Formatter):
    
    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    cri_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    err_fmt = "%(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    info_fmt = "%(message)s"
    debug_fmt = "%(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + debug_fmt + reset,
        logging.INFO: grey + info_fmt + reset,
        logging.WARNING: yellow + err_fmt + reset,
        logging.ERROR: red + err_fmt + reset,
        logging.CRITICAL: bold_red + cri_fmt + reset
    }

    def format(self, record):
        
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def set_logger_level():
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(CustomFormatter())
    logger.addHandler(ch)