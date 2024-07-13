# Heart Disease Prediction Project

## Project Overview

This project involves building a heart disease prediction model using Logistic Regression and deploying it as a web application using Flask. The project includes data preprocessing, model training, and making predictions based on new input data.

## Directory Structure

```
Heart_Disease_Prediction_Project/
│
├── app.py
├── static/
│   └── styles.css
├── templates/
│   ├── index.html
│   └── result.html
├── Heart_disease_prediction.ipynb
├── heart_disease.pkl
├── heart_disease_data.csv
├── requirements.txt
└── README.md
```

## Files Description

- **app.py**: The Flask application file that handles the routing and model predictions.
- **static/styles.css**: The CSS file for styling the HTML pages.
- **templates/index.html**: The home page where users can input their data.
- **templates/result.html**: The page displaying the prediction results.
- **Heart_disease_prediction.ipynb**: Jupyter Notebook containing the data preprocessing, model training, and prediction code.
- **heart_disease.pkl**: The serialized Logistic Regression model.
- **heart_disease_data.csv**: The dataset used for training the model.
- **requirements.txt**: List of dependencies required to run the project.

## Steps to Build the Model

1. **Collect Data**:
   - The dataset (`heart_disease_data.csv`) contains the necessary data for training the model.

2. **Data Preprocessing**:
   - Load the data into a Pandas DataFrame.
   - Separate the features and target variable.

3. **Train-Test Split**:
   - Split the data into training and testing sets.

4. **Logistic Regression Model**:
   - Train a Logistic Regression model using the training data.

5. **Trained Logistic Model**:
   - Evaluate the model's performance on both training and test data.
   - Serialize the trained model using `pickle` for later use in the Flask app.

6. **Prediction for New Data**:
   - Predict whether a new set of input data indicates heart disease.

## User Input Attributes

The web application takes the following attributes as user inputs to predict if a person has heart disease:

1. **Age**: Age of the person
2. **Sex**: Gender of the person (1 = male, 0 = female)
3. **CP**: Chest pain type (0, 1, 2, or 3)
4. **Trestbps**: Resting blood pressure (in mm Hg)
5. **Chol**: Serum cholesterol (in mg/dl)
6. **FBS**: Fasting blood sugar (1 if > 120 mg/dl, 0 otherwise)
7. **Restecg**: Resting electrocardiographic results (0, 1, or 2)
8. **Thalach**: Maximum heart rate achieved
9. **Exang**: Exercise-induced angina (1 = yes, 0 = no)
10. **Oldpeak**: ST depression induced by exercise relative to rest
11. **Slope**: Slope of the peak exercise ST segment (0, 1, or 2)
12. **Ca**: Number of major vessels (0-3) colored by fluoroscopy
13. **Thal**: Thalassemia (0 = normal, 1 = fixed defect, 2 = reversible defect)

## Usage Instructions

### Setting Up the Environment

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/saadhussain01306/Heart-Disease-Prediction.git
   cd Heart-Disease-Prediction
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask App**:
   ```bash
   python app.py
   ```

### Web Application

1. **Home Page (index.html)**:
   - Input the required data for prediction.

2. **Result Page (result.html)**:
   - Display the prediction result indicating whether the person has heart disease or not.

## Interface

![Screenshot 2024-07-14 002659](https://github.com/user-attachments/assets/c7d57cb0-6751-40ba-84e2-5fdba5e341b3)

![Screenshot 2024-07-14 002739](https://github.com/user-attachments/assets/d84e70fb-4a75-43b6-8e39-a66a61565ada)

