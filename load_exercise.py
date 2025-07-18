import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# .env-Datei laden
load_dotenv()
SESSION_COOKIE = os.getenv("SESSION_COOKIE")

if not SESSION_COOKIE:
    raise Exception("SESSION_COOKIE ist nicht gesetzt. Bitte füge es zur .env-Datei hinzu.")

BASE_URL = "https://adventofcode.com"

def fetch_puzzle(year, day):
    """
    Lädt die Aufgabe des Advent of Code für ein bestimmtes Jahr und einen Tag herunter.
    """
    url = f"{BASE_URL}/{year}/day/{day}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Fehler beim Laden der Aufgabe: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    article = soup.find("article", class_="day-desc")

    if not article:
        raise Exception("Die Aufgabe konnte nicht gefunden werden.")

    # Extrahiere den reinen Text und entferne unnötige Leerzeichen
    content = article.get_text(separator="\n", strip=True)
    return convert_to_markdown(content)

def fetch_input(year, day):
    """
    Lädt die Input-Datei für ein bestimmtes Jahr und einen Tag herunter.
    """
    url = f"{BASE_URL}/{year}/day/{day}/input"
    headers = {"Cookie": f"session={SESSION_COOKIE}"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Fehler beim Laden der Eingabedatei: {response.status_code}")

    return response.text

def convert_to_markdown(content):
    """
    Konvertiert den Textinhalt in Markdown-Format.
    """
    # Markdown für Highlights anpassen
    content = content.replace(":", ": **")  # Hervorhebung nach Doppelpunkten
    content = content.replace(".", ".**")  # Hervorhebung am Satzende
    return content

def create_structure(year, day, content, input_data):
    """
    Erstellt die Verzeichnisstruktur und speichert die Aufgabe, main.py und input.txt ab.
    """
    folder_path = os.path.join(str(year), f"day{day}")
    os.makedirs(folder_path, exist_ok=True)

    # Aufgabe speichern
    task_file_path = os.path.join(folder_path, f"day{day}.md")
    with open(task_file_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Eingabedatei speichern
    input_file_path = os.path.join(folder_path, "input.txt")
    with open(input_file_path, "w", encoding="utf-8") as f:
        f.write(input_data)

    # main.py erstellen
    main_file_path = os.path.join(folder_path, "main.py")
    with open(main_file_path, "w", encoding="utf-8") as f:
        f.write(f"""\
def day{day}():
    \"\"\"Tag {day} des Jahres {year}\"\"\"
    print("Lösung für Tag {day} des Jahres {year} hier implementieren.")

def main():
    day{day}()

if __name__ == "__main__":
    main()
""")

def main():
    year = int(input("Gib das Jahr ein (2015-2021): "))
    day = int(input("Gib den Tag ein (1-25): "))

    try:
        print(f"Lade Aufgabe für Jahr {year}, Tag {day}...")
        content = fetch_puzzle(year, day)
        print(f"Lade Eingabedatei für Jahr {year}, Tag {day}...")
        input_data = fetch_input(year, day)
        create_structure(year, day, content, input_data)
        print(f"Aufgabe, Eingabedatei und main.py erfolgreich erstellt unter {year}/day{day}")
    except Exception as e:
        print(f"Fehler: {e}")
    print('\n')


if __name__ == "__main__":
    main()
