# EscribIA - Corrección y Calificación Automática de Textos en Español

Este proyecto es una aplicación de **Flask** que utiliza la API de OpenAI para corregir y calificar textos escritos en español. La aplicación está diseñada para ayudar a estudiantes universitarios a mejorar sus habilidades de escritura al proporcionar correcciones automáticas y calificaciones basadas en gramática, ortografía, puntuación y redacción general.

## Características

- **Corrección automática de textos**: Se revisan errores ortográficos, gramaticales, y de puntuación.
- **Calificación automática**: Se asigna una calificación numérica (del 1 al 10) basada en la calidad del texto después de la corrección.
- **API REST**: La aplicación está diseñada como una API REST para que pueda integrarse con otras plataformas.

## Tecnologías Utilizadas

- **Python 3.x**
- **Flask**: Microframework web para crear las rutas de la API.
- **Flask-CORS**: Manejo de CORS para permitir solicitudes desde cualquier origen.
- **OpenAI API**: Para realizar las correcciones y calificaciones basadas en los modelos de lenguaje de OpenAI.
- **Postman**: Para realizar pruebas de la API de forma manual.

## Instalación

Sigue los pasos a continuación para clonar, instalar y ejecutar la aplicación en tu entorno local.

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/escribia-correccion.git
cd escribia-correccion
```

### 2. Crear un entorno virtual

Es recomendable crear un entorno virtual para manejar las dependencias del proyecto:

```bash
python -m venv venv
source venv/bin/activate  # En Windows usa venv\Scripts\activate
```

### 3. Instalar las dependencias

Todas las dependencias necesarias están listadas en `requirements.txt`. Puedes instalarlas con:

```bash
pip install -r requirements.txt
```

### 4. Configurar las variables de entorno

Necesitarás una API key de OpenAI. Puedes obtenerla creando una cuenta en [OpenAI](https://openai.com).

Crea un archivo `.env` en la raíz del proyecto y añade lo siguiente:

```bash
OPENAI_API_KEY=tu_clave_de_openai_aqui
```

### 5. Ejecutar la aplicación

Una vez configurado el entorno y las variables, puedes ejecutar la aplicación localmente con:

```bash
flask run
```

Por defecto, Flask ejecutará la aplicación en `http://127.0.0.1:5000`.

## Uso de la API

La API expone una ruta `/procesar_texto` para corregir y calificar los textos. Puedes enviar una solicitud POST con un texto en formato JSON, y recibirás la respuesta con el texto corregido y la calificación.

### Ejemplo de Solicitud

#### Método: `POST`

#### URL: `http://127.0.0.1:5000/procesar_texto`

#### Body (raw):

```json
{
  "text": "ete testo es de prueva para corregir"
}
```

#### Ejemplo de Respuesta:

```json
{
  "corrected_text": "Este texto es de prueba para corregir.",
  "score": "7"
}
```

## Pruebas con Postman

Puedes probar la API utilizando Postman siguiendo estos pasos:

1. Abre Postman y crea una nueva solicitud.
2. Selecciona el método **POST**.
3. Introduce la URL `http://127.0.0.1:5000/procesar_texto`.
4. En la pestaña **Headers**, añade `Content-Type: application/json`.
5. En la pestaña **Body**, selecciona la opción **raw** y elige **JSON**. Luego, introduce el texto que deseas corregir, por ejemplo:

   ```json
   {
     "text": "ete testo es de prueva para corregir"
   }
   ```

6. Haz clic en **Send** y revisa la respuesta, que incluirá el texto corregido y la calificación.

## Estructura del Proyecto

```
├── app.py               # Archivo principal con las rutas de la API
├── class_model.py       # Clases para la corrección y calificación de textos
├── .env                 # Archivo para las variables de entorno (ignorado en Git)
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación del proyecto
```

## Licencia

Este proyecto es de uso académico y está bajo la licencia MIT. Puedes leer más sobre la licencia en el archivo `LICENSE` de este repositorio.


