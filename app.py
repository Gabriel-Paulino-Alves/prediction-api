from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
from classes.class_names import class_names


app = Flask(__name__)

# Carrega o modelo
model = load_model('models/my_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    
    if 'image' not in request.files:
        return jsonify({'error': 'Não foi enviada nenhuma imagem!'}), 400

    file = request.files['image']

    # Abrir e redimensionar
    img = Image.open(file).resize((224, 224))  # ajuste para o tamanho do seu modelo
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array / 255.0, axis=0)

    #predição
    prediction = model.predict(img_array)
    class_idx = int(np.argmax(prediction))

    return jsonify({'class_index': class_idx, 'class_name': class_names[class_idx]})
