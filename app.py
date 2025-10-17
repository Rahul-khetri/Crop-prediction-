from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get form input
#         features = [float(request.form[f]) for f in ['Nitrogen', 'Phosphorus', 'Potassium', 'temperature', 'humidity', 'ph', 'rainfall']]
#         prediction = model.predict([features])[0]
#         return render_template('result.html', prediction=prediction)
#     except Exception as e:
#         return render_template('result.html', prediction=f"Error: {e}")


# ...existing code...
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # use the same input names as in templates/index.html
        fields = ['Nitrogen', 'Phosphorus', 'Potassium', 'Temperature', 'Humidity', 'pH', 'Rainfall']
        values = []
        for f in fields:
            v = request.form.get(f)
            if v is None or v.strip() == '':
                return render_template('result.html', prediction=f"Error: missing field '{f}'")
            values.append(float(v))
        # arrange features in the order your model expects (N,P,K,temperature,humidity,ph,rainfall)
        features = [values[0], values[1], values[2], values[3], values[4], values[5], values[6]]
        prediction = model.predict([features])[0]
        return render_template('result.html', prediction=prediction)
    except Exception as e:
        return render_template('result.html', prediction=f"Error: {e}")
# ...existing code...
if __name__ == '__main__':
    app.run(debug=True)
