# Kleitos 3.0 - Assistente de Voz do Guerreiro Espartano

Este programa cria um assistente de voz interativo baseado no personagem Kleitos, um guerreiro espartano com personalidade semelhante ao Kratos. O sistema utiliza reconhecimento de voz para captar o que você diz, processa com inteligência artificial para emular a personalidade de Kleitos, e responde usando síntese de voz do ElevenLabs.

## Funcionalidades

- Reconhecimento de voz em português
- Processamento de linguagem natural com personalidade de Kleitos
- Síntese de voz usando ElevenLabs com voz personalizada
- Interface de linha de comando simples

## Requisitos

- Python 3.7 ou superior
- Conexão com a internet
- Microfone funcional
- Conta na OpenAI com créditos disponíveis
- Conta no ElevenLabs com voz personalizada treinada

## Instalação

1. Clone ou baixe este repositório

2. Instale as dependências necessárias:

```
pip install SpeechRecognition openai requests pygame python-dotenv
```

3. Instale o PyAudio (necessário para o reconhecimento de voz):

```
pip install PyAudio
```

Se houver problemas na instalação do PyAudio no Windows, você pode tentar:

```
pip install pipwin
pipwin install PyAudio
```

4. Configure as chaves de API:
   - Renomeie o arquivo `.env.example` para `.env`
   - Preencha com suas chaves da API OpenAI e ElevenLabs
   - Adicione o ID da sua voz personalizada treinada no ElevenLabs

## Como usar

1. Execute o programa:

```
python main.py
```

2. Aguarde a mensagem inicial de Kleitos

3. Fale ao microfone quando solicitado

4. Para encerrar o programa, diga "sair", "encerrar", "fechar" ou "tchau"

## Treinando sua voz personalizada no ElevenLabs

1. Crie uma conta no [ElevenLabs](https://elevenlabs.io/)

2. Acesse a seção de vozes e selecione "Create Voice"

3. Faça upload de amostras de áudio da voz do Kratos (quanto mais amostras, melhor a qualidade)

4. Após o treinamento, copie o ID da voz gerada para o arquivo `.env`

## Solução de problemas

- **Erro no reconhecimento de voz**: Verifique se o microfone está funcionando corretamente e se o ambiente não está muito barulhento

- **Erro na API OpenAI**: Verifique se sua chave API está correta e se você tem créditos disponíveis

- **Erro na API ElevenLabs**: Verifique se sua chave API está correta e se você tem minutos de voz disponíveis

## Personalização

Você pode modificar a personalidade de Kleitos editando a descrição do personagem no arquivo `main.py`, na função `generate_kleitos_response()`.