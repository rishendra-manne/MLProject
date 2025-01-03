import logging
from datetime import datetime
import os
from os.path import exists

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),'log',LOG_FILE)
os.makedirs(log_path,exist_ok=True)
log_file_path=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO,

)