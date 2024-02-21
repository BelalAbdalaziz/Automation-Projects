import pytest
import logging


class LogGen:
  @staticmethod
  def loggen():
    logger=logging.getLogger()
    return logger

# Note
#logging.basicConfig(filename=".\\Logs\\automation.log",level=logging.INFO,                   
#                    format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#This Method with new update doesn't work with pytest cause it creat logger for it

# have to methods
# 1) By creat pytest.ini
#2) By write IN CLI
#>>pytest -v -s testCases\LoginTest.py --browser chrome  --log-file-level info 
#  --log-file-format="%(asctime)s %(levelname)s %(message)s" --log-file-date-format="%Y-%m-%d %H:%M:%S" --log-file Logs\automation.log


    

        