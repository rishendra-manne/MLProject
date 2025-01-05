import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Get traceback info
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get file name where error occurred
    error_message = (
        f"Error occurred in script: {file_name}, "
        f"line number: {exc_tb.tb_lineno}, "
        f"error message: {error}"
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message
