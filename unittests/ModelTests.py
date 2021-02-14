#!/usr/bin/env python
import unittest
from model import *

results_dir = "../results"
train_dir = "../cs-train"
data_dir = "../cs-production"


class ModelTest(unittest.TestCase):
    """
    Test main model API commands
    """

    def test_01_train(self):
        """
        Test model training
        """
        data_df = fetch_data(train_dir)

        ## train the model
        train_model(data_df)
        self.assertTrue(os.path.exists(os.path.join(results_dir, "models")))

    def test_02_load(self):
        """
        Test model loading
        """

        ## load the model
        all_data, all_models = load_model(os.path.join(results_dir, "models"), "AdaBoostRegressor", "EIRE")
        self.assertTrue(all_data)
        self.assertTrue(all_models)

    def test_03_predict(self):
        """
        Test model predicting
        """

        ## load model first
        country = 'EIRE'
        result1 = model_predict(data_dir, country, "2018-01-01")
        result2 = model_predict(country, "2019-01-01")
        result_list = [result1, result2]
        for result in result_list:
            self.assertTrue(result)


### Run the tests
if __name__ == '__main__':
    unittest.main()