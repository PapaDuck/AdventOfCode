import os
import sys
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# .env-Datei laden
load_dotenv()
SESSION_COOKIE = os.getenv("SESSION_COOKIE")

if not SESSION_COOKIE:
    raise Exception("SESSION_COOKIE ist nicht gesetzt. Bitte füge es zur .env-Datei hinzu.")
    
BASE_URL = "https://adventofcode.com"
REQUEST_DELAY = 1.5  # Sekunden zwischen Requests (respektvoller Umgang mit der API)

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

    if response.status_code == 400:
        raise Exception(f"Tag noch nicht verfügbar oder Session Cookie ungültig")
    elif response.status_code == 404:
        raise Exception(f"Tag existiert nicht (möglicherweise zukünftiges Datum)")
    elif response.status_code != 200:
        raise Exception(f"HTTP {response.status_code}: {response.reason}")

    return response.text

def convert_to_markdown(content):
    """
    Konvertiert den Textinhalt in Markdown-Format.
    """
    # Markdown für Highlights anpassen
    content = content.replace(":", ": **")  # Hervorhebung nach Doppelpunkten
    content = content.replace(".", ".**")  # Hervorhebung am Satzende
    return content

def day_exists(year, day):
    """
    Prüft, ob ein Tag bereits in der Ordnerstruktur existiert.
    """
    folder_path = os.path.join(str(year), f"day{day}")
    return os.path.exists(folder_path)

