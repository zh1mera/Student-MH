# Intelligent Student Mental Health System (HealthSync)

## 1. What is it about?
The **Student Mental Health System** (HealthSync) is an intelligent early detection and support routing system. It is designed to proactively monitor student well-being by analyzing academic performance (like attendance and grades), lifestyle behaviors, and self-reported emotional states. Its primary goal is to identify at-risk students before a crisis occurs and connect them with appropriate school counseling interventions in a sensitive, ethical, and privacy-conscious manner.

### Alignment with UN Sustainable Development Goals (SDGs)
This system directly addresses two major global goals:
*   **SDG 3 (Good Health and Well-Being):** By creating a proactive detection mechanism, the system monitors mental health indicators early and routes students to professional help, aiming to reduce the severity of mental health crises among the student body.
*   **SDG 4 (Quality Education):** Mental health is critical to academic success. By intervening early when students exhibit burnout, stress, or anxiety, the system helps prevent absenteeism and dropouts, ensuring students are mentally equipped to stay in school and succeed.

## 2. What are the Functions and Components?
The system operates as a Web Application built with Python (Flask) and consists of four main intelligent components:

1.  **Machine Learning Classifier (`ml_classifier.py`)**: 
    *   **Function**: Uses Supervised Learning (Decision Tree) to classify if a student needs intervention based on lifestyle habits.
    *   **Inputs**: Study hours, sleep hours, social media usage, and financial stress.
2.  **Fuzzy Logic Module (`fuzzy_module.py`)**: 
    *   **Function**: Handles the ambiguity of human emotions. Instead of treating stress as a rigid "Yes/No", it calculates a continuous severity score.
    *   **Inputs**: Self-reported Stress (0-100) and Isolation (0-100).
3.  **Inference Engine (`inference_engine.py`)**: 
    *   **Function**: The brain of the application. It acts as a knowledge base applying "Forward Chaining" rules to combine hard data with the AI's predictions.
    *   **Inputs**: Attendance, Grades Drop, ML Prediction, and Fuzzy Severity Score.
4.  **Counselor Dashboard (`app.py`, HTML/CSS)**: 
    *   **Function**: The graphical user interface (GUI) where school counselors input student data and receive formatted, actionable risk reports.

## 3. How do they all tie in together? (System Architecture)
The components work in a unified pipeline triggered by the Counselor Dashboard:

1.  **Data Entry**: The counselor enters all available student metrics into the web form.
2.  **Parallel Processing**: 
    *   The lifestyle metrics are sent to the **Machine Learning Classifier**.
    *   The emotional metrics are sent to the **Fuzzy Logic Module**.
3.  **Aggregation**: The outputs of both AI models, along with the student's attendance and grades, are sent to the **Inference Engine**.
4.  **Decision**: The Inference Engine runs through its rule base and returns a final, holistic `Risk Level` and an `Intervention Recommendation`.
5.  **Output**: The web interface dynamically displays this result in a color-coded format for the counselor.

## 4. How to use it? (User Guide)
1.  **Start the System**: Simply double-click the `Start_HealthSync.bat` file in your project folder. This will automatically start the AI server and open the dashboard in your web browser.
2.  **Enter Data**: Fill out the form with a student's data. 
    *   *Example Scenario A (High Risk)*: Set Attendance to 70%, check "Grades Drop", set Sleep to 4 hours, Financial Stress to 9, and Survey Stress to 85.
    *   *Example Scenario B (Low Risk)*: Set Attendance to 98%, Sleep to 8 hours, and Stress to 20.
4.  **Analyze**: Click the **Run Analysis** button.
5.  **Review the Report**: Look at the results panel on the right. It will instantly show the ML prediction, the Fuzzy Score, the Overall Risk, and what the counselor should do next.

## 5. How does it work? (Under the Hood)
When the "Run Analysis" button is clicked:
1.  JavaScript gathers the form data and sends a `POST` request to the Flask server (`/analyze`).
2.  Flask extracts the variables and passes them to the AI modules.
3.  **ML Process**: The Decision tree checks if the student's lifestyle patterns match historical data of students who needed interventions.
4.  **Fuzzy Process**: `scikit-fuzzy` maps the 0-100 stress/isolation scores into linguistic variables (e.g., "Mild", "Concerning", "Critical") using triangular membership functions. It calculates the overlapping intersections to output a precise severity percentage (e.g., 72.5%).
5.  **Inference Process**: Using IF-THEN rules (e.g., *IF Fuzzy Score > 70 AND Attendance < 80 THEN Risk = Critical*), the system solidifies a final recommendation.
6.  Flask packages this result into a JSON response and sends it back to the frontend, which updates the DOM to display the badges and text.
