# astrology_data.py
from localization import get_string # Import for unknown sign translation

# Significati dei segni zodiacali in entrambe le lingue
# Le chiavi sono ora i nomi italiani (usati internamente)
# Ogni segno ha un dizionario con 'it' e 'en' per i significati
ZODIAC_MEANINGS_MULTI = {
    "Ariete": {
        "it": "Energia iniziale, leadership, coraggio, impulsività. Nel progetto: Ottimo per l'avvio, spinta all'azione, ma attenzione alla pianificazione e alla collaborazione.",
        "en": "Initial energy, leadership, courage, impulsiveness. In the project: Great for starting, drive to action, but careful with planning and collaboration."
    },
    "Toro": {
        "it": "Stabilità, praticità, perseveranza, resistenza al cambiamento. Nel progetto: Costruisce basi solide, affidabile, ma può essere lento o testardo.",
        "en": "Stability, practicality, perseverance, resistance to change. In the project: Builds solid foundations, reliable, but can be slow or stubborn."
    },
    "Gemelli": {
        "it": "Comunicazione, adattabilità, curiosità, dispersione. Nel progetto: Facilita lo scambio di idee, multitasking, ma rischia di mancare di focus.",
        "en": "Communication, adaptability, curiosity, dispersion. In the project: Facilitates idea exchange, multitasking, but risks lacking focus."
    },
    "Cancro": {
        "it": "Intuizione, sensibilità, protezione, umoralità. Nel progetto: Crea un ambiente di supporto, attento al team, ma può essere troppo emotivo o chiuso.",
        "en": "Intuition, sensitivity, protection, moodiness. In the project: Creates a supportive environment, attentive to the team, but can be too emotional or closed off."
    },
    "Leone": {
        "it": "Creatività, leadership carismatica, generosità, egocentrismo. Nel progetto: Ispira il team, porta visibilità, ma può voler essere troppo al centro dell'attenzione.",
        "en": "Creativity, charismatic leadership, generosity, egocentrism. In the project: Inspires the team, brings visibility, but may want too much attention."
    },
    "Vergine": {
        "it": "Analisi, organizzazione, precisione, critica eccessiva. Nel progetto: Eccellente per i dettagli, la pianificazione e il controllo qualità, ma può essere troppo pignolo.",
        "en": "Analysis, organization, precision, excessive criticism. In the project: Excellent for details, planning, and quality control, but can be too picky."
    },
    "Bilancia": {
        "it": "Diplomazia, collaborazione, armonia, indecisione. Nel progetto: Facilita il lavoro di squadra e le partnership, cerca l'equilibrio, ma fatica a prendere decisioni difficili.",
        "en": "Diplomacy, collaboration, harmony, indecision. In the project: Facilitates teamwork and partnerships, seeks balance, but struggles with difficult decisions."
    },
    "Scorpione": {
        "it": "Intensità, determinazione, investigazione, segretezza/controllo. Nel progetto: Va a fondo dei problemi, trasformativo, ma può essere troppo intenso o sospettoso.",
        "en": "Intensity, determination, investigation, secrecy/control. In the project: Gets to the bottom of problems, transformative, but can be too intense or suspicious."
    },
    "Sagittario": {
        "it": "Ottimismo, visione, esplorazione, mancanza di realismo. Nel progetto: Porta entusiasmo e guarda al futuro, ma può trascurare i dettagli pratici.",
        "en": "Optimism, vision, exploration, lack of realism. In the project: Brings enthusiasm and looks to the future, but may overlook practical details."
    },
    "Capricorno": {
        "it": "Disciplina, responsabilità, ambizione, pessimismo/rigidità. Nel progetto: Struttura solida, orientato agli obiettivi a lungo termine, ma può essere troppo rigido o severo.",
        "en": "Discipline, responsibility, ambition, pessimism/rigidity. In the project: Solid structure, long-term goal-oriented, but can be too rigid or severe."
    },
    "Acquario": {
        "it": "Innovazione, originalità, visione collettiva, distacco/imprevedibilità. Nel progetto: Porta idee fuori dagli schemi, orientato al gruppo, ma può essere poco convenzionale o distante.",
        "en": "Innovation, originality, collective vision, detachment/unpredictability. In the project: Brings unconventional ideas, group-oriented, but can be unconventional or distant."
    },
    "Pesci": {
        "it": "Intuizione, compassione, creatività artistica, evasione/caos. Nel progetto: Sensibile alle dinamiche di gruppo, porta creatività fluida, ma può mancare di struttura o confini.",
        "en": "Intuition, compassion, artistic creativity, escapism/chaos. In the project: Sensitive to group dynamics, brings fluid creativity, but may lack structure or boundaries."
    },
    "Sconosciuto": {
        "it": "Segno non valido o non fornito.",
        "en": "Invalid or not provided sign."
        # We could use get_string here too, but keeping it simple
    }
}

def get_zodiac_meaning(internal_sign_key, lang):
    """ Recupera il significato di un segno zodiacale nella lingua specificata. """
    meanings = ZODIAC_MEANINGS_MULTI.get(internal_sign_key, ZODIAC_MEANINGS_MULTI["Sconosciuto"])
    return meanings.get(lang, meanings.get("en")) # Fallback to English if lang specific not found

# Web scraping part remains commented out / conceptual