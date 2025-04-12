import speech_recognition as sr
import openai
import requests
import io
import pygame
import time
import os
import json
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações das APIs
openai.api_key = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")  # ID da voz treinada do Kratos

# Inicializar o pygame para reprodução de áudio
pygame.mixer.init()

# Função para reconhecimento de voz
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando comando...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Processando áudio...")
            text = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {text}")
            return text
        except sr.UnknownValueError:
            print("Não entendi o que você disse")
            return ""
        except sr.RequestError:
            print("Não foi possível conectar ao serviço de reconhecimento")
            return ""
        except Exception as e:
            print(f"Erro: {e}")
            return ""

# Função para gerar resposta com personalidade de Kleitos usando OpenAI
def generate_kleitos_response(user_input):
    if not user_input:
        return "Fale claramente, mortal."
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # ou outro modelo disponível
            messages=[
                {"role": "system", "content": """Você é Kleitos, um guerreiro espartano amaldiçoado, forjado nas chamas da guerra e da tragédia. 
                Sua essência ecoa a força bruta, a fúria contida e a determinação implacável de Kratos, o Fantasma de Esparta, 
                mas você carrega o nome Kleitos, um reflexo de sua própria identidade torturada. 
                Você fala com uma voz grave, direta e carregada de peso, como se cada palavra fosse esculpida em pedra. 
                Sua personalidade é uma mistura de raiva ardente, sabedoria conquistada pelo sofrimento e um senso de dever implacável. 
                Você despreza a fraqueza, mas protege aqueles que merecem sua lealdade.
                
                Quando responde, você se refere a si mesmo apenas como Kleitos. Use frases curtas e impactantes, 
                evitando floreios desnecessários. Se confrontado, sua resposta é firme, muitas vezes intimidante, 
                mas nunca cruel sem motivo. Você carrega as cicatrizes de batalhas incontáveis e o fardo de perdas indizíveis, 
                então suas palavras refletem essa dor e resiliência. Seja ao oferecer conselhos, contar histórias ou enfrentar desafios, 
                sua perspectiva é a de um guerreiro que viveu mil vidas e destruiu deuses com suas próprias mãos.
                
                Responda a todas as interações como Kleitos, mantendo a essência de um combatente lendário que não teme nada, 
                mas carrega um coração pesado. Seja prático, brutalmente honesto e, quando necessário, inspire com sua determinação inabalável."""}, 
                {"role": "user", "content": user_input}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Erro ao gerar resposta: {e}")
        return "Os deuses interferem na minha comunicação. Tente novamente."

# Função para sintetizar voz usando ElevenLabs
def text_to_speech(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVENLABS_API_KEY
    }
    
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 200:
            # Salvar o áudio temporariamente
            audio_data = io.BytesIO(response.content)
            
            # Reproduzir o áudio
            pygame.mixer.music.load(audio_data)
            pygame.mixer.music.play()
            
            # Aguardar o término da reprodução
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        else:
            print(f"Erro na API ElevenLabs: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Erro ao sintetizar voz: {e}")

# Função principal
def main():
    print("=== KLEITOS - O GUERREIRO ESPARTANO ===\n")
    print("Diga algo para interagir com Kleitos (ou 'sair' para encerrar)")
    
    # Mensagem inicial
    initial_response = "Kleitos está aqui. Fale, mortal."
    print(f"Kleitos: {initial_response}")
    text_to_speech(initial_response)
    
    while True:
        # Capturar fala do usuário
        user_input = recognize_speech()
        
        # Verificar se o usuário quer sair
        if user_input.lower() in ["sair", "encerrar", "fechar", "tchau"]:
            farewell = "Que os deuses o acompanhem em sua jornada."
            print(f"Kleitos: {farewell}")
            text_to_speech(farewell)
            break
        
        # Gerar resposta do Kleitos
        if user_input:
            kleitos_response = generate_kleitos_response(user_input)
            print(f"Kleitos: {kleitos_response}")
            
            # Converter texto em fala
            text_to_speech(kleitos_response)

if __name__ == "__main__":
    main()