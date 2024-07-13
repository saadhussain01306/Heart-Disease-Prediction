from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('heart_disease.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    input_data = np.array(input_features).reshape(1, -1)
    
    prediction = model.predict(input_data)
    
    if prediction[0] == 0:
        result = 'The Person does not have Heart Disease'
    else:
        result = 'The Person has Heart Disease'
    
    return render_template('result.html', prediction_text=result)

# if __name__ == "__main__":
#     app.run(debug=True)
