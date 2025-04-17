# localization.py

# Supported languages
LANGUAGES = {
    "it": "Italiano",
    "en": "English"
}
DEFAULT_LANG = "it"
CURRENT_LANG = DEFAULT_LANG

# --- General UI and Report Strings ---
STRINGS = {
    "window_title": {
        "it": "Proiettore Tarocchi & Astrologia per Progetti",
        "en": "Tarot & Astrology Project Projector"
    },
    "project_data_frame": {
        "it": "Dati del Progetto",
        "en": "Project Data"
    },
    "label_project_name": {
        "it": "Nome Progetto:",
        "en": "Project Name:"
    },
    "label_description": {
        "it": "Breve Descrizione:",
        "en": "Brief Description:"
    },
    "label_start_date": {
        "it": "Data Inizio (YYYY-MM-DD):",
        "en": "Start Date (YYYY-MM-DD):"
    },
    "label_participants_num": {
        "it": "Numero Partecipanti:",
        "en": "Number of Participants:"
    },
    "label_participants_signs": {
        "it": "Segni Zodiacali Partecipanti:",
        "en": "Participant Zodiac Signs:"
    },
    "label_signs_example": {
        "it": "(Es: Ariete, Toro, Gemelli)",
        "en": "(Ex: Aries, Taurus, Gemini)"
    },
    "generate_button": {
        "it": "✨ Genera Proiezione ✨",
        "en": "✨ Generate Projection ✨"
    },
    "output_frame": {
        "it": "Risultato Proiezione",
        "en": "Projection Result"
    },
    "generating_message_astro": {
        "it": "Ricerca posizionamento astri.\n",
        "en": "Searching for star positions.\n"
    },
    "generating_message_shuffle": {
        "it": "Mescolamento mazzo.\n",
        "en": "Shuffling the deck.\n"
    },
    "generating_message_draw": {
        "it": "Estrazione delle carte.\n",
        "en": "Drawing the cards.\n"
    },
    "error_input_title": {
        "it": "Errore Input",
        "en": "Input Error"
    },
    "error_project_name_required": {
        "it": "Il nome del progetto è obbligatorio.",
        "en": "Project name is required."
    },
    "error_invalid_date": {
        "it": "Formato data non valido. Usare YYYY-MM-DD.",
        "en": "Invalid date format. Use YYYY-MM-DD."
    },
    "error_invalid_participants_num": {
        "it": "Numero partecipanti deve essere un numero intero non negativo.",
        "en": "Number of participants must be a non-negative integer."
    },
    "warning_signs_title": {
        "it": "Attenzione Segni",
        "en": "Signs Warning"
    },
    "warning_unrecognized_signs": {
        "it": "I seguenti segni non sono stati riconosciuti e verranno ignorati: {}",
        "en": "The following signs were not recognized and will be ignored: {}"
    },
    "info_participants_title": {
        "it": "Info Partecipanti",
        "en": "Participants Info"
    },
    "info_participants_mismatch": {
        "it": "Hai inserito {} partecipanti ma fornito {} segni validi.",
        "en": "You entered {} participants but provided {} valid signs."
    },
    "error_processing_title": {
        "it": "Errore Elaborazione",
        "en": "Processing Error"
    },
    "error_processing_message": {
        "it": "Si è verificato un errore durante la generazione del report:\n{}",
        "en": "An error occurred while generating the report:\n{}"
    },
    "error_processing_fallback": {
        "it": "Errore durante l'elaborazione.",
        "en": "Error during processing."
    },
    "report_main_title": {
        "it": "--- Proiezione Simbolica per il Progetto: {} ---",
        "en": "--- Symbolic Projection for Project: {} ---"
    },
    "report_description": {
        "it": "Descrizione",
        "en": "Description"
    },
    "report_start_date": {
        "it": "Data Inizio Prevista",
        "en": "Planned Start Date"
    },
    "report_participants_num": {
        "it": "Numero Partecipanti",
        "en": "Number of Participants"
    },
    "report_participants_signs": {
        "it": "Segni Zodiacali Partecipanti",
        "en": "Participant Zodiac Signs"
    },
    "report_tarot_header": {
        "it": "*** Interpretazione Tarocchi ({}, {}, {}) ***",
        "en": "*** Tarot Interpretation ({}, {}, {}) ***"
    },
    "report_tarot_pos1": {
        "it": "Contesto Energetico",
        "en": "Energetic Context"
    },
    "report_tarot_pos2": {
        "it": "Azione Consigliata / Sfida Chiave",
        "en": "Recommended Action / Key Challenge"
    },
    "report_tarot_pos3": {
        "it": "Prospettiva / Esito Potenziale",
        "en": "Outlook / Potential Outcome"
    },
    "report_card_orientation_upright": {
        "it": "Dritto",
        "en": "Upright"
    },
    "report_card_orientation_reversed": {
        "it": "Rovescio",
        "en": "Reversed"
    },
    "report_astro_header": {
        "it": "*** Influenze Astrologiche ***",
        "en": "*** Astrological Influences ***"
    },
    "report_astro_project_sign": {
        "it": "Energia di Partenza del Progetto (Segno Solare: {})",
        "en": "Project Starting Energy (Sun Sign: {})"
    },
    "report_astro_team_dynamics": {
        "it": "Dinamiche del Team (basate sui segni dei {} partecipanti)",
        "en": "Team Dynamics (based on the signs of the {} participants)"
    },
    "report_astro_team_reflection": {
        "it": "Riflessione: Considera come queste diverse energie interagiscono. Ci sono sinergie naturali o potenziali aree di attrito/complementarità?",
        "en": "Reflection: Consider how these different energies interact. Are there natural synergies or potential areas of friction/complementarity?"
    },
    "report_astro_no_participants": {
        "it": "Nessuna informazione sui partecipanti fornita per analizzare le dinamiche del team.",
        "en": "No participant information provided to analyze team dynamics."
    },
    "report_final_thoughts_header": {
        "it": "*** Considerazioni Finali ***",
        "en": "*** Final Considerations ***"
    },
    "report_disclaimer": {
        "it": "Questo report offre spunti simbolici basati su Tarocchi e Astrologia. Non sostituisce la pianificazione strategica, l'analisi dei rischi concreta o la gestione attiva del progetto. Usa queste indicazioni come strumento di riflessione per esplorare le dinamiche energetiche, i potenziali punti di forza e le aree che potrebbero richiedere maggiore attenzione.",
        "en": "This report offers symbolic insights based on Tarot and Astrology. It does not replace strategic planning, concrete risk analysis, or active project management. Use these indications as a reflective tool to explore energetic dynamics, potential strengths, and areas that might require more attention."
    },
    "orientation_upright_internal": { # Internal mapping key
        "it": "dritto",
        "en": "upright"
    },
    "orientation_reversed_internal": {
        "it": "rovescio",
        "en": "reversed"
    },
     "unknown_sign": {
        "it": "Sconosciuto",
        "en": "Unknown"
    },
    "NA": {
        "it": "N/D",
        "en": "N/A"
    },
     "language_select_label": {
        "it": "Lingua:",
        "en": "Language:"
    },

}

