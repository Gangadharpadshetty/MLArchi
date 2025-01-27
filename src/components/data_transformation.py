import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer

from sklearn.impute import SimpleImputer
frm sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import PowerTransformer
from sklearn.preprocessing import FunctionTransformer

from src.exceptions import CustomException
from src.logger import logging
import os


@dataclass
class DataTrasformationConfig:
       preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
       def __init__(self):
              self.data_transformation_config=DataTrasformationConfig()
       def get_data_transformer_object(self):
              try:
                     numerical_columns=["writing_score","reading_score"]
                     categorical_columns=[
                            "gender",
                            "race_ethnicity",
                            "parental_level_of_education",
                            "lunch",
                            "test_preparation_course"
                     ]
                     numerical_pipeline=Pipeline([
                            ("imputer",SimpleImputer(strategy="median")),
                            ("scaler",StandardScaler())
                     ])
                   
                     cat_pipeline=pipeline(
                            steps=[
                                   ("imputer",SimpleImputer(strategy="most_frequent")),
                                   ("encoder",OneHotEncoder())
                                   ("scaler",StandardScaler())

                            ]
                     )
                     logging.info("Column transformer initiated")
                     logging.info("Numerical pipeline initiated")
                     logging.info("Categorical pipeline initiated")
                     preprocessor=ColumnTransformer(
                            transformers=[
                                   ("numerical_pipeline",numerical_pipeline,numerical_columns),
                                   ("cat_pipeline",cat_pipeline,categorical_columns)
                            ]
                     )
                     return preprocessor


              except exception as e:
                     raise CustomException(e,sys)

       def initiate_data_transformation(self,train_path,test_path):
              try:
                     logging.info("Data transformation initiated")
                     train_df=pd.read_csv(train_path)
                     test_df=pd.read_csv(test_path)
                     preprocessor_obj=self.get_data_transformer_object()
                     logging.info("Data transformation completed")
                     logging.info("Saving the preprocessor object")

                     input_feature_train_df=train_df.drop("math_score",axis=1)
                     save_object
                     (file_path=self.data_transformation_conf,
                     obj=preprocessor_obj)
                      
                     
              except Exception as e:
                     raise CustomException(e,sys)


