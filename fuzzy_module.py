import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def calculate_emotional_severity(stress_score, isolation_score):
    """
    Uses fuzzy logic to calculate emotional severity.
    Inputs:
    - stress_score (0-100)
    - isolation_score (0-100)
    Returns:
    - severity_score (0-100)
    """
    # 1. Define Fuzzy Variables
    stress = ctrl.Antecedent(np.arange(0, 101, 1), 'stress')
    isolation = ctrl.Antecedent(np.arange(0, 101, 1), 'isolation')
    severity = ctrl.Consequent(np.arange(0, 101, 1), 'severity')

    # 2. Define Fuzzy Sets (Membership Functions)
    stress.automf(3, names=['low', 'moderate', 'high'])
    isolation.automf(3, names=['low', 'moderate', 'high'])
    
    severity['mild'] = fuzz.trimf(severity.universe, [0, 0, 50])
    severity['concerning'] = fuzz.trimf(severity.universe, [20, 50, 80])
    severity['critical'] = fuzz.trimf(severity.universe, [50, 100, 100])

    # 3. Define Fuzzy Rules
    rule1 = ctrl.Rule(stress['low'] & isolation['low'], severity['mild'])
    rule2 = ctrl.Rule(stress['moderate'] | isolation['moderate'], severity['concerning'])
    rule3 = ctrl.Rule(stress['high'] & isolation['high'], severity['critical'])
    rule4 = ctrl.Rule(stress['high'] & isolation['low'], severity['concerning'])
    rule5 = ctrl.Rule(stress['low'] & isolation['high'], severity['concerning'])

    # 4. Create Control System
    severity_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    severity_sim = ctrl.ControlSystemSimulation(severity_ctrl)

    # 5. Calculate Result
    severity_sim.input['stress'] = stress_score
    severity_sim.input['isolation'] = isolation_score
    
    try:
        severity_sim.compute()
        return round(severity_sim.output['severity'], 2)
    except:
        return 0.0
