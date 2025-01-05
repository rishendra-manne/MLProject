import os
import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from src.components.data_ingestion import DataIngestion
from src.exception import CustomException
from src.logger import logging
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from dataclasses import dataclass
from src.utils import save_object

@dataclass
class TransformationConfig:
    preprocessor_path=os.path.join("artifacts","preprocessor.pkl")


class DataTransform:

    def __init__(self):
        self.transform_config=TransformationConfig

    def transform_object(self):

        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            num_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="mean")),
                    ("scaler",StandardScaler())
                ]
            )
            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("encoding",OneHotEncoder()),
                    ("scaler",StandardScaler())
                ]

            )

            preprocessor =ColumnTransformer(
                [
                    ("num feature transformation",num_pipeline,numerical_columns),
                    ("cat feature transformation",cat_pipeline,categorical_columns)
                ]
            )
            return preprocessor

        except Exception as e:

            raise CustomException(e,sys)

    def initaiate_transformation(self,train_path,test_path):

        try:

            train_data=pd.read_csv(train_path)
            test_data=pd.read_csv(test_path)
            logging.info("data has been read")

            target_feature="math_score"

            train_input_data=train_data.drop(columns=[target_feature],axis=1)
            test_input_data=test_data.drop(columns=[target_feature],axis=1)

            train_target=train_data[target_feature]
            test_target=test_data[target_feature]

            preprocessor = self.transform_object()
            transformed_train_data=preprocessor.fit_transform(train_input_data)
            transformed_test_data=preprocessor.fit(test_input_data)
            logging.info("data transformed sucessfully")

            train_array = np.c_[
                    transformed_train_data,np.array(train_target)
                ]
            logging.info("train data array created")
            test_array=np.c_[
                transformed_test_data,np.array(test_target)

            ]
            logging.info("test data array created")

            save_object(
                obj=preprocessor,
                path=self.transform_config.preprocessor_path
                )
            return (
                train_array,
                test_array,
                self.transform_config.preprocessor_path
            )
        except Exception as e:
            raise CustomException(e,sys)


if __name__ =="__main__":
    data=DataIngestion()
    x,y=data.ingest(r"C:\Users\mrish\OneDrive\Documents\Churn_Modelling.csv")
    ob=DataTransform()
    ob.initaiate_transformation(train_path=x,test_path=y)