def create_structure(year, day, content, input_data):
    """
    Erstellt die Verzeichnisstruktur und speichert die Aufgabe, main.py, input.txt und input_test.txt ab.
    """
    folder_path = os.path.join(str(year), f"day{day}")
    os.makedirs(folder_path, exist_ok=True)

    # Aufgabe speichern
    task_file_path = os.path.join(folder_path, f"day{day}.md")
    with open(task_file_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Eingabedatei speichern (echte Daten)
    input_file_path = os.path.join(folder_path, "input.txt")
    with open(input_file_path, "w", encoding="utf-8") as f:
        f.write(input_data)

    # Test-Eingabedatei erstellen (leer, muss manuell befüllt werden)
    test_input_file_path = os.path.join(folder_path, "input_test.txt")
    with open(test_input_file_path, "w", encoding="utf-8") as f:
        f.write("# TODO: Füge hier die Test-Daten aus der Aufgabenbeschreibung ein\n")

    # main.py erstellen
    main_file_path = os.path.join(folder_path, "main.py")
    with open(main_file_path, "w", encoding="utf-8") as f:
        f.write(f"""\
import sys

def load_data(test_file=False):
    filename = "input_test.txt" if test_file else "input.txt"
    with open(filename) as input_file:
        data = input_file.read()
    return data.splitlines()


def day{day}():
    data = load_data(testing)
    print(data)
    # TODO: Implementiere die Lösung hier


def main():
    result = day{day}()
    print(f'##### {{result}} #####')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        parameter = sys.argv[1]
        if parameter == "test":
            testing = True
    else:
        testing = False
    main()
""")

def get_available_years():
    """
    Gibt eine Liste der verfügbaren Jahre zurück (2015 bis aktuelles Jahr).
    """
    current_year = datetime.now().year
    # AoC startet im Dezember, also nur bis aktuelles Jahr wenn wir schon in Dezember sind
    if datetime.now().month < 12:
        current_year -= 1
    return list(range(2015, current_year + 1))

def get_max_available_day(year):
    """
    Ermittelt den höchsten verfügbaren Tag für ein Jahr.
    Advent of Code läuft vom 1. bis 25. Dezember.
    """
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day
    
    # Wenn das Jahr in der Zukunft liegt, sind keine Tage verfügbar
    if year > current_year:
        return 0
    
    # Wenn das Jahr in der Vergangenheit liegt, sind alle 25 Tage verfügbar
    if year < current_year:
        return 25
    
    # Aktuelles Jahr: prüfe Monat und Tag
    if current_month < 12:
        return 0  # Noch nicht Dezember
    elif current_month == 12:
        return min(current_day, 25)  # Max. Tag 25
    else:
        return 25  # Jahr ist vorbei

def load_all_missing_days(year):
    """
    Lädt alle fehlenden Tage für ein bestimmtes Jahr.
    """
    max_day = get_max_available_day(year)
    
    if max_day == 0:
        print(f"\n⚠️  Keine Tage für Jahr {year} verfügbar!")
        if year > datetime.now().year:
            print(f"   Das Jahr liegt in der Zukunft.")
        else:
            print(f"   Advent of Code startet am 1. Dezember.")
        return
    
    print(f"\n{'='*60}")
    print(f"Lade fehlende Tage für Jahr {year} (verfügbar: 1-{max_day})")
    print(f"{'='*60}\n")
    
    loaded_count = 0
    skipped_count = 0
    error_count = 0
    
    for day in range(1, max_day + 1):  # Nur verfügbare Tage
        if day_exists(year, day):
            print(f"  ⏭️  Tag {day:2d}: Bereits vorhanden, überspringe...")
            skipped_count += 1
            continue
        
        try:
            print(f"  📥 Tag {day:2d}: Lade Aufgabe...", end=" ", flush=True)
            content = fetch_puzzle(year, day)
            time.sleep(REQUEST_DELAY)  # Warte zwischen Requests
            
            print("Lade Input...", end=" ", flush=True)
            input_data = fetch_input(year, day)
            time.sleep(REQUEST_DELAY)  # Warte zwischen Requests
            
            create_structure(year, day, content, input_data)
            print("✅ Erfolgreich!")
            loaded_count += 1
            
        except Exception as e:
            print(f"❌ Fehler: {e}")
            error_count += 1
            # Bei kritischen Fehlern (z.B. Session ungültig) abbrechen
            if "Session Cookie" in str(e) or "400" in str(e):
                print(f"\n⚠️  Kritischer Fehler erkannt. Breche ab.")
                print(f"   Überprüfe dein SESSION_COOKIE in der .env Datei!")
                break
    
    print(f"\n{'='*60}")
    print(f"Zusammenfassung für {year}:")
    print(f"  ✅ Erfolgreich geladen: {loaded_count}")
    print(f"  ⏭️  Übersprungen:        {skipped_count}")
    print(f"  ❌ Fehler:              {error_count}")
    print(f"{'='*60}\n")

def load_single_day(year, day):
    """
    Lädt einen einzelnen Tag.
    """
    # Prüfe ob der Tag verfügbar ist
    max_day = get_max_available_day(year)
    if day > max_day:
        print(f"\n⚠️  Tag {day} ist für Jahr {year} noch nicht verfügbar!")
        print(f"   Maximal verfügbarer Tag: {max_day}")
        return
    
    if day_exists(year, day):
        print(f"\nTag {day} für Jahr {year} existiert bereits!")
        overwrite = input("Möchtest du ihn überschreiben? (j/n): ")
        if overwrite.lower() != 'j':
            return
    
    try:
        print(f"\nLade Aufgabe für Jahr {year}, Tag {day}...")
        content = fetch_puzzle(year, day)
        print(f"Lade Eingabedatei für Jahr {year}, Tag {day}...")
        input_data = fetch_input(year, day)
        create_structure(year, day, content, input_data)
        print(f"✅ Erfolgreich erstellt unter {year}/day{day}")
    except Exception as e:
        print(f"❌ Fehler: {e}")
        if "Session Cookie" in str(e):
            print(f"\n💡 Tipp: Überprüfe dein SESSION_COOKIE in der .env Datei!")
            print(f"   1. Gehe zu https://adventofcode.com")
            print(f"   2. Logge dich ein")
            print(f"   3. Öffne DevTools (F12)")
            print(f"   4. Application → Cookies → session")

def main():
    print("\n" + "="*60)
    print("  Advent of Code - Automatischer Puzzle Downloader")
    print("="*60)
    print("\nOptionen:")
    print("  1. Einzelnen Tag laden")
    print("  2. Alle fehlenden Tage eines Jahres laden")
    print("  3. Alle fehlenden Tage aller Jahre laden")
    print("="*60 + "\n")
    
    try:
        choice = input("Wähle eine Option (1-3): ").strip()
        
        if choice == "1":
            year = int(input("Gib das Jahr ein (2015-2025): "))
            day = int(input("Gib den Tag ein (1-25): "))
            load_single_day(year, day)
            
        elif choice == "2":
            year = int(input("Gib das Jahr ein (2015-2025): "))
            confirm = input(f"\n⚠️  Dies lädt alle fehlenden Tage für {year}. Fortfahren? (j/n): ")
            if confirm.lower() == 'j':
                load_all_missing_days(year)
            
        elif choice == "3":
            available_years = get_available_years()
            print(f"\n⚠️  Dies lädt alle fehlenden Tage für die Jahre {available_years[0]}-{available_years[-1]}.")
            print("Dies kann einige Minuten dauern und erzeugt viele Requests!")
            confirm = input("Wirklich fortfahren? (j/n): ")
            if confirm.lower() == 'j':
                for year in available_years:
                    load_all_missing_days(year)
                    time.sleep(REQUEST_DELAY)  # Pause zwischen Jahren
        else:
            print("Ungültige Option!")
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Abgebrochen durch Benutzer.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fehler: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()