def set_language(lang_code):
    """Sets the current language."""
    global CURRENT_LANG
    if lang_code in LANGUAGES:
        CURRENT_LANG = lang_code
    else:
        print(f"Warning: Language '{lang_code}' not supported. Using default '{DEFAULT_LANG}'.")
        CURRENT_LANG = DEFAULT_LANG

def get_string(key, lang=None, *args):
    """Gets the translated string for a given key and language."""
    if lang is None:
        lang = CURRENT_LANG

    try:
        base_string = STRINGS[key][lang]
        return base_string.format(*args) if args else base_string
    except KeyError:
        # Fallback to default language if translation is missing
        try:
            print(f"Warning: Translation missing for key '{key}' in language '{lang}'. Falling back to '{DEFAULT_LANG}'.")
            base_string = STRINGS[key][DEFAULT_LANG]
            return base_string.format(*args) if args else base_string
        except KeyError:
            print(f"Error: String key '{key}' not found in any language.")
            return f"<{key}>" # Return the key as a placeholder

# --- Mappings for data (Zodiac signs) ---
# Store internal keys (Italian) mapped to display names
ZODIAC_DISPLAY_NAMES = {
    "Ariete": {"it": "Ariete", "en": "Aries"},
    "Toro": {"it": "Toro", "en": "Taurus"},
    "Gemelli": {"it": "Gemelli", "en": "Gemini"},
    "Cancro": {"it": "Cancro", "en": "Cancer"},
    "Leone": {"it": "Leone", "en": "Leo"},
    "Vergine": {"it": "Vergine", "en": "Virgo"},
    "Bilancia": {"it": "Bilancia", "en": "Libra"},
    "Scorpione": {"it": "Scorpione", "en": "Scorpio"},
    "Sagittario": {"it": "Sagittario", "en": "Sagittarius"},
    "Capricorno": {"it": "Capricorno", "en": "Capricorn"},
    "Acquario": {"it": "Acquario", "en": "Aquarius"},
    "Pesci": {"it": "Pesci", "en": "Pisces"},
    "Sconosciuto": {"it": "Sconosciuto", "en": "Unknown"}
}

# Create reverse mapping: Display Name (lowercase) -> Internal Key
# This is needed for parsing user input in the GUI
INTERNAL_SIGN_KEYS = {}
for internal_key, names in ZODIAC_DISPLAY_NAMES.items():
    for lang_code, display_name in names.items():
        INTERNAL_SIGN_KEYS[(display_name.lower(), lang_code)] = internal_key

def get_display_sign_name(internal_key, lang=None):
    """Gets the display name for a zodiac sign internal key."""
    if lang is None:
        lang = CURRENT_LANG
    return ZODIAC_DISPLAY_NAMES.get(internal_key, ZODIAC_DISPLAY_NAMES["Sconosciuto"]).get(lang, internal_key)

def get_internal_sign_key(display_name, lang=None):
    """Gets the internal key from a display name (case-insensitive)."""
    if lang is None:
        lang = CURRENT_LANG
    return INTERNAL_SIGN_KEYS.get((display_name.lower(), lang), "Sconosciuto")

def get_valid_sign_display_names(lang=None):
    """Returns a list of valid sign display names for the given language."""
    if lang is None:
        lang = CURRENT_LANG
    # Exclude "Sconosciuto"
    return [names[lang] for key, names in ZODIAC_DISPLAY_NAMES.items() if key != "Sconosciuto"]

def get_orientation_string(internal_orientation_key, lang=None):
    """Gets the display string for card orientation (e.g., 'dritto' -> 'Upright')."""
    if lang is None:
        lang = CURRENT_LANG
    if internal_orientation_key == 'dritto':
        return get_string('report_card_orientation_upright', lang)
    elif internal_orientation_key == 'rovescio':
        return get_string('report_card_orientation_reversed', lang)
    else:
        return internal_orientation_key # Fallback