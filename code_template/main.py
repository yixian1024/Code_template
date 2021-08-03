# bundle_manager.py
import os
from shutil import rmtree
import logging
from tempfile import mkdtemp
import argparse
from pathlib import Path
from dotenv import load_dotenv

from utility import  set_logger_level
from parser import OBJ

ROOTDIR = os.path.abspath(Path(__file__).parent.parent)
TMPDIR = mkdtemp()


def initialize():

    try:
        # read arguments
        p = argparse.ArgumentParser(description="Please enter argument")
        p.add_argument('-f', '--file',
                        dest="f",
                        help='Path of YAML file',
                        required=True, type=Path)
        p.add_argument('-e', '--environment',
                        dest="env",
                        help='Path of environment file .env',
                        required=True, type=Path)
        args = p.parse_args()

        # create directory
        os.makedirs(TMPDIR)
        logging.info('Temp directory: %s', TMPDIR)

        # load environment
        load_dotenv(args.env)

        # set logger
        set_logger_level()

        return args
    except Exception as e:
        logging.error(f'Fail to initialized: {e}')
        raise e


def read_file(file_path):

    try:
        # parse user yaml file
        ir = OBJ(file_path)
        return ir
    except Exception as e:
        raise e



def main():

    try:
        args = initialize()
        ir = read_file(args.f)
        
    except Exception as e:
        logging.error(e)
    finally:
        rmtree(TMPDIR)


if __name__ == '__main__':
    main()