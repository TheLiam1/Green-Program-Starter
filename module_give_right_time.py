"""import module_give_neueste_MWh_and_right_timestamp_gesamt as mgn
import main


# Ich brauche jetzt nur noch den Gesamtwert abzurufen um einer bestimmten Uhrzeit
# Und dann den Grünstromwert abrufen um einer bestimmten Uhrzeit
# Dann den Anteil des grünen Stromes am Gesamtwert berechnen

def give_anteil_zu_uhrzeit(zahl1_wert):
    gesamtwert_zu_uhrzeit = mgn.give_MWh_gesamt_zu_uhrzeit(zahl1_wert)
    # timestamp_zu_uhrzeit_gesamt = mgn.give_right_timestamp_zu_uhrzeit()

    grüner_wert_zu_uhrzeit = main.give_erzeugung_5097_zu_uhrzeit(zahl1_wert)
    # timestamp_zu_uhrzeit_grün = main.give_right_timestamp_zu_uhrzeit_grün()

    anteil_an_grünem_strom = grüner_wert_zu_uhrzeit / gesamtwert_zu_uhrzeit
    return anteil_an_grünem_strom
    """