from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__, static_folder='static')

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
    data = request.get_json(force=True)
    features = [
        data['Course'], data['Daytime/evening attendance'], data['Previous qualification'],
        data['Previous qualification (grade)'], data['Admission grade'],
        data['Educational special needs'], data['Tuition fees up to date'], data['Gender'],
        data['Scholarship holder'], data['Age at enrollment'],
        data['Curricular units 1st sem (credited)'],
        data['Curricular units 1st sem (enrolled)'],
        data['Curricular units 1st sem (evaluations)'],
        data['Curricular units 1st sem (approved)'],
        data['Curricular units 1st sem (grade)'],
        data['Curricular units 1st sem (without evaluations)'],
        data['Curricular units 2nd sem (credited)'],
        data['Curricular units 2nd sem (enrolled)'],
        data['Curricular units 2nd sem (evaluations)'],
        data['Curricular units 2nd sem (approved)'],
        data['Curricular units 2nd sem (grade)'],
        data['Curricular units 2nd sem (without evaluations)']
    ]
    print(features)

    prediction = model.predict([features])
    return jsonify({"prediction: ": prediction.tolist()})

if __name__ == "__main__":
    app.run(debug=True)