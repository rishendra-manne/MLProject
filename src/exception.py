import sys
from src.logger import logging

def error_message(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb.frame.f_code.co.filename
    error_message=f"error occured in the script name{file_name} line number{exc_tb.tb_lineno} error message {error}"
    return error_message



class custom_exception:
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message(error=error_message,error_detail=error_detail)
    def __str__(self):
        return error_message

