import re

import pyttsx3
import speech_recognition as sr


def initialize_engine():
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.setProperty("voice", "spanish")
    return engine


def identify_name(text):
    name = None
    patterns = ["me llamo ([A-Za-z]+)", "^([A-Za-z]+)$"]
    for pattern in patterns:
        try:
            name = re.findall(pattern, text)[0]
        except IndexError:
            pass
        return name


def recognize_voice(r):
    with sr.Microphone() as source:
        print("Puedes hablar")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="es-ES")
    return text


def main():
    engine = initialize_engine()

    engine.say("Hola, ¿cómo te llamas?")
    engine.runAndWait()
    r = sr.Recognizer()

    text = recognize_voice(r)

    name = identify_name(text)
    if name:
        engine.say("Encantado de conocerte, {}".format(name[0]))
    else:
        engine.say("Mira, la verdad no te entiendo. Eres un pendejo")
    engine.runAndWait()


if __name__ == '__main__':
    main()
