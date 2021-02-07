import pandas as pd
import os
import joblib
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor, AdaBoostRegressor
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PowerTransformer
from preparation import fetch_data

data_dir = "../cs_train"
model_dir = "../results/models"
non_feature_cols = ["date", "Price", "Country", "target"]
model_name = "AdaBoostRegressor"


def load_model(model_dir, model_name, country):
    """
    Load model according to given name and country
    """
    return joblib.load(os.path.join(model_dir, country+"_"+model_name))


def train_model_impl(df):
    """
    Actual implementation of training
    """
    X = df.loc[:, df.columns not in non_feature_cols]
    y = df["target"]

    X_train, X_valid, y_train, y_valid = train_test_split(X, y)

    pipe = Pipeline(steps=[("power_transf", PowerTransformer()),
                           ("model", AdaBoostRegressor())])
    pipe.fit(X_train, y_train)
    return pipe


def model_predict(data_dir, country, date):
    """
    Predict revenue for the 30 days following given date for the given country
    """
    date = pd.to_datetime(date)
    data_df = fetch_data(data_dir)
    if country not in data_df["Country"]:
        raise ValueError("Country " + country + " is not in provided data.")

    if date not in data_df["date"]:
        raise ValueError("Date " + str(date) + " not in provided data.")

    # retrieve data
    X = data_df.loc[:, data_df.columns not in non_feature_cols]
    X = X.loc[X["date"] < date, :]

    # retrieve model
    model = load_model(model_dir, model_name, country)

    return model.predict(X)


def train_model(df):
    """
    Perform training separately for each country in df
    """

    for country in df["Country"].unique():
        print("Training for " + country)
        trained_pipe = train_model_impl(df.loc[df["Country"]==country, :])
        joblib.dump(trained_pipe, os.path.join(model_dir, country+"_"+type(trained_pipe["model"].__name__)))


if __name__ == "main":
    # fetch data
    data_df = fetch_data(data_dir)

    # train API endpoint
    print("Training models.")
    train_model(data_df)

    # predict API endpoint
    date = "2019-07-01"
    country = "EIRE"
    print("Prediction for date: " + date + " and country " + country)
    y_pred = model_predict(data_dir, country, date)
    print("Predicted revenue: " + y_pred)