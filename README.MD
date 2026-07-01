# Sistema de Assistência Virtual com Python

Projeto desenvolvido como desafio prático utilizando **Processamento de Linguagem Natural (PLN)** em Python.

O sistema realiza reconhecimento de voz (Speech to Text), sintetização de voz (Text to Speech) e executa comandos por voz para automatizar tarefas simples.

## Funcionalidades

* 🎤 Reconhecimento de voz em português (Speech to Text)
* 🔊 Conversão de texto em fala (Text to Speech)
* 🌐 Pesquisa automática no Google
* 🗺️ Abertura de rota no Google Maps
* ▶️ Abertura de um canal no YouTube

## Tecnologias utilizadas

* Python 3
* SpeechRecognition
* Pyttsx3
* PyAudio
* Webbrowser (biblioteca padrão)
* urllib (biblioteca padrão)

## Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/dio-challenge-system-virtual-assistant.git
```

Acesse a pasta do projeto:

```bash
cd dio-challenge-system-virtual-assistant
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

### Linux (Ubuntu/Debian)

Para utilizar o microfone é necessário instalar o PortAudio:

```bash
sudo apt update
sudo apt install portaudio19-dev python3-dev build-essential
```

## Executando

```bash
python main.py
```

Ao iniciar, o assistente informará que está pronto para ouvir comandos.

## Comandos disponíveis

### Pesquisar no Google

Comando de voz:

```
igreja católica
```

ou simplesmente

```
igreja
```

Ação executada:

* Abre uma pesquisa no Google sobre **Igreja Católica**.

---

### Abrir rota no Google Maps

Comando de voz:

```
rotas para mar a dentro
```

ou

```
mar
```

Ação executada:

* Abre o Google Maps com a rota para o destino configurado.

---

### Abrir canal no YouTube

Comando de voz:

```
padre josé eduardo
```

ou

```
padre
```

Ação executada:

* Abre o canal do Padre José Eduardo no YouTube.

---

### Encerrar o programa

Comando de voz:

```
sair
```

## Estrutura do projeto

```
.
├── main.py
├── requirements.txt
└── README.md
```

## Bibliotecas utilizadas

* SpeechRecognition
* Pyttsx3
* PyAudio

## Objetivo

Este projeto foi desenvolvido para demonstrar os conceitos básicos de **Processamento de Linguagem Natural (PLN)**, implementando um assistente virtual simples capaz de:

* converter texto em voz;
* converter voz em texto;
* interpretar comandos de voz;
* automatizar ações utilizando o navegador.

## Autor

Projeto desenvolvido como desafio prático da DIO (Digital Innovation One).
