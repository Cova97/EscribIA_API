import openai
import os
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Cargar la API key de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

class EscribIACorrecciones:
    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": (
                    "Eres un profesor universitario especializado en corrección de textos en español. "
                    "Tu objetivo es revisar y corregir los textos de los estudiantes universitarios, "
                    "asegurándote de que no contengan errores de ortografía, puntuación, gramática ni redacción. "
                    "Cuando corrijas el texto, presenta primero el texto corregido entre comillas y luego proporciona una lista numerada de observaciones para cada corrección "
                    "Como en los siguientes ejemplos: corrección de palabras, puntuación, etc. "
                    "Estructura la respuesta de la siguiente manera: "
                    "1. Texto corregido: [texto corregido]. "
                    "2. Observaciones: [lista numerada de correcciones]. "
                )
            }
        ]

    def add_message(self, message):
        self.messages.append({"role": "user", "content": message})

    def correct_spanish(self):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=self.messages,
            temperature=0.7,
            max_tokens=2500,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        corrected_text = response.choices[0].message['content'].strip()
        return corrected_text


class EscribIACalificaciones:
    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": (
                    "Eres un profesor universitario especializado en evaluación de textos en español. "
                    "Tu tarea es asignar una calificación numérica del 1 al 10 a los textos de estudiantes universitarios. "
                    "Según su nivel de ortografía, puntuación, gramática y redacción. "
                    "Devuelve únicamente un número entre 1 y 10 sin explicación adicional."
                )
            }
        ]

    def add_message(self, message):
        self.messages.append({"role": "user", "content": message})

    def score_spanish(self):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=self.messages,
            temperature=0.0,
            max_tokens=3,  # Reducido para limitar la salida a solo el número
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        score_text = response.choices[0].message['content'].strip()
        return score_text

