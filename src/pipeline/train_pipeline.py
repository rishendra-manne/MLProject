import os
import sys
import pandas as pd
import numpy as np

from src.components.data_transformation import DataTransform
from src.components.model_trainer import ModelTrainer
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from dataclasses import dataclass

class TrainingPipeline:
    def __init__(self):

        self.data = DataIngestion()
        self.scaler= DataTransform()
        self.trainer=ModelTrainer()

    def train_model(self):

        try:
            train_path,test_path=self.data.ingest(r"C:\Users\mrish\OneDrive\Documents\Churn_Modelling.csv")
            logging.info("data ingestion completed")

            train_array,test_array,_=self.scaler.initaiate_transformation(train_path=train_path,test_path=test_path)
            logging.info("data transformation completed")
            logging.info("model training started")

            model_score=self.trainer.initiate_model(train_array,test_array)
            logging.info("model training and testing has finished")

            return model_score

        except Exception as e:

            raise CustomException(e,sys)
if __name__=="__main__":
    model_train=TrainingPipeline()
    score=model_train.train_model()
    print(score)