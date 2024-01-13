import logging
import pandas as pd
from zenml import step
from src.customer_satisfaction.evaluation import (RMSE,R2Score,MSE)
from sklearn.base import RegressorMixin
from typing import Tuple
from typing_extensions import Annotated
import mlflow


@step
def evaluate_model(
    model: RegressorMixin, X_test: pd.DataFrame, y_test: pd.Series
) -> Tuple[
    Annotated[float, "r2_score"],
    Annotated[float,"rmse"]
]:
    try:
        prediction = model.predict(X_test)
        
        mse_class = MSE()
        mse = mse_class.calculate_score(y_test, prediction)
        mlflow.log_metric("mse", mse)

        # Using the R2Score class for R2 score calculation
        r2_class = R2Score()
        r2_score = r2_class.calculate_score(y_test, prediction)
        mlflow.log_metric("r2_score", r2_score)

        # Using the RMSE class for root mean squared error calculation
        rmse_class = RMSE()
        rmse = rmse_class.calculate_score(y_test, prediction)
        mlflow.log_metric("rmse", rmse)
            
        return r2_score, rmse
    except Exception as e:
        logging.error("Error in evaluting model{}".format(e))
        raise e
