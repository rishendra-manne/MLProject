import os
import sys

import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object

from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    model_path=os.path.join("artifacts",'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_config=ModelTrainerConfig()

    def initiate_model(self,train,test):

        try:

            logging.info("splitting the data into train and target")

            x_train,y_train,x_test,y_test=(
                train[:,:-1],
                train[:,-1],
                test[:,:-1],
                test[:,-1]

                )
            model=XGBRegressor()
            params={'learning_rate':[.1,.01,.05,.001],
                        'n_estimators': [8,16,32,64,128,256]}
            grid_search=GridSearchCV(model,params,cv=3,scoring="r2")
            grid_search.fit(x_train,y_train)
            logging.info("best params found")

            logging.info("model training started")
            model.set_params(**grid_search.best_params_)
            model.fit(x_train,y_train)
            logging.info("model training finished")

            predictions=model.predict(x_test)
            model_score=r2_score(y_test,predictions)

            save_object(
                obj=model,
                path=self.model_config.model_path

                        )
            logging.info("model saved")
            return model_score

        except Exception as e:
            raise CustomException(e,sys)



