import tool
def berechne_abrechnung(name, bruttogehalt, vL_AG, lohnsteuer, kinder, vS, Zusatzbeitrag, vorschuss, frac):
    print("Willkommen zu Julian Binefelds Gehaltsrechner. ")
    print("")
    
    #Beitragsbemessungsgrenzen 2026
    Beitragsbemessungsgrenze_RV_AV_2026 = 8450.00
    Beitragsbemessungsgrenze_KV_PV_2026 = 5812.50

    jahr = 2026
    
    if jahr == 2026:
        Beitragsbemessungsgrenze_RV_AV = Beitragsbemessungsgrenze_RV_AV_2026
        Beitragsbemessungsgrenze_KV_PV = Beitragsbemessungsgrenze_KV_PV_2026
    else:
        print("Fehler: Bitte 2026 wählen! ")
    
    st_sv_gehalt = bruttogehalt + vL_AG

    KiSt_euro = lohnsteuer * 8 / 100
    steuern = lohnsteuer + KiSt_euro
    print("")
    
    #Beitragssätze der Sozialversicherungen
    RV_Beitragssatz = 18.6
    AV_Beitragssatz = 2.6
    KV_Beitragssatz = 14.6
    
    #Berechnung des Arbeitnehmer/Arbeitgeberanteils (50/50)
    RV_AN_anteil = RV_Beitragssatz / 200
    AV_AN_anteil = AV_Beitragssatz / 200
    KV_AN_anteil = (KV_Beitragssatz + Zusatzbeitrag) / 200
    
    if  kinder >= 1 and kinder < 5:
        PV_Beitragssatz_AN = 1.8 - 0.25 * (kinder - 1)
    elif kinder >= 5:
        PV_Beitragssatz_AN = 0.8
    else:
        PV_Beitragssatz_AN = 2.4
    
    PV_AN_anteil = PV_Beitragssatz_AN / 100
    
    PV_Beitragssatz_AG = 1.8
    PV_AG_anteil = PV_Beitragssatz_AG / 100
    print("")
    
    #Berechnung RV/AV
    if st_sv_gehalt >= Beitragsbemessungsgrenze_RV_AV:
        RV = Beitragsbemessungsgrenze_RV_AV * RV_AN_anteil
        AV = Beitragsbemessungsgrenze_RV_AV * AV_AN_anteil
    else:
        RV = st_sv_gehalt * RV_AN_anteil
        AV = st_sv_gehalt * AV_AN_anteil
    
    #Berechnung KV/PV
    if st_sv_gehalt >= Beitragsbemessungsgrenze_KV_PV:
        KV = Beitragsbemessungsgrenze_KV_PV * KV_AN_anteil
        PV_AN = Beitragsbemessungsgrenze_KV_PV * PV_AN_anteil
        PV_AG = Beitragsbemessungsgrenze_KV_PV * PV_AG_anteil
    else:
        KV = st_sv_gehalt * KV_AN_anteil
        PV_AN = st_sv_gehalt * PV_AN_anteil
        PV_AG = st_sv_gehalt * PV_AG_anteil
    
    sv_AN_anteil = RV + AV + KV + PV_AN
    sv_AG_anteil = RV + AV + KV + PV_AG
    sv_anteil = sv_AN_anteil + sv_AG_anteil
    nettogehalt = st_sv_gehalt - steuern - sv_AN_anteil
    
    ueberweisungbetrag = nettogehalt - vS - vorschuss

    #Ausgaben
    print(name )
    tool.dynammische_dezimal("Das Bruttogehalt", bruttogehalt, frac)
    tool.dynammische_dezimal("Der AG-Anteil der vermögenswirksamen Leistungen", vL_AG, frac)
    tool.dynammische_dezimal("Das Steuern und Sozialversicherungspflichtige Gehalt", st_sv_gehalt, frac)
    print("")
    tool.dynammische_dezimal("Die Lohnsteuer", lohnsteuer, frac)
    tool.dynammische_dezimal("Die Kirchensteuer", KiSt_euro, frac)
    print("")
    tool.dynammische_dezimal("KV", KV, frac)
    tool.dynammische_dezimal("RV", RV, frac)
    tool.dynammische_dezimal("AV", AV, frac)
    tool.dynammische_dezimal("PV-AN", PV_AN, frac)
    print("")
    tool.dynammische_dezimal("Das Nettogehalt", nettogehalt, frac)
    tool.dynammische_dezimal("Das vermögenswirksame Sparen", vS, frac)
    tool.dynammische_dezimal("Der Vorschuss", vorschuss, frac)
    print("")
    tool.dynammische_dezimal("Der Überweisungsbetrag", ueberweisungbetrag, frac)
    
    #Buchungssätze
    print(f"1. Buchung der Abführung der Sozialversicherungsbeitraäge. ")
    print("")
    print(f"2640 SV-Vorrauszahlung {sv_anteil:,.{frac}f} € ")
    print(f"   an 2800 Bank {sv_anteil:,.{frac}f} € ")
    print("")

    print(f"2. Buchung des Gehalts. ")
    print("")
    print(f"6300 Gehälter {st_sv_gehalt:,.{frac}f} € ")
    print(f"   an 2800 Bank {ueberweisungbetrag:,.{frac}f} € ")
    print(f"   an 4830 sonstige Verb gegenüber FB {steuern:,.{frac}f} € ")
    print(f"   an 2640 SV-Vorrauszahlung {sv_AN_anteil:,.{frac}f} € ")
    print(f"   an 2650 Vorschüsse {vorschuss:,.{frac}f} € ")
    print(f"   an 4860 Verb aus vL {vS:,.{frac}f} € ")
    print("")

    print(f"3. Buchung des Arbeitgeberanteils zur Sozialversicherung. ")
    print("")
    print(f"6400 Arbeitgeberanteil zur SV {sv_AG_anteil:,.{frac}f} € ")
    print(f"   an 2640 SV-Vorrauszahlung {sv_AG_anteil:,.{frac}f} € ")
    print("")

    print(f"4. Buchung der Abführung der Lohn- und Kirchensteuer. ")
    print("")
    print(f"4830 sonstige Verb gegenüber FB {steuern:,.{frac}f} € ")
    print(f"4860 Verb aus vL {vS:,.{frac}f} € ")
    print(f"   an 2800 Bank {(steuern + vS):,.{frac}f} € ")
    print("")
    return {
        "nettogehalt": nettogehalt,
        "ueberweisungbetrag": ueberweisungbetrag,
        "lohnsteur": lohnsteuer,
        "KiSt_euro":  KiSt_euro,
        "KV": KV,
        "RV": RV,
        "AV": AV,
        "PV_AN": PV_AN,
    }
    print("Programm beendet. ")