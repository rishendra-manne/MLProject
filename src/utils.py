import pickle
import numpy as np
import pandas as pd

import os
import sys
from src.exception import CustomException

def save_object(obj,path):
    try:
        dir_path=os.path.dirname(path)
        os.makedirs(dir_path,exist_ok=True)

        with open(path,'wb') as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
