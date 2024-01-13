import logging
from abc import ABC, abstractmethod
from sklearn.linear_model import LinearRegression

class Model(ABC):
    """
    Abstract base class for all models.
    """
    @abstractmethod
    def train(self, X_train, y_train):
        """
        Trains the model on the given data.

        Args:
            X_train: Training data
            y_train: Target data
        """
        pass

    
class LinearRegressionModel(Model):
    """
    LinearRegressionModel that implements the Model interface.
    """

    def train(self, X_train, y_train, **kwargs):
        try:
            reg = LinearRegression(**kwargs)
            reg.fit(X_train, y_train)
            logging.info("Model training completed")
            return reg
        except Exception as e:
            logging.error("Error in training{}".format(e))
            raise e

    # For linear regression, there might not be hyperparameters that we want to tune, so we can simply return the score
    #def optimize(self, trial, X_train, y_train, X_test, y_test):
    #    reg = self.train(X_train, y_train)
    #    return reg.score(X_test, y_test)    