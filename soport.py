import nltk
from nltk.tokenize import word_tokenize

def soporte_tecnico():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    
    print("¡Hola! Soy tu asistente de soporte técnico. ¿En qué puedo ayudarte?")
    
    respuestas = {
        "reiniciar": "Para reiniciar tu computadora:\n1. Guarda todos tus documentos abiertos\n2. Ve al menú de inicio\n3. Haz clic en el botón de energía\n4. Selecciona 'Reiniciar'",
        "señal": "Para problemas de señal:\n1. Verifica que tu dispositivo no esté en modo avión\n2. Intenta activar y desactivar la conexión\n3. Acércate más al router si es posible",
        "internet": "Para problemas de internet:\n1. Verifica que el cable de red esté conectado\n2. Reinicia el router (desconéctalo por 30 segundos)\n3. Comprueba si otros dispositivos tienen conexión",
        "contraseña": "Para cambiar tu contraseña:\n1. Ve a Configuración\n2. Selecciona 'Cuentas' o 'Seguridad'\n3. Busca la opción 'Cambiar contraseña'\n4. Sigue las instrucciones en pantalla",
        "lento": "Si tu dispositivo está lento:\n1. Cierra las aplicaciones que no estés usando\n2. Verifica el espacio disponible en disco\n3. Ejecuta el limpiador de disco\n4. Considera realizar un análisis de virus"
    }

    while True:
        try:
            pregunta = input("Tú: ").lower().strip()
            
            if not pregunta:
                print("Chatbot: Por favor, escribe tu pregunta.")
                continue
                
            if pregunta == "salir":
                print("Chatbot: ¡Hasta luego! Que tengas un buen día.")
                break
                
            palabras_clave = word_tokenize(pregunta)
            
            respuesta_encontrada = False
            for palabra in palabras_clave:
                if palabra in respuestas:
                    print(f"Chatbot: {respuestas[palabra]}")
                    respuesta_encontrada = True
                    break
            
            if not respuesta_encontrada:
                print("Chatbot: Lo siento, no entendí tu pregunta. Puedes preguntar sobre:\n" +
                    "- Cómo reiniciar tu dispositivo\n" +
                    "- Problemas de señal o internet\n" +
                    "- Cambio de contraseña\n" +
                    "- Dispositivo lento\n" +
                    "O escribe 'salir' para terminar.")
                
        except Exception as e:
            print("Chatbot: Hubo un error al procesar tu pregunta. Por favor, intenta de nuevo.")
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    soporte_tecnico()