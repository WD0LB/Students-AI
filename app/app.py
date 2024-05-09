from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

#load the model
with open('/home/hb/projects/Students-AI/app/grid_search_rfc.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

#define the prediction end point
@app.route('/predict', methods=['POST'])
def predict():
    # Assuming form data is used instead of JSON
    try:
        features = [
            int(request.form['Course']),
            int(request.form['Daytime/evening attendance']),
            int(request.form['Previous qualification']),
            float(request.form['Previous qualification (grade)']),
            float(request.form['Admission grade']),
            int(request.form['Educational special needs']),
            int(request.form['Tuition fees up to date']),
            int(request.form['Gender']),
            int(request.form['Scholarship holder']),
            int(request.form['Age at enrollment']),
            int(request.form['Curricular units 1st sem (credited)']),
            int(request.form['Curricular units 1st sem (enrolled)']),
            int(request.form['Curricular units 1st sem (evaluations)']),
            int(request.form['Curricular units 1st sem (approved)']),
            float(request.form['Curricular units 1st sem (grade)']),
            int(request.form['Curricular units 1st sem (without evaluations)']),
            int(request.form['Curricular units 2nd sem (credited)']),
            int(request.form['Curricular units 2nd sem (enrolled)']),
            int(request.form['Curricular units 2nd sem (evaluations)']),
            int(request.form['Curricular units 2nd sem (approved)']),
            float(request.form['Curricular units 2nd sem (grade)']),
            int(request.form['Curricular units 2nd sem (without evaluations)'])
        ]
        
        prediction = model.predict([features])
        # Redirect to the results page with prediction result
        return redirect(url_for('result', prediction=prediction[0]))

    except Exception as e:
        return str(e)  # For debugging purposes
    
@app.route('/result')
def result():
    prediction = request.args.get('prediction', type=str)  # Retrieve the prediction from query parameters
    return render_template('result.html', prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)