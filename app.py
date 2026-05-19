from flask import Flask, render_template, request, jsonify
from ml_classifier import classifier
from fuzzy_module import calculate_emotional_severity
from inference_engine import evaluate_student
import os

# Set template and static folders explicitly to avoid path issues
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static'))

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    
    # 1. Parse Inputs
    attendance = float(data.get('attendance', 100))
    grades_drop = data.get('grades_drop') == True
    study_hours = float(data.get('study_hours', 5))
    sleep_hours = float(data.get('sleep_hours', 8))
    social_media = float(data.get('social_media', 2))
    financial_stress = float(data.get('financial_stress', 1))
    survey_stress = float(data.get('survey_stress', 0))
    survey_isolation = float(data.get('survey_isolation', 0))
    
    # 2. ML Prediction
    ml_pred = classifier.predict_risk(study_hours, sleep_hours, social_media, financial_stress)
    
    # 3. Fuzzy Logic
    fuzzy_score = calculate_emotional_severity(survey_stress, survey_isolation)
    
    # 4. Inference Engine
    result = evaluate_student(attendance, grades_drop, fuzzy_score, ml_pred)
    
    return jsonify({
        "ml_prediction": "Needs Intervention" if ml_pred == 1 else "Normal",
        "fuzzy_score": fuzzy_score,
        "risk_level": result["risk_level"],
        "recommendation": result["recommendation"]
    })

if __name__ == '__main__':
    app.run(debug=True)
