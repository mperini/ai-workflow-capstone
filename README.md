# IBM AI Enterprise Workflow Capstone Project
This repository contains the code for the IBM AI Enterprise Workflow final project. Objective of the project is to create a revenue forecast machine learning model, which 
predicts the total forecast for a chosen country given past revenue data.
## Project Structure
    .
    ├── cs-production       # Validation data
    ├── cs-train            # Training data
    ├── notebooks           # Jupyter notebooks for data/modeling exploration
    ├── src                 # Source files
    ├── unittests           # Unit tests

## Usage
To set up the API:

`python app.py`

To run model training and prediction:

`python model.py`

To run model unit tests:

`python ModelTests.py`

To run API unit tests:

`python ApiTests.py`