import os
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

DATA_PATH = os.path.join(os.path.dirname(__file__), 'synthetic_survey.csv')

def generate_synthetic_data():
    """Generates synthetic student survey data if it doesn't exist."""
    np.random.seed(42)
    n_samples = 500
    
    # Features
    study_hours = np.random.randint(0, 10, n_samples)
    sleep_hours = np.random.randint(3, 10, n_samples)
    social_media_hours = np.random.randint(1, 8, n_samples)
    financial_stress = np.random.randint(1, 10, n_samples)
    
    # Target (Needs Intervention)
    # Simple logic to generate somewhat realistic labels
    needs_intervention = []
    for i in range(n_samples):
        score = 0
        if sleep_hours[i] < 6: score += 2
        if social_media_hours[i] > 5: score += 1
        if financial_stress[i] > 7: score += 2
        if study_hours[i] > 7 or study_hours[i] < 2: score += 1
        
        needs_intervention.append(1 if score >= 4 else 0)
        
    df = pd.DataFrame({
        'study_hours': study_hours,
        'sleep_hours': sleep_hours,
        'social_media_hours': social_media_hours,
        'financial_stress': financial_stress,
        'needs_intervention': needs_intervention
    })
    
    df.to_csv(DATA_PATH, index=False)
    return df

class MentalHealthClassifier:
    def __init__(self):
        self.model = DecisionTreeClassifier(random_state=42, max_depth=5)
        
        if not os.path.exists(DATA_PATH):
            df = generate_synthetic_data()
        else:
            df = pd.read_csv(DATA_PATH)
            
        X = df[['study_hours', 'sleep_hours', 'social_media_hours', 'financial_stress']]
        y = df['needs_intervention']
        
        self.model.fit(X, y)
        
    def predict_risk(self, study_hours, sleep_hours, social_media_hours, financial_stress):
        """Predicts if a student needs intervention (1) or not (0)."""
        prediction = self.model.predict([[study_hours, sleep_hours, social_media_hours, financial_stress]])
        return int(prediction[0])

# Initialize global classifier instance
classifier = MentalHealthClassifier()
