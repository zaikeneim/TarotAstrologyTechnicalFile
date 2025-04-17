# numerology_data.py
# Uses string keys for numbers for consistency, includes 0 for edge cases.

NUMEROLOGY_MEANINGS_MULTI = {
    "1": {
        "it": "Iniziativa, Leadership, Indipendenza, Originalità. Progetto: Energia di avvio, necessità di un leader chiaro, approccio pionieristico, potenziale per l'innovazione.",
        "en": "Initiative, Leadership, Independence, Originality. Project: Starting energy, need for a clear leader, pioneering approach, potential for innovation."
    },
    "2": {
        "it": "Collaborazione, Diplomazia, Sensibilità, Cooperazione. Progetto: Importanza del lavoro di squadra, necessità di equilibrio e armonia, partnership chiave, sensibilità alle dinamiche interpersonali.",
        "en": "Collaboration, Diplomacy, Sensitivity, Cooperation. Project: Importance of teamwork, need for balance and harmony, key partnerships, sensitivity to interpersonal dynamics."
    },
    "3": {
        "it": "Creatività, Comunicazione, Espressione, Ottimismo. Progetto: Enfasi sulla comunicazione e presentazione, potenziale creativo, necessità di esprimere idee chiaramente, ambiente gioioso.",
        "en": "Creativity, Communication, Expression, Optimism. Project: Emphasis on communication and presentation, creative potential, need to express ideas clearly, joyful environment."
    },
    "4": {
        "it": "Struttura, Stabilità, Lavoro Pratico, Disciplina. Progetto: Necessità di pianificazione solida, attenzione ai dettagli pratici, costruzione di basi sicure, lavoro metodico.",
        "en": "Structure, Stability, Practical Work, Discipline. Project: Need for solid planning, attention to practical details, building secure foundations, methodical work."
    },
    "5": {
        "it": "Cambiamento, Libertà, Adattabilità, Versatilità. Progetto: Dinamismo, necessità di flessibilità, potenziali cambiamenti di direzione, spirito avventuroso, gestione della varietà.",
        "en": "Change, Freedom, Adaptability, Versatility. Project: Dynamism, need for flexibility, potential changes in direction, adventurous spirit, managing variety."
    },
    "6": {
        "it": "Responsabilità, Armonia, Servizio, Cura. Progetto: Focus sul benessere del team/comunità, responsabilità sociale, ricerca di equilibrio e bellezza, attenzione ai dettagli estetici/etici.",
        "en": "Responsibility, Harmony, Service, Care. Project: Focus on team/community well-being, social responsibility, seeking balance and beauty, attention to aesthetic/ethical details."
    },
    "7": {
        "it": "Analisi, Introspezione, Ricerca, Saggezza. Progetto: Necessità di analisi approfondita, ricerca e sviluppo, focus sulla conoscenza, potenziale per specializzazione, introspezione strategica.",
        "en": "Analysis, Introspection, Research, Wisdom. Project: Need for in-depth analysis, research and development, focus on knowledge, potential for specialization, strategic introspection."
    },
    "8": {
        "it": "Ambizione, Potere, Successo Materiale, Organizzazione. Progetto: Orientato agli obiettivi e ai risultati tangibili, potenziale per grande successo, gestione efficace delle risorse, leadership forte.",
        "en": "Ambition, Power, Material Success, Organization. Project: Goal-oriented towards tangible results, potential for great success, effective resource management, strong leadership."
    },
    "9": {
        "it": "Completamento, Umanitarismo, Compassione, Visione Globale. Progetto: Fase di conclusione o impatto ampio, focus sul beneficio collettivo, visione a lungo termine, necessità di lasciare andare.",
        "en": "Completion, Humanitarianism, Compassion, Global Vision. Project: Completion phase or broad impact, focus on collective benefit, long-term vision, need for letting go."
    },
    "11": {
        "it": "Intuizione, Ispirazione, Idealismo, Visione (Maestro). Progetto: Potenziale visionario elevato, necessità di seguire l'intuizione, ispirazione elevata, sfide nel rendere concreto l'ideale.",
        "en": "Intuition, Inspiration, Idealism, Vision (Master). Project: High visionary potential, need to follow intuition, elevated inspiration, challenges in making the ideal concrete."
    },
    "22": {
        "it": "Costruttore Maestro, Grandi Realizzazioni, Pragmatismo Visionario. Progetto: Potenziale per costruire qualcosa di duraturo e di grande impatto, capacità di unire visione e pratica, grandi sfide.",
        "en": "Master Builder, Great Achievements, Visionary Pragmatism. Project: Potential to build something lasting and impactful, ability to unite vision and practice, significant challenges."
    },
    "33": {
        "it": "Maestro Guida/Guaritore, Compassione Elevata, Ispirazione Collettiva. Progetto: Focus sull'insegnamento, la guida o il benessere collettivo su larga scala, potenziale di grande ispirazione, responsabilità elevata.",
        "en": "Master Teacher/Healer, Elevated Compassion, Collective Inspiration. Project: Focus on teaching, guiding, or large-scale collective well-being, potential for great inspiration, high responsibility."
    },
    "0": {  # Handle case where input might be empty or non-alphabetic
        "it": "Nessun valore calcolabile (input vuoto o non alfabetico).",
        "en": "No calculable value (empty or non-alphabetic input)."
    }
}


def get_numerology_meaning(number, lang):
    """ Recupera il significato di un numero nella lingua specificata. """
    # Convert number to string for dictionary lookup
    number_str = str(number)
    meanings = NUMEROLOGY_MEANINGS_MULTI.get(number_str,
                                             NUMEROLOGY_MEANINGS_MULTI["0"])  # Default to 0 if number somehow not found
    return meanings.get(lang, meanings.get("en"))  # Fallback to English

