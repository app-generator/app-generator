Integrating Machine Learning Models with FastAPI
================================================

.. include::  /_templates/components/banner-top.rst


This document explains how to integrate a machine learning model into a FastAPI application. It includes a simple example to make it easy to understand. The goal is to create an API that receives input data, processes it through a pre-trained machine learning model, and returns predictions.

**Scenario:**
Let's consider a simple scenario where we want to predict whether a person has diabetes based on some medical features. We'll use a pre-trained machine learning model (for simplicity, we will use `scikit-learn`).

Steps:
 1. Train a simple machine learning model.
 2. Save the trained model to a file.
 3. Create a FastAPI app to serve predictions from the model.

Prerequisites
-------------
- Python 3.7+
- FastAPI
- Uvicorn (for running FastAPI)
- Scikit-learn
- Joblib (for saving and loading the model)

Install dependencies:
---------------------
.. code-block:: bash

    pip install fastapi[all] scikit-learn joblib uvicorn matplotlib

Step 1: Train a Simple Model
============================
We will start by training a simple machine learning model to predict whether a person has diabetes based on their medical features.

.. code-block:: python

    # train_model.py

    import joblib
    import matplotlib.pyplot as plt
    from sklearn.datasets import load_diabetes
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier

    # Load diabetes dataset
    diabetes_data = load_diabetes()

    # Visualize the distribution of the target variable
    plt.hist(diabetes_data.target, bins=50)
    plt.xlabel('Target Value')
    plt.ylabel('Frequency')
    plt.title('Distribution of Target Variable')
    plt.show()

    # Convert target into binary (1 = diabetic, 0 = not diabetic)
    y = diabetes_data.target > 100

    # Split into training and testing sets
    X = diabetes_data.data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a RandomForestClassifier
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save the trained model to a file
    joblib.dump(model, 'diabetes_model.joblib')

    print("Model trained and saved.")

Run this script to train and save the model:

.. code-block:: bash

    python train_model.py

Step 2: Create FastAPI Application
==================================
Now, we will create a FastAPI application that loads the saved model and exposes an endpoint to make predictions.

.. code-block:: python

    # main.py

    import joblib
    import numpy as np
    from fastapi import FastAPI
    from pydantic import BaseModel

    # Load the saved model
    model = joblib.load('diabetes_model.joblib')

    # Create FastAPI app
    app = FastAPI()


    # Define the input data structure
    class DiabetesFeatures(BaseModel):
        age: float
        sex: float
        bmi: float
        map: float
        tc: float
        ldl: float
        hdl: float
        tch: float
        ltg: float
        glu: float


    # Define a prediction endpoint
    @app.post("/predict/")
    def predict(features: DiabetesFeatures):
        # Convert input data to a numpy array
        input_data = np.array([[  # Convert input features to the appropriate format
            features.age,
            features.sex,
            features.bmi,
            features.map,
            features.tc,
            features.ldl,
            features.hdl,
            features.tch,
            features.ltg,
            features.glu
        ]])

        # Get the prediction probability (probability for "diabetic")
        prediction_prob = model.predict_proba(input_data)

        # Set a threshold for predicting 'Diabetic' (e.g., 0.6 probability for being diabetic)
        threshold = 0.6
        is_diabetic = prediction_prob[0][1] > threshold  # Use the second column for the probability of class '1'

        # Return the result based on probability threshold
        return {"prediction": "Diabetic" if is_diabetic else "Not Diabetic"}


Step 3: Run the FastAPI Server
=============================
To start the FastAPI server, use `uvicorn`:

.. code-block:: bash

    uvicorn main:app --reload

Step 4: Test the API
====================
Once the server is running, you can test the API using `curl` or through an interactive UI at `http://127.0.0.1:8000/docs`.

Example `curl` request:

.. code-block:: bash

    curl -X 'POST' \
      'http://127.0.0.1:8000/predict/' \
      -H 'Content-Type: application/json' \
      -d '{
      "age": 50.0,
      "sex": 1.0,
      "bmi": 25.0,
      "map": 92.0,
      "tc": 220.0,
      "ldl": 120.0,
      "hdl": 50.0,
      "tch": 70.0,
      "ltg": 3.5,
      "glu": 90.0
    }'

Expected Response:

.. code-block:: json

    {
      "prediction": "Not Diabetic"
    }

Conclusion
----------
In this guide demonstrates how to integrate a machine learning model with FastAPI. The key steps were:
 1. Train and save a machine learning model.
 2. Load the model in a FastAPI application.
 3. Expose an endpoint to make predictions based on input data.


.. include::  /_templates/components/footer-links.rst
