from pipelines.training_pipeline import train_pipline
from steps.clean_data import clean_data
from steps.evaluation import evaluate_model
from steps.ingest_data import ingest_df
from steps.model_train import train_model
from zenml.client import Client

if __name__ == "__main__":
    #run the pipeline
    print(Client().active_stack.experiment_tracker.get_tracking_uri())
    train_pipline(data_path="D:\Runway\Projects\customer_satisfaction\data\olist_customers_dataset.csv")