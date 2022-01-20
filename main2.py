# Importando los archivos necesarios para correr esta aplicación Flask
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

# Recibiendo los mensajes del usuario y mandando la respuesta
incoming_msg = request.values.get('Body', '').lower()
  
response = MessagingResponse()
msg = response.message()
msg.body('Esta es la respuesta del bot.')

# Lógica del chatbot.
def bot():
  
    # Entrada del usuario
    user_msg = request.values.get('Cuerpo', '').lower()
  
    # Creando el objeto de MessagingResponse
    response = MessagingResponse()
  
    q = user_msg + "geeksforgeeks.org"
  
    # Lista de URLS guardadas
    result = []
  
    # Buscando y guardando URLS
    for i in search(q, tld='co.in', num=6, stop=6, pause=2):
        result.append(i)
  
    # Desplegando el resultado
    msg = response.message(f"--- Resultado para '{user_msg}' son  ---")
  
    msg = response.message(result[0])
    msg = response.message(result[1])
    msg = response.message(result[2])
    msg = response.message(result[3])
    msg = response.message(result[4])
  
    return str(response)