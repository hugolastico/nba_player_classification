import numpy as np
from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Initialisation de flask
app = Flask(__name__)

# Charger le modèle
lda_model = joblib.load('lda_model.pkl')

# Initialisation de la route
@app.route('/predict', methods=['POST'])

def predict():
    
    # Récupérer les données JSON envoyées par l'utilisateur
    data = request.get_json()

    # Vérifier que les données contiennent les features
    features = ['GP', 'PTS/MIN', 'REB', 'AST', 'STL', 'BLK']
    if not all(feature in data for feature in features):
        return jsonify({'error': 'Invalid input. Missing required features.'}), 400
    
    # Charger le scaler sauvegardé
    scaler = joblib.load('scaler.pkl')
    
    # Préparer les données pour le modèle
    input_data = pd.DataFrame([[data[feature] for feature in features]], columns=features)
    input_data = scaler.transform(input_data)
    
    # Prédiction
    prediction = lda_model.predict(input_data)

    # Retourner le résultat
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)

