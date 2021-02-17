# IBM AI Enterprise Workflow Capstone Project
This repository contains the code for the IBM AI Enterprise Workflow final project. Objective of the project is to create a revenue forecast machine learning model, which 
predicts the total forecast for a chosen country given past revenue data.
## Project Structure
    .
    ├── cs-production       # Validation data
    ├── cs-train            # Training data
    ├── notebooks           # Jupyter notebooks for data/modeling exploration
    ├── results/models      # Results folder    
    ├── src                 # Source files
    ├── test                # Unit tests
    Dockerfile
    README.md
    requirements.txt
    run_all_tests.py

## Usage
To set up the API:

`python app.py`

To run model training and prediction:

`python model.py`

To run all tests together:

`python -m unittest discover`

To run model unit tests:

`python test/test_Model.py`

To run API unit tests:

`python test/test_Api.py`

To run logging unit tests:

`python test/test_Logging.py`

## For evaluation
- __Are there unit tests for the API?__ `test_Api.py`
- __Are there unit tests for the model?__ `test_Model.py`
- __Are there unit tests for the logging?__ `test_Logging.py`
- __Can all of the unit tests be run with a single script and do all of the unit tests pass?__
Run `python -m unittest discover`
- __Is there a mechanism to monitor performance?__ Performance can be assessed from logs
- __Was there an attempt to isolate the read/write unit tests from production models and logs?__ 
Selection mechanism via the `test` flag
- __Does the API work as expected? For example, can you get predictions for a specific country as well as for all countries combined?__
  See test cases 3 to 5 in `test_Api.py`
- __Does the data ingestion exists as a function or script to facilitate automation?__ `preparation.py`
- __Were multiple models compared?__ See `Modeling.ipynb`
- __Did the EDA investigation use visualizations?__ See `Data prep.ipynb`
- __Is everything containerized within a working Docker image?__ See `Dockerfile`
- __Did they use a visualization to compare their model to the baseline model?__ See `Modeling.ipynb`

