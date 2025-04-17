# logic.py
import random
from datetime import datetime
# Importa dati multilingua e funzioni di localizzazione
from tarot_data import MAZZO_STRUTTURA, get_tarot_meaning, get_tarot_card_display_name
from astrology_data import get_zodiac_meaning
from localization import (
    get_string, get_display_sign_name, get_orientation_string,
    DEFAULT_LANG
)

def crea_mazzo_completo():
    """ Crea una copia fresca del mazzo di tarocchi. """
    return MAZZO_STRUTTURA[:] # Ritorna una copia

def mischia_mazzo(mazzo):
    """ Mischia il mazzo di carte in modo casuale. """
    random.shuffle(mazzo)

def estrai_carte(mazzo, numero_carte=3):
    """ Estrae un numero specificato di carte dal mazzo mischiato. """
    estratte = []
    if len(mazzo) < numero_carte:
        print("Errore: Non ci sono abbastanza carte nel mazzo.")
        # Potrebbe essere meglio sollevare un'eccezione qui
        return []
    for _ in range(numero_carte):
        carta_info = mazzo.pop(0) # Prende la carta dalla cima
        # L'orientamento interno resta 'dritto'/'rovescio'
        orientamento = random.choice(['dritto', 'rovescio'])
        estratte.append({
            'carta_info': carta_info, # Contiene nome_it, nome_en, arcano, seme etc.
            'orientamento': orientamento # 'dritto' o 'rovescio'
            })
    return estratte

def get_segno_solare(data):
    """
    Calcola il segno zodiacale basandosi sul giorno e mese.
    Ritorna la chiave interna (nome italiano).
    """
    giorno = data.day
    mese = data.month
    # Mappatura date -> chiave interna segno (italiano)
    if (mese == 3 and giorno >= 21) or (mese == 4 and giorno <= 19): return "Ariete"
    if (mese == 4 and giorno >= 20) or (mese == 5 and giorno <= 20): return "Toro"
    if (mese == 5 and giorno >= 21) or (mese == 6 and giorno <= 20): return "Gemelli"
    if (mese == 6 and giorno >= 21) or (mese == 7 and giorno <= 22): return "Cancro"
    if (mese == 7 and giorno >= 23) or (mese == 8 and giorno <= 22): return "Leone"
    if (mese == 8 and giorno >= 23) or (mese == 9 and giorno <= 22): return "Vergine"
    if (mese == 9 and giorno >= 23) or (mese == 10 and giorno <= 22): return "Bilancia"
    if (mese == 10 and giorno >= 23) or (mese == 11 and giorno <= 21): return "Scorpione"
    if (mese == 11 and giorno >= 22) or (mese == 12 and giorno <= 21): return "Sagittario"
    if (mese == 12 and giorno >= 22) or (mese == 1 and giorno <= 19): return "Capricorno"
    if (mese == 1 and giorno >= 20) or (mese == 2 and giorno <= 18): return "Acquario"
    if (mese == 2 and giorno >= 19) or (mese == 3 and giorno <= 20): return "Pesci"
    return "Sconosciuto" # Chiave interna per sconosciuto

def genera_report_proiezione(dati_progetto, lang=DEFAULT_LANG):
    """
    Genera il report testuale combinando Tarocchi e Astrologia nella lingua specificata.
    'dati_progetto' è un dizionario che contiene tutte le informazioni necessarie.
    'lang' è il codice della lingua (es. 'it', 'en').
    """
    nome_progetto = dati_progetto['nome']
    descrizione = dati_progetto['descrizione']
    data_inizio = dati_progetto['data_inizio']
    num_partecipanti = dati_progetto['num_partecipanti']
    # La lista contiene le chiavi interne (italiano) dei segni
    segni_partecipanti_keys = dati_progetto['segni_partecipanti_keys']

    # 1. Preparazione Tarocchi
    mazzo = crea_mazzo_completo()
    mischia_mazzo(mazzo)
    # Usiamo una stesa a 3 carte: Contesto, Azione/Sfida, Prospettiva
    carte_estratte = estrai_carte(mazzo, 3)
    if not carte_estratte:
        # Usare una stringa localizzata per l'errore sarebbe meglio,
        # ma questo errore è più per il log che per l'utente finale GUI.
        return f"Error [{lang}]: Cannot draw Tarot cards."

    # 2. Analisi Astrologica
    segno_solare_progetto_key = get_segno_solare(data_inizio)
    significato_segno_progetto = get_zodiac_meaning(segno_solare_progetto_key, lang)
    display_segno_progetto = get_display_sign_name(segno_solare_progetto_key, lang)

    # 3. Costruzione del Report usando get_string per la localizzazione
    report = get_string("report_main_title", lang, nome_progetto) + "\n\n"
    report += f"{get_string('report_description', lang)}: {descrizione}\n"
    report += f"{get_string('report_start_date', lang)}: {data_inizio.strftime('%d-%m-%Y')}\n"
    report += f"{get_string('report_participants_num', lang)}: {num_partecipanti}\n"

    # Ottieni i nomi visualizzati dei segni dei partecipanti per il report
    segni_display = [get_display_sign_name(key, lang) for key in segni_partecipanti_keys]
    report += f"{get_string('report_participants_signs', lang)}: {', '.join(segni_display) if segni_display else get_string('NA', lang)}\n\n"

    # Localizza i nomi delle posizioni della stesa
    pos1_name = get_string("report_tarot_pos1", lang)
    pos2_name = get_string("report_tarot_pos2", lang)
    pos3_name = get_string("report_tarot_pos3", lang)
    report += get_string("report_tarot_header", lang, pos1_name, pos2_name, pos3_name) + "\n"

    posizioni_stesa = [f"1. {pos1_name}", f"2. {pos2_name}", f"3. {pos3_name}"]

    for i, estrazione in enumerate(carte_estratte):
        carta_info = estrazione['carta_info']
        orientamento_key = estrazione['orientamento'] # 'dritto' o 'rovescio'
        nome_carta_it = carta_info['nome'] # Chiave interna per i significati

        # Ottieni nome visualizzato e significato nella lingua corretta
        nome_carta_display = get_tarot_card_display_name(carta_info, lang)
        orientamento_display = get_orientation_string(orientamento_key, lang)
        significato = get_tarot_meaning(nome_carta_it, orientamento_key, lang)

        report += f"{posizioni_stesa[i]} ({nome_carta_display} - {orientamento_display}):\n   {significato}\n\n"

    report += get_string("report_astro_header", lang) + "\n"
    report += get_string("report_astro_project_sign", lang, display_segno_progetto) + ":\n"
    report += f"   {significato_segno_progetto}\n\n"

    if segni_partecipanti_keys:
        report += get_string("report_astro_team_dynamics", lang, num_partecipanti) + ":\n"
        # Conteggio basato sulle chiavi interne
        conteggio_segni = {key: segni_partecipanti_keys.count(key) for key in set(segni_partecipanti_keys)}
        for segno_key, count in conteggio_segni.items():
            prefisso_conteggio = f"{count}x " if count > 1 else ""
            display_segno = get_display_sign_name(segno_key, lang)
            significato_segno = get_zodiac_meaning(segno_key, lang)
            report += f"- {prefisso_conteggio}{display_segno}: {significato_segno}\n"
        report += f"\n   {get_string('report_astro_team_reflection', lang)}\n\n"
    else:
        report += get_string("report_astro_no_participants", lang) + "\n\n"

    report += get_string("report_final_thoughts_header", lang) + "\n"
    report += get_string("report_disclaimer", lang) + "\n"

    return report