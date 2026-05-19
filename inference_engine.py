def evaluate_student(attendance, grades_drop, fuzzy_score, ml_prediction):
    """
    Inference Engine using Forward Chaining.
    Takes observable inputs, fuzzy output, and ML prediction to determine final risk and recommendation.
    """
    risk_level = "Low"
    recommendation = "No action needed. Regular monitoring."

    # Rules Engine
    if fuzzy_score > 70 or ml_prediction == 1:
        if attendance < 80 and grades_drop:
            risk_level = "Critical"
            recommendation = "Immediate Crisis Intervention and Parent/Guardian Contact."
        elif attendance < 90:
            risk_level = "High"
            recommendation = "Schedule Urgent One-on-One Counseling Session."
        else:
            risk_level = "High"
            recommendation = "Schedule One-on-One Counseling Check-in."
    elif fuzzy_score > 40:
        if attendance < 90 or grades_drop:
            risk_level = "Moderate"
            recommendation = "Refer to Academic Advisor and Peer Support Group."
        else:
            risk_level = "Moderate"
            recommendation = "Send Check-in Email with Wellness Resources."
    else:
        if attendance < 85 or grades_drop:
            risk_level = "Low-Moderate"
            recommendation = "Academic check-in to investigate performance."

    return {
        "risk_level": risk_level,
        "recommendation": recommendation
    }
