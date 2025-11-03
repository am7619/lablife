from flask import Flask, render_template_string, request
import requests
import math

app = Flask(__name__)

DEFAULT_VALUES = {
    'wbc': 4.5, 'hgb': 12.8, 'hct': 35.0, 'plt': 190.0, 'rbc': 3.58,
    'mcv': 97.7, 'mch': 35.7, 'mchc': 36.6, 'rdw': 13.1, 'mpv': 6.2,
    'neut_percent': 67.5, 'lymph_percent': 24.2, 'mono_percent': 6.2,
    'eos_percent': 1.6, 'baso_percent': 0.5, 'sod': 143.0, 'pot': 3.9,
    'chlor': 104.0, 'co2': 29.0, 'un': 12.0, 'creat': 1.2, 'gluc': 182.0,
    'cal': 9.4, 'prot': 7.3, 'alb': 4.7, 'ast': 42.0, 'alt': 41.0,
    'alk': 74.0, 'tbil': 1.0
}

DISPLAY_NAMES = {
    'wbc': 'White Blood Cells (10^9/L)',
    'hgb': 'Hemoglobin (g/dL)',
    'hct': 'Hematocrit (%)',
    'plt': 'Platelets (10^9/L)',
    'rbc': 'Red Blood Cells (10^12/L)',
    'mcv': 'MCV (fL)',
    'mch': 'MCH (pg)',
    'mchc': 'MCHC (g/dL)',
    'rdw': 'RDW (%)',
    'mpv': 'Mean Platelet Volume (fL)',
    'neut_percent': 'Neutrophils (%)',
    'lymph_percent': 'Lymphocytes (%)',
    'mono_percent': 'Monocytes (%)',
    'eos_percent': 'Eosinophils (%)',
    'baso_percent': 'Basophils (%)',
    'sod': 'Sodium (mmol/L)',
    'pot': 'Potassium (mmol/L)',
    'chlor': 'Chloride (mmol/L)',
    'co2': 'CO2 (mmHg)',
    'un': 'Urea Nitrogen (mg/dL)',
    'creat': 'Creatinine (mg/dL)',
    'gluc': 'Glucose (mg/dL)',
    'cal': 'Calcium (mg/dL)',
    'prot': 'Total Protein (g/dL)',
    'alb': 'Albumin (g/dL)',
    'ast': 'AST (U/L)',
    'alt': 'ALT (U/L)',
    'alk': 'Alkaline Phosphatase (U/L)',
    'tbil': 'Total Bilirubin (mg/dL)'
}

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>LabLife - Biological Age</title>
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
  <div class="max-w-4xl mx-auto mt-10 bg-white p-8 rounded-2xl shadow">
    <h1 class="text-2xl font-semibold mb-6 text-center text-blue-700">LabLife - Biological Age</h1>
    <h1 class="text-1xl font-semibold mb-6 text-center text-blue-700">Calculate your biological age from your laboratory results</h1>
    <form method="post" class="space-y-6">
      <div class="text-center">
        <button type="submit"
                class="bg-blue-500 hover:bg-blue-600 text-white px-8 py-3 rounded-lg shadow transition">
          Predict
        </button>
        {% if prediction is not none %}
          <div class="mt-4">
            <p class="bg-green-500 hover:bg-green-600 text-white px-12 py-3 rounded-lg shadow transition">
              {{ prediction }}
            </p>
          </div>
        {% endif %}
      </div>

      <!-- Lab input section -->
      <div class="grid grid-cols-3 gap-3 mt-6">
        {% for field, value in values.items() %}
          <div>
            <label class="block text-gray-700 font-medium mb-1">{{ display_names[field] }}</label>
            <input type="number" step="any" name="{{ field }}" value="{{ value }}"
                   class="w-full p-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300">
          </div>
        {% endfor %}
      </div>
    </form>
  </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    values = DEFAULT_VALUES.copy()

    if request.method == 'POST':
        for k in values.keys():
            try:
                values[k] = float(request.form.get(k, 0))
            except ValueError:
                values[k] = 0.0

        try:
            response = requests.post('http://localhost:8080/predict', json=values)
            if response.ok:
                result = response.json().get('prediction', None)
                if result is not None:
                    prediction = f"Predicted age: {int(round(float(result)))} years"
            else:
                prediction = f"*** Server Error {response.status_code} ***"
        except Exception as e:
            prediction = f"*** Connection error: {e} ***"

    return render_template_string(HTML, values=values, prediction=prediction, display_names=DISPLAY_NAMES)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
