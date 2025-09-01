import os
import sys
import logging


logging_str='%(asctime)s - %(levelname)s - %(module)s - %(message)s'

log_dr="logs"
filepath=os.path.join(log_dr, 'running_logs.log')
os.makedirs(log_dr, exist_ok=True)

logging.basicConfig(level=logging.INFO, format=logging_str, handlers=[
    logging.FileHandler(filepath),logging.StreamHandler(sys.stdout)
])
logger=logging.getLogger("my_project")