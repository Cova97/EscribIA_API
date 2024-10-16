from flask import Flask, request, jsonify
from flask_cors import CORS
from class_model import EscribIACorrecciones, EscribIACalificaciones

# Cargar la aplicación
app = Flask(__name__)
CORS(app)

# Ruta para corregir y calificar el texto en una sola solicitud
@app.route('/procesar_texto', methods=['POST'])
def process_text():
    correcciones = EscribIACorrecciones()
    calificaciones = EscribIACalificaciones()
    
    try:
        data = request.get_json()
        if data is None or 'text' not in data:
            return jsonify({'error': 'No se proporcionó el texto.'}), 400
        
        text = data['text']
        
        # Primero, corregir el texto
        correcciones.add_message(text)
        corrected_text = correcciones.correct_spanish()
        
        # Luego, usar el texto corregido para la calificación
        calificaciones.add_message(corrected_text)
        score = calificaciones.score_spanish()
        
        # Retornar ambos resultados en una sola respuesta
        return jsonify({
            'corrected_text': corrected_text,
            'score': score
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main
if __name__ == '__main__':
    app.run(debug=True)
