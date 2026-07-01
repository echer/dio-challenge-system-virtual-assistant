import speech_recognition as sr
import pyttsx3
import webbrowser
import urllib.parse

# ==========================
# TEXT TO SPEECH
# ==========================
engine = pyttsx3.init()

def falar(texto):
    print("Assistente:", texto)
    engine.setProperty("voice", "roa/pt-br")
    engine.setProperty("rate", 170)  # velocidade (opcional)
    engine.setProperty("volume", 1.0)  # volume (opcional)

    engine.say(texto)
    engine.runAndWait()

# ==========================
# SPEECH TO TEXT
# ==========================
def ouvir():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Fale um comando...")
        falar("Estou ouvindo.")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
            )

            comando = recognizer.recognize_google(
                audio,
                language="pt-BR"
            ).lower()

            print("Você disse:", comando)
            return comando

        except sr.UnknownValueError:
            falar("Não consegui entender.")
            return ""

        except sr.RequestError:
            falar("Erro no serviço de reconhecimento.")
            return ""

        except Exception:
            falar("Ocorreu um erro.")
            return ""

# ==========================
# COMANDOS
# ==========================
def executar(comando):

    # 1 - Pesquisa Google
    if "igreja" in comando or "catolica" in comando:
        falar("Pesquisando Igreja Católica no Google.")

        pesquisa = urllib.parse.quote("igreja católica")
        webbrowser.open(f"https://www.google.com/search?q={pesquisa}")

    # 2 - Abrir rota
    elif "rotas" in comando or "mar" in comando:
        falar("Abrindo rota para Mar a Dentro.")

        webbrowser.open("https://maps.app.goo.gl/J15pVhTG1n7yDYiX7")

    # 3 - Abrir YouTube
    elif "padre" in comando or "jose eduardo" in comando:
        falar("Abrindo canal do Padre José Eduardo.")

        webbrowser.open("https://www.youtube.com/@PadreJos%C3%A9Eduardo")

    else:
        falar("Comando não reconhecido.")

# ==========================
# PROGRAMA PRINCIPAL
# ==========================
if __name__ == "__main__":

    falar("Assistente virtual iniciado.")

    while True:

        comando = ouvir()

        if comando == "":
            continue

        if "sair" in comando:
            falar("Encerrando o programa.")
            break

        executar(comando)