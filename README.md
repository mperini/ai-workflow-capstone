# IBM AI Enterprise Workflow Capstone Project
This repository contains the code for the IBM AI Enterprise Workflow final project. Objective of the project is to create a revenue forecast machine learning model, which 
predicts the total forecast for a chosen country given past revenue data.
## Project Structure
    .
    ├── cs-production       # Validation data
    ├── cs-train            # Training data
    ├── notebooks           # Jupyter notebooks for data/modeling exploration
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