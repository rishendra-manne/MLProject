import os

import pandas as pd
import sys
from src.exception import custom_exception
from src.logger import logging

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataConfig:
    train_data_path :str=os.path.join("artifacts","train.csv")
    test_data_path :str =os.path.join("artifacts","test.csv")
    raw_data_path :str =os.path.join("artifacts","raw.csv")


class DataIngestion:
    def __init__(self):
        self.config=DataConfig()

    def ingest(self,data_path):
        logging.info("starting the data ingestion")
        try:
            data_frame=pd.read_csv(data_path)
            logging.info("data has been read into the memory")

            os.makedirs(os.path.dirname(self.config.train_data_path),exist_ok=True)
            logging.info("created data directory")

            data_frame.to_csv(self.config.raw_data_path,header=True,index=False)

            logging.info("train test split initiated")
            train,test=train_test_split(data_frame,test_size=0.2,random_state=42)

            train.to_csv(self.config.train_data_path,index=False,header=True)
            logging.info("train data saved sucessfully")

            test.to_csv(self.config.test_data_path,index=False,header=True)
            logging.info("test data saved sucessfully")

            return (
                self.config.train_data_path,
                self.config.test_data_path
            )
        except Exception as e:
            raise custom_exception(e,sys)


if __name__ =="__main__":
    data=DataIngestion()
    data.ingest(r"C:\Users\mrish\OneDrive\Documents\Churn_Modelling.csv")