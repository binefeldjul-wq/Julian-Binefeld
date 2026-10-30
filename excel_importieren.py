import openpyxl

# Import der Gehaltsabrechnungslogik 
from gehalt import berechne_abrechnung

def start_programm(frac):
    # Excel-Datei laden
    wb = openpyxl.load_workbook("gehaltsdatei.xlsx")
    sheet = wb.active

    # Schleife über alle Mitarbeiterzeilen
    for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row):
        name = row[0].value
        if not name:
            continue

    # Rohdaten aus Excel einlesen
    bruttogehalt = row[1].value or 0
    vL_AG = row[2].value or 0
    jahr = row[3].value or 0
    kinder = row[4].value or 0
    vS = row[5].value or 0
    Zusatzbeitrag = row[6].value or 0
    vorschuss = row[7].value or 0

    # Übergabe an deine gehalt.py!
    ergebnisse = berechne_abrechnung(
        name, bruttogehalt, vL_AG, jahr, kinder, vS, Zusatzbeitrag, vorschuss, frac
    )

    # Ergebnisse in Excel zurückschreiben
    row[8].value = round(ergebnisse["nettogehalt"], 2)
    row[9].value = round(ergebnisse["ueberweisungbetrag"], 2)

    # Speichern 
    wb.save("gehaltsdatei.xlsx")
    print("Alle Gehaltsdaten erfolgreich über gehalt.py verarbeitet! ")
    print("")