import logging
from datetime import datetime
import os

# Define log file path
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_DIR = os.path.join(os.getcwd(), 'log')  # Define directory for logs
os.makedirs(LOG_DIR, exist_ok=True)  # Create the directory if it doesn't exist
log_file_path = os.path.join(LOG_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Confirm logger setup
logging.info("Logger has been initialized.")
