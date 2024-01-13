import logging
from numpy import divide
import pandas as pd
from zenml import step
from typing import Tuple
from typing_extensions import Annotated

from src.customer_satisfaction.data_cleaning import (DataCleaning,
                                                     DataDivideStrategy,
                                                     DataPreProcessingStrategy,
                                                    )

@step
def clean_data(df: pd.DataFrame) ->Tuple [
    Annotated[pd.DataFrame, "x_train"],
    Annotated[pd.DataFrame, "x_test"],
    Annotated[pd.Series, "y_train"],
    Annotated[pd.Series, "y_test"],
]:
    """
    Data cleaning class which preprocesses the data and divides it into train and test data.

    Args:
        data: pd.DataFrame
    """
    try:
        process_strategy = DataPreProcessingStrategy()
        data_cleaning = DataCleaning(df,process_strategy)
        processed_data =data_cleaning.handle_data()

        divide_strategy = DataDivideStrategy()
        data_cleaning = DataCleaning(processed_data,divide_strategy)
        
        X_train, X_test, y_train, y_test = data_cleaning.handle_data()
        logging.info("data creaning and data divede completed")
        return X_train, X_test, y_train, y_test
    
    except Exception as e:
        logging.error("error in cleaning:{}".format(e))
        raise e