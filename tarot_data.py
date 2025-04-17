# tarot_data.py
from localization import get_string # Import for fallback message

# Struttura base del mazzo con nomi italiani (chiave) e inglesi
MAZZO_STRUTTURA = [
    # Arcani Maggiori
    {'nome': 'Il Matto', 'nome_en': 'The Fool', 'arcano': 'Maggiore', 'numero': 0},
    {'nome': 'Il Mago', 'nome_en': 'The Magician', 'arcano': 'Maggiore', 'numero': 1},
    {'nome': 'La Papessa', 'nome_en': 'The High Priestess', 'arcano': 'Maggiore', 'numero': 2},
    {'nome': 'L\'Imperatrice', 'nome_en': 'The Empress', 'arcano': 'Maggiore', 'numero': 3},
    {'nome': 'L\'Imperatore', 'nome_en': 'The Emperor', 'arcano': 'Maggiore', 'numero': 4},
    {'nome': 'Il Papa', 'nome_en': 'The Hierophant', 'arcano': 'Maggiore', 'numero': 5},
    {'nome': 'Gli Amanti', 'nome_en': 'The Lovers', 'arcano': 'Maggiore', 'numero': 6},
    {'nome': 'Il Carro', 'nome_en': 'The Chariot', 'arcano': 'Maggiore', 'numero': 7},
    {'nome': 'La Giustizia', 'nome_en': 'Justice', 'arcano': 'Maggiore', 'numero': 8},
    {'nome': 'L\'Eremita', 'nome_en': 'The Hermit', 'arcano': 'Maggiore', 'numero': 9},
    {'nome': 'La Ruota della Fortuna', 'nome_en': 'Wheel of Fortune', 'arcano': 'Maggiore', 'numero': 10},
    {'nome': 'La Forza', 'nome_en': 'Strength', 'arcano': 'Maggiore', 'numero': 11},
    {'nome': 'L\'Appeso', 'nome_en': 'The Hanged Man', 'arcano': 'Maggiore', 'numero': 12},
    {'nome': 'La Morte', 'nome_en': 'Death', 'arcano': 'Maggiore', 'numero': 13},
    {'nome': 'La Temperanza', 'nome_en': 'Temperance', 'arcano': 'Maggiore', 'numero': 14},
    {'nome': 'Il Diavolo', 'nome_en': 'The Devil', 'arcano': 'Maggiore', 'numero': 15},
    {'nome': 'La Torre', 'nome_en': 'The Tower', 'arcano': 'Maggiore', 'numero': 16},
    {'nome': 'Le Stelle', 'nome_en': 'The Star', 'arcano': 'Maggiore', 'numero': 17},
    {'nome': 'La Luna', 'nome_en': 'The Moon', 'arcano': 'Maggiore', 'numero': 18},
    {'nome': 'Il Sole', 'nome_en': 'The Sun', 'arcano': 'Maggiore', 'numero': 19},
    {'nome': 'Il Giudizio', 'nome_en': 'Judgement', 'arcano': 'Maggiore', 'numero': 20},
    {'nome': 'Il Mondo', 'nome_en': 'The World', 'arcano': 'Maggiore', 'numero': 21},

    # Arcani Minori - Bastoni / Wands
    {'nome': 'Asso di Bastoni', 'nome_en': 'Ace of Wands', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 1},
    {'nome': 'Due di Bastoni', 'nome_en': 'Two of Wands', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 2},
    {'nome': 'Tre di Bastoni', 'nome_en': 'Three of Wands', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 3},
    {'nome': 'Quattro di Bastoni', 'nome_en': 'Four of Wands', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 4},
    {'nome': 'Cinque di Bastoni', 'nome_en': 'Five of Wands', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 5},
    {'nome': 'Sei di Bastoni', 'nome_en': 'Six of Wands', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 6},
    {'nome': 'Sette di Bastoni', 'nome_en': 'Seven of Wands', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 7},
    {'nome': 'Otto di Bastoni', 'nome_en': 'Eight of Wands', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 8},
    {'nome': 'Nove di Bastoni', 'nome_en': 'Nine of Wands', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 9},
    {'nome': 'Dieci di Bastoni', 'nome_en': 'Ten of Wands', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 10},
    {'nome': 'Fante di Bastoni', 'nome_en': 'Page of Wands', 'arcano': 'Minore', 'seme': 'Bastoni', 'figura': 'Fante'},
    {'nome': 'Cavaliere di Bastoni', 'nome_en': 'Knight of Wands', 'arcano': 'Minore', 'seme': 'Bastoni', 'figura': 'Cavaliere'},
    {'nome': 'Regina di Bastoni', 'nome_en': 'Queen of Wands', 'arcano': 'Minore', 'seme': 'Bastoni', 'figura': 'Regina'},
    {'nome': 'Re di Bastoni', 'nome_en': 'King of Wands', 'arcano': 'Minore', 'seme': 'Bastoni', 'figura': 'Re'},

    # Arcani Minori - Coppe / Cups
    {'nome': 'Asso di Coppe', 'nome_en': 'Ace of Cups', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 1},
    {'nome': 'Due di Coppe', 'nome_en': 'Two of Cups', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 2},
    {'nome': 'Tre di Coppe', 'nome_en': 'Three of Cups', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 3},
    {'nome': 'Quattro di Coppe', 'nome_en': 'Four of Cups', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 4},
    {'nome': 'Cinque di Coppe', 'nome_en': 'Five of Cups', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 5},
    {'nome': 'Sei di Coppe', 'nome_en': 'Six of Cups', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 6},
    {'nome': 'Sette di Coppe', 'nome_en': 'Seven of Cups', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 7},
    {'nome': 'Otto di Coppe', 'nome_en': 'Eight of Cups', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 8},
    {'nome': 'Nove di Coppe', 'nome_en': 'Nine of Cups', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 9},
    {'nome': 'Dieci di Coppe', 'nome_en': 'Ten of Cups', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 10},
    {'nome': 'Fante di Coppe', 'nome_en': 'Page of Cups', 'arcano': 'Minore', 'seme': 'Coppe', 'figura': 'Fante'},
    {'nome': 'Cavaliere di Coppe', 'nome_en': 'Knight of Cups', 'arcano': 'Minore', 'seme': 'Coppe', 'figura': 'Cavaliere'},
    {'nome': 'Regina di Coppe', 'nome_en': 'Queen of Cups', 'arcano': 'Minore', 'seme': 'Coppe', 'figura': 'Regina'},
    {'nome': 'Re di Coppe', 'nome_en': 'King of Cups', 'arcano': 'Minore', 'seme': 'Coppe', 'figura': 'Re'},

    # Arcani Minori - Spade / Swords
    {'nome': 'Asso di Spade', 'nome_en': 'Ace of Swords', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 1},
    {'nome': 'Due di Spade', 'nome_en': 'Two of Swords', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 2},
    {'nome': 'Tre di Spade', 'nome_en': 'Three of Swords', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 3},
    {'nome': 'Quattro di Spade', 'nome_en': 'Four of Swords', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 4},
    {'nome': 'Cinque di Spade', 'nome_en': 'Five of Swords', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 5},
    {'nome': 'Sei di Spade', 'nome_en': 'Six of Swords', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 6},
    {'nome': 'Sette di Spade', 'nome_en': 'Seven of Swords', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 7},
    {'nome': 'Otto di Spade', 'nome_en': 'Eight of Swords', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 8},
    {'nome': 'Nove di Spade', 'nome_en': 'Nine of Swords', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 9},
    {'nome': 'Dieci di Spade', 'nome_en': 'Ten of Swords', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 10},
    {'nome': 'Fante di Spade', 'nome_en': 'Page of Swords', 'arcano': 'Minore', 'seme': 'Spade', 'figura': 'Fante'},
    {'nome': 'Cavaliere di Spade', 'nome_en': 'Knight of Swords', 'arcano': 'Minore', 'seme': 'Spade', 'figura': 'Cavaliere'},
    {'nome': 'Regina di Spade', 'nome_en': 'Queen of Swords', 'arcano': 'Minore', 'seme': 'Spade', 'figura': 'Regina'},
    {'nome': 'Re di Spade', 'nome_en': 'King of Swords', 'arcano': 'Minore', 'seme': 'Spade', 'figura': 'Re'},

    # Arcani Minori - Denari / Pentacles
    {'nome': 'Asso di Denari', 'nome_en': 'Ace of Pentacles', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 1},
    {'nome': 'Due di Denari', 'nome_en': 'Two of Pentacles', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 2},
    {'nome': 'Tre di Denari', 'nome_en': 'Three of Pentacles', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 3},
    {'nome': 'Quattro di Denari', 'nome_en': 'Four of Pentacles', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 4},
    {'nome': 'Cinque di Denari', 'nome_en': 'Five of Pentacles', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 5},
    {'nome': 'Sei di Denari', 'nome_en': 'Six of Pentacles', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 6},
    {'nome': 'Sette di Denari', 'nome_en': 'Seven of Pentacles', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 7},
    {'nome': 'Otto di Denari', 'nome_en': 'Eight of Pentacles', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 8},
    {'nome': 'Nove di Denari', 'nome_en': 'Nine of Pentacles', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 9},
    {'nome': 'Dieci di Denari', 'nome_en': 'Ten of Pentacles', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 10},
    {'nome': 'Fante di Denari', 'nome_en': 'Page of Pentacles', 'arcano': 'Minore', 'seme': 'Denari', 'figura': 'Fante'},
    {'nome': 'Cavaliere di Denari', 'nome_en': 'Knight of Pentacles', 'arcano': 'Minore', 'seme': 'Denari', 'figura': 'Cavaliere'},
    {'nome': 'Regina di Denari', 'nome_en': 'Queen of Pentacles', 'arcano': 'Minore', 'seme': 'Denari', 'figura': 'Regina'},
    {'nome': 'Re di Denari', 'nome_en': 'King of Pentacles', 'arcano': 'Minore', 'seme': 'Denari', 'figura': 'Re'},
]

# Significati multilingua. Chiave = nome italiano.
TAROT_MEANINGS_MULTI = {
    # --- ARCANI MAGGIORI ---
    "Il Matto": {
        "it": {
            "dritto": "Nuovo inizio, potenziale grezzo, fede nell'ignoto, innovazione. Progetto: Lancio audace, approccio non convenzionale, necessità di valutare i rischi, entusiasmo iniziale.",
            "rovescio": "Avventatezza, ingenuità, caos, paura di iniziare, mancanza di preparazione. Progetto: Piani irrealistici, decisioni impulsive, rischio non calcolato, blocco all'avvio."
        },
        "en": {
            "dritto": "New beginning, raw potential, faith in the unknown, innovation. Project: Bold launch, unconventional approach, need to assess risks, initial enthusiasm.",
            "rovescio": "Recklessness, naivety, chaos, fear of starting, lack of preparation. Project: Unrealistic plans, impulsive decisions, uncalculated risk, blocked start."
        }
    },
    "Il Mago": {
         "it": {
            "dritto": "Abilità, risorse disponibili, volontà, manifestazione, comunicazione efficace. Progetto: Avere gli strumenti/competenze, focus sull'obiettivo, capacità di trasformare idee in realtà.",
            "rovescio": "Manipolazione, talenti sprecati, inganno, mancanza di focus, cattiva comunicazione. Progetto: Risorse non utilizzate, piani confusi, potenziale inganno o mancanza di trasparenza."
        },
        "en": {
            "dritto": "Skill, available resources, willpower, manifestation, effective communication. Project: Having the tools/skills, focus on the goal, ability to turn ideas into reality.",
            "rovescio": "Manipulation, wasted talents, deception, lack of focus, poor communication. Project: Unused resources, confused plans, potential deception or lack of transparency."
        }
    },
    "La Papessa": {
        "it": {
            "dritto": "Intuizione, conoscenza nascosta, pazienza, mistero, introspezione. Progetto: Necessità di guardare oltre le apparenze, fidarsi dell'istinto, fase di studio o ricerca silenziosa.",
            "rovescio": "Segreti svelati, superficialità, ignorare l'intuizione, informazioni nascoste problematiche. Progetto: Mancanza di profondità nell'analisi, gossip, decisioni basate su dati incompleti."
        },
        "en": {
            "dritto": "Intuition, hidden knowledge, patience, mystery, introspection. Project: Need to look beyond appearances, trust intuition, phase of quiet study or research.",
            "rovescio": "Secrets revealed, superficiality, ignoring intuition, problematic hidden information. Project: Lack of depth in analysis, gossip, decisions based on incomplete data."
        }
    },
    "L'Imperatrice": {
        "it": {
            "dritto": "Creatività, nutrimento, abbondanza, fertilità, crescita. Progetto: Fase fertile e produttiva, ambiente di lavoro armonioso, sviluppo di idee, risultati tangibili.",
            "rovescio": "Blocco creativo, dipendenza, esaurimento risorse, sovra-controllo. Progetto: Creatività soffocata, problemi di budget/risorse, burnout, ambiente di lavoro opprimente."
        },
        "en": {
             "dritto": "Creativity, nurturing, abundance, fertility, growth. Project: Fertile and productive phase, harmonious work environment, development of ideas, tangible results.",
             "rovescio": "Creative block, dependence, resource depletion, over-control. Project: Stifled creativity, budget/resource problems, burnout, oppressive work environment."
        }
    },
    "L'Imperatore": {
        "it": {
            "dritto": "Autorità, struttura, controllo, stabilità, leadership. Progetto: Necessità di ordine e pianificazione, figura di leader forte, basi solide, rispetto delle regole.",
            "rovescio": "Autoritarismo, rigidità, mancanza di controllo, caos, abuso di potere. Progetto: Tyrannical leadership, excessive bureaucracy, lack of flexibility, rebellion against rules."
        },
        "en": {
            "dritto": "Authority, structure, control, stability, leadership. Project: Need for order and planning, strong leader figure, solid foundations, respect for rules.",
            "rovescio": "Authoritarianism, rigidity, lack of control, chaos, abuse of power. Project: Tyrannical leadership, excessive bureaucracy, lack of flexibility, rebellion against rules."
        }
    },
    "Il Papa": {
        "it": {
            "dritto": "Tradizione, conformità, guida spirituale/morale, istituzioni, apprendimento. Progetto: Seguire procedure consolidate, mentorship, importanza dei valori condivisi, consulenza esterna.",
            "rovescio": "Ribellione alle regole, sfidare le convenzioni, guida fuorviante, rigidità dogmatica. Progetto: Necessità di innovare oltre le norme, conflitto con la gerarchia, cattivi consigli."
        },
        "en": {
            "dritto": "Tradition, conformity, spiritual/moral guidance, institutions, learning. Project: Following established procedures, mentorship, importance of shared values, external consulting.",
            "rovescio": "Rebellion against rules, challenging conventions, misleading guidance, dogmatic rigidity. Project: Need to innovate beyond norms, conflict with hierarchy, bad advice."
        }
    },
    "Gli Amanti": {
        "it": {
            "dritto": "Scelte importanti, unione, partnership, valori, comunicazione. Progetto: Decisioni cruciali da prendere, importanza della collaborazione e dell'allineamento, definizione dei valori del progetto.",
            "rovescio": "Conflitto, indecisione, scelte sbagliate, rottura di partnership, valori disallineati. Progetto: Difficoltà decisionali, tensioni nel team/partnership, comunicazione fallace."
        },
        "en": {
            "dritto": "Important choices, union, partnership, values, communication. Project: Crucial decisions to make, importance of collaboration and alignment, defining project values.",
            "rovescio": "Conflict, indecision, wrong choices, partnership breakdown, misaligned values. Project: Decision-making difficulties, team/partnership tensions, flawed communication."
        }
    },
    "Il Carro": {
        "it": {
            "dritto": "Vittoria, determinazione, autocontrollo, azione decisa, superamento ostacoli. Progetto: Spinta in avanti, controllo degli elementi contrastanti, raggiungimento di un traguardo importante.",
            "rovescio": "Mancanza di direzione, perdita di controllo, aggressività, fallimento, ostacoli insormontabili. Progetto: Progetto fuori controllo, conflitti interni, direzione incerta, sforzi vani."
        },
        "en": {
            "dritto": "Victory, determination, self-control, decisive action, overcoming obstacles. Project: Forward momentum, control of conflicting elements, reaching an important milestone.",
            "rovescio": "Lack of direction, loss of control, aggression, failure, insurmountable obstacles. Project: Project out of control, internal conflicts, uncertain direction, vain efforts."
        }
    },
    "La Giustizia": {
        "it": {
            "dritto": "Equità, verità, legge (causa-effetto), responsabilità, decisioni oggettive. Progetto: Necessità di trasparenza e onestà, decisioni basate sui fatti, conseguenze delle azioni passate, contratti.",
            "rovescio": "Ingiustizia, disonestà, squilibrio, eludere responsabilità, conseguenze legali negative. Progetto: Decisioni parziali, mancanza di trasparenza, dispute contrattuali, problemi legali."
        },
        "en": {
            "dritto": "Fairness, truth, law (cause-effect), responsibility, objective decisions. Project: Need for transparency and honesty, fact-based decisions, consequences of past actions, contracts.",
            "rovescio": "Injustice, dishonesty, imbalance, evading responsibility, negative legal consequences. Project: Biased decisions, lack of transparency, contractual disputes, legal issues."
        }
    },
    "L'Eremita": {
        "it": {
            "dritto": "Introspezione, ricerca interiore, guida, saggezza, ritiro temporaneo. Progetto: Fase di riflessione, analisi approfondita, ricerca di consiglio esperto, necessità di lavorare in solitudine.",
            "rovescio": "Isolamento, solitudine, rifiuto della guida, eccessiva prudenza, ritardi. Progetto: Lavorare troppo isolati, paura di agire, informazioni chiave ignorate, stagnazione."
        },
        "en": {
            "dritto": "Introspection, inner search, guidance, wisdom, temporary withdrawal. Project: Reflection phase, in-depth analysis, seeking expert advice, need to work alone.",
            "rovescio": "Isolation, loneliness, refusal of guidance, excessive caution, delays. Project: Working too isolated, fear of acting, key information ignored, stagnation."
        }
    },
    "La Ruota della Fortuna": {
        "it": {
            "dritto": "Cambiamento, cicli, destino, fortuna, eventi inaspettati (positivi). Progetto: Punto di svolta, cambiamento di direzione, fattori esterni favorevoli, adattabilità richiesta.",
            "rovescio": "Sfortuna, eventi negativi inaspettati, resistenza al cambiamento, cicli negativi. Progetto: Imprevisti problematici, resistenza all'adattamento, periodo difficile, fattori esterni sfavorevoli."
        },
        "en": {
            "dritto": "Change, cycles, destiny, luck, unexpected events (positive). Project: Turning point, change of direction, favorable external factors, adaptability required.",
            "rovescio": "Bad luck, unexpected negative events, resistance to change, negative cycles. Project: Problematic unforeseen events, resistance to adaptation, difficult period, unfavorable external factors."
        }
    },
    "La Forza": {
        "it": {
            "dritto": "Coraggio interiore, pazienza, controllo emotivo, influenza gentile, compassione. Progetto: Affrontare le sfide con calma e resilienza, gestire situazioni difficili con diplomazia, forza morale.",
            "rovescio": "Debolezza,insicurezza, rabbia incontrollata, mancanza di autodisciplina. Progetto: Reazioni emotive sproporzionate, mancanza di fiducia nelle proprie capacità, conflitti interni."
        },
        "en": {
            "dritto": "Inner courage, patience, emotional control, gentle influence, compassion. Project: Facing challenges with calm and resilience, managing difficult situations with diplomacy, moral strength.",
            "rovescio": "Weakness, insecurity, uncontrolled anger, lack of self-discipline. Project: Disproportionate emotional reactions, lack of confidence in one's abilities, internal conflicts."
        }
    },
    "L'Appeso": {
        "it": {
            "dritto": "Sacrificio, attesa, nuova prospettiva, sospensione, lasciar andare. Progetto: Necessità di una pausa per rivalutare, vedere le cose da un'altra angolazione, sacrificio necessario per un bene maggiore.",
            "rovescio": "Stallo inutile, rifiuto di sacrificarsi, martirio, indecisione prolungata. Progetto: Progetto bloccato senza motivo apparente, incapacità di fare le scelte necessarie, sforzi sprecati."
        },
        "en": {
            "dritto": "Sacrifice, waiting, new perspective, suspension, letting go. Project: Need for a pause to reassess, seeing things from another angle, necessary sacrifice for a greater good.",
            "rovescio": "Useless stalemate, refusal to sacrifice, martyrdom, prolonged indecision. Project: Project blocked for no apparent reason, inability to make necessary choices, wasted efforts."
        }
    },
    "La Morte": {
        "it": {
            "dritto": "Fine necessaria, trasformazione, cambiamento radicale, lasciar andare il passato. Progetto: Chiusura di una fase, necessità di abbandonare vecchi metodi, trasformazione significativa.",
            "rovescio": "Resistenza al cambiamento, paura della fine, stagnazione, fine dolorosa ma ritardata. Progetto: Aggrapparsi a ciò che non funziona più, paura di chiudere, processo di cambiamento bloccato."
        },
        "en": {
            "dritto": "Necessary end, transformation, radical change, letting go of the past. Project: Closure of a phase, need to abandon old methods, significant transformation.",
            "rovescio": "Resistance to change, fear of the end, stagnation, painful but delayed end. Project: Clinging to what no longer works, fear of closure, blocked change process."
        }
    },
    "La Temperanza": {
        "it": {
            "dritto": "Equilibrio, moderazione, pazienza, integrazione, armonia. Progetto: Trovare il giusto mezzo, combinare diverse risorse/idee, pazienza nel processo, team ben bilanciato.",
            "rovescio": "Squilibrio, eccesso, impazienza, conflitto, mancanza di visione a lungo termine. Progetto: Estremismi, risorse mal gestite, conflitti tra diverse parti, fretta eccessiva."
        },
        "en": {
            "dritto": "Balance, moderation, patience, integration, harmony. Project: Finding the middle ground, combining different resources/ideas, patience in the process, well-balanced team.",
            "rovescio": "Imbalance, excess, impatience, conflict, lack of long-term vision. Project: Extremes, poorly managed resources, conflicts between different parties, excessive haste."
        }
    },
    "Il Diavolo": {
        "it": {
            "dritto": "Attaccamento materiale, dipendenza, limitazioni autoimposte, tentazione, potere oscuro. Progetto: Attenzione a scorciatoie non etiche, dipendenza da un approccio/risorsa, dinamiche di potere tossiche.",
            "rovescio": "Rompere le catene, libertà, distacco, consapevolezza delle limitazioni. Progetto: Liberarsi da vincoli (contrattuali, mentali), prendere coscienza di dinamiche negative e agire."
        },
        "en": {
            "dritto": "Material attachment, addiction, self-imposed limitations, temptation, dark power. Project: Beware of unethical shortcuts, dependence on an approach/resource, toxic power dynamics.",
            "rovescio": "Breaking chains, freedom, detachment, awareness of limitations. Project: Freeing oneself from constraints (contractual, mental), becoming aware of negative dynamics and acting."
        }
    },
    "La Torre": {
        "it": {
            "dritto": "Distruzione improvvisa, rivelazione scioccante, caos, cambiamento forzato, crollo di strutture. Progetto: Crisi improvvisa, fallimento di piani, necessità di ricostruire dalle fondamenta.",
            "rovescio": "Evitare il disastro, paura del cambiamento, ritardare l'inevitabile, crisi più contenuta. Progetto: Riuscire a evitare il peggio, ma la necessità di cambiamento rimane, disagio latente."
        },
        "en": {
            "dritto": "Sudden destruction, shocking revelation, chaos, forced change, collapse of structures. Project: Sudden crisis, failure of plans, need to rebuild from the foundations.",
            "rovescio": "Avoiding disaster, fear of change, delaying the inevitable, more contained crisis. Project: Managing to avoid the worst, but the need for change remains, latent discomfort."
        }
    },
    "Le Stelle": {
        "it": {
            "dritto": "Speranza, ispirazione, guarigione, serenità, guida spirituale. Progetto: Ottimismo per il futuro, visione chiara, ispirazione rinnovata, periodo di calma dopo la tempesta.",
            "rovescio": "Disperazione, mancanza di fede, scoraggiamento, visione offuscata. Progetto: Perdita di motivazione, pessimismo, sentirsi persi o senza direzione chiara."
        },
        "en": {
            "dritto": "Hope, inspiration, healing, serenity, spiritual guidance. Project: Optimism for the future, clear vision, renewed inspiration, period of calm after the storm.",
            "rovescio": "Despair, lack of faith, discouragement, blurred vision. Project: Loss of motivation, pessimism, feeling lost or without clear direction."
        }
    },
    "La Luna": {
        "it": {
            "dritto": "Illusione, paura, ansia, inconscio, confusione, intuizione profonda. Progetto: Attenzione a ciò che non è chiaro, paura dell'ignoto, informazioni nascoste, fidarsi dell'istinto ma verificare.",
            "rovescio": "Chiarezza emergente, paure superate, confusione che si dissipa, verità rivelata. Progetto: Superamento di un periodo di incertezza, comprensione di dinamiche nascoste."
        },
        "en": {
            "dritto": "Illusion, fear, anxiety, unconscious, confusion, deep intuition. Project: Pay attention to what is unclear, fear of the unknown, hidden information, trust instinct but verify.",
            "rovescio": "Emerging clarity, fears overcome, dissipating confusion, truth revealed. Project: Overcoming a period of uncertainty, understanding hidden dynamics."
        }
    },
    "Il Sole": {
        "it": {
            "dritto": "Successo, vitalità, gioia, chiarezza, ottimismo, realizzazione. Progetto: Successo evidente, energia positiva, team entusiasta, obiettivi raggiunti, chiarezza strategica.",
            "rovescio": "Successo ritardato, ottimismo eccessivo, mancanza di chiarezza, arroganza. Progetto: Risultati meno brillanti del previsto, sottovalutare le sfide, difficoltà a vedere i problemi."
        },
        "en": {
            "dritto": "Success, vitality, joy, clarity, optimism, accomplishment. Project: Evident success, positive energy, enthusiastic team, goals achieved, strategic clarity.",
            "rovescio": "Delayed success, excessive optimism, lack of clarity, arrogance. Project: Results less brilliant than expected, underestimating challenges, difficulty seeing problems."
        }
    },
    "Il Giudizio": {
        "it": {
            "dritto": "Risveglio, resa dei conti, valutazione, rinnovamento, chiamata a uno scopo superiore. Progetto: Valutazione finale, momento di bilancio, decisione importante sul futuro, rinnovamento degli obiettivi.",
            "rovescio": "Autocritica eccessiva, paura del giudizio, ignorare la chiamata, opportunità perse. Progetto: Incapacità di valutare oggettivamente, paura delle conseguenze, rimanere bloccati nel passato."
        },
        "en": {
            "dritto": "Awakening, reckoning, evaluation, renewal, call to a higher purpose. Project: Final evaluation, moment of assessment, important decision about the future, renewal of objectives.",
            "rovescio": "Excessive self-criticism, fear of judgment, ignoring the call, missed opportunities. Project: Inability to evaluate objectively, fear of consequences, remaining stuck in the past."
        }
    },
    "Il Mondo": {
        "it": {
            "dritto": "Completamento, integrazione, successo, realizzazione, fine di un ciclo. Progetto: Conclusione positiva del progetto, raggiungimento di tutti gli obiettivi, integrazione riuscita, soddisfazione.",
            "rovescio": "Incompletezza, mancanza di chiusura, successo parziale, ritardi finali. Progetto: Progetto non concluso del tutto, obiettivi mancati, difficoltà nell'integrazione finale, sensazione di incompiuto."
        },
        "en": {
            "dritto": "Completion, integration, success, achievement, end of a cycle. Project: Positive conclusion of the project, achievement of all goals, successful integration, satisfaction.",
            "rovescio": "Incompleteness, lack of closure, partial success, final delays. Project: Project not fully concluded, missed goals, difficulty in final integration, feeling of unfinished business."
        }
    },

    # --- ARCANI MINORI: BASTONI (Elemento Fuoco: Energia, Azione, Creatività, Impresa) ---
    # --- MINOR ARCANA: WANDS (Element Fire: Energy, Action, Creativity, Enterprise) ---
    "Asso di Bastoni": {
        "it": {
             "dritto": "Nuova scintilla creativa, ispirazione, potenziale, inizio energico, intraprendenza. Progetto: Kick-off entusiasta, nuova idea promettente, fase di avvio dinamica.",
             "rovescio": "Mancanza di energia, ritardi, falsa partenza, blocco creativo, idee non realizzate. Progetto: Difficoltà a iniziare, mancanza di motivazione, ostacoli iniziali."
        },
        "en": {
             "dritto": "New creative spark, inspiration, potential, energetic start, initiative. Project: Enthusiastic kick-off, promising new idea, dynamic start-up phase.",
             "rovescio": "Lack of energy, delays, false start, creative block, unrealized ideas. Project: Difficulty starting, lack of motivation, initial obstacles."
        }
    },
    "Due di Bastoni": {
        "it": {
            "dritto": "Pianificazione futura, progresso iniziale, decisioni, scoperta, valutazione opzioni. Progetto: Fase di pianificazione strategica, scelta della direzione, valutazione di partnership.",
            "rovescio": "Paura dell'ignoto, mancanza di pianificazione, indecisione, piani bloccati. Progetto: Incapacità di decidere la strategia, paura di espandersi, limitazioni autoimposte."
        },
        "en": {
            "dritto": "Future planning, initial progress, decisions, discovery, evaluating options. Project: Strategic planning phase, choosing direction, evaluating partnerships.",
            "rovescio": "Fear of the unknown, lack of planning, indecision, blocked plans. Project: Inability to decide strategy, fear of expansion, self-imposed limitations."
        }
    },
    "Tre di Bastoni": {
        "it": {
            "dritto": "Espansione, lungimiranza, attesa dei risultati, preparazione, collaborazione iniziale. Progetto: Primi risultati positivi, espansione delle attività, visione a lungo termine.",
            "rovescio": "Ritardi nei risultati, ostacoli all'espansione, mancanza di visione, piani irrealistici. Progetto: Le aspettative non si concretizzano, difficoltà di crescita, poca lungimiranza."
        },
        "en": {
            "dritto": "Expansion, foresight, waiting for results, preparation, initial collaboration. Project: First positive results, expansion of activities, long-term vision.",
            "rovescio": "Delays in results, obstacles to expansion, lack of vision, unrealistic plans. Project: Expectations not materializing, growth difficulties, lack of foresight."
        }
    },
    "Quattro di Bastoni": {
        "it": {
            "dritto": "Celebrazione, armonia, stabilità raggiunta, traguardo intermedio, lavoro di squadra positivo. Progetto: Raggiungimento di una milestone importante, team coeso, ambiente positivo.",
            "rovescio": "Mancanza di armonia, instabilità, celebrazione prematura, tensioni nascoste. Progetto: Conflitti nel team, risultati instabili, festeggiamenti fuori luogo."
        },
        "en": {
            "dritto": "Celebration, harmony, achieved stability, intermediate goal, positive teamwork. Project: Reaching an important milestone, cohesive team, positive environment.",
            "rovescio": "Lack of harmony, instability, premature celebration, hidden tensions. Project: Conflicts in the team, unstable results, inappropriate celebrations."
        }
    },
    "Cinque di Bastoni": {
        "it": {
            "dritto": "Conflitto, competizione, disaccordo, sfide, diverse opinioni. Progetto: Discussioni accese, competizione interna/esterna, necessità di gestire opinioni divergenti.",
            "rovescio": "Evitare il conflitto, accordo forzato, tensione repressa, fine della competizione. Progetto: Paura di affrontare i problemi, accordi superficiali, possibile risoluzione dei conflitti."
        },
        "en": {
            "dritto": "Conflict, competition, disagreement, challenges, different opinions. Project: Heated discussions, internal/external competition, need to manage divergent opinions.",
            "rovescio": "Avoiding conflict, forced agreement, repressed tension, end of competition. Project: Fear of facing problems, superficial agreements, possible resolution of conflicts."
        }
    },
    "Sei di Bastoni": {
        "it": {
            "dritto": "Successo pubblico, riconoscimento, vittoria, leadership acclamata, progresso. Progetto: Raggiungimento di un obiettivo chiave con successo, riconoscimento del lavoro svolto, morale alto.",
            "rovescio": "Fallimento, mancanza di riconoscimento, tradimento, arroganza dopo il successo. Progetto: Obiettivo mancato, lavoro non apprezzato, possibile sabotaggio, eccessiva sicurezza."
        },
        "en": {
            "dritto": "Public success, recognition, victory, acclaimed leadership, progress. Project: Achieving a key objective successfully, recognition for work done, high morale.",
            "rovescio": "Failure, lack of recognition, betrayal, arrogance after success. Project: Missed objective, unappreciated work, possible sabotage, overconfidence."
        }
    },
    "Sette di Bastoni": {
        "it": {
            "dritto": "Difesa, perseveranza, sfida, mantenere la propria posizione, coraggio. Progetto: Difendere il progetto da critiche o ostacoli, perseverare nonostante le difficoltà.",
            "rovescio": "Sopraffazione, arrendersi, stanchezza, perdere terreno, mancanza di fiducia. Progetto: Sentirsi sopraffatti dalle sfide, dubitare della validità del progetto, cedere alle pressioni."
        },
        "en": {
            "dritto": "Defense, perseverance, challenge, holding one's position, courage. Project: Defending the project from criticism or obstacles, persevering despite difficulties.",
            "rovescio": "Overwhelmed, giving up, fatigue, losing ground, lack of confidence. Project: Feeling overwhelmed by challenges, doubting the project's validity, yielding to pressure."
        }
    },
    "Otto di Bastoni": {
        "it": {
            "dritto": "Movimento rapido, azione veloce, comunicazione rapida, notizie in arrivo, progresso accelerato. Progetto: Sviluppi rapidi, decisioni veloci necessarie, comunicazioni importanti.",
            "rovescio": "Ritardi, frustrazione, rallentamenti, comunicazioni bloccate, resistenza al progresso. Progetto: Ostacoli che rallentano tutto, difficoltà di comunicazione, inerzia."
        },
        "en": {
            "dritto": "Rapid movement, swift action, quick communication, news arriving, accelerated progress. Project: Rapid developments, quick decisions needed, important communications.",
            "rovescio": "Delays, frustration, slowdowns, blocked communications, resistance to progress. Project: Obstacles slowing everything down, communication difficulties, inertia."
        }
    },
    "Nove di Bastoni": {
        "it": {
            "dritto": "Resilienza, ultima resistenza, stanchezza ma non sconfitta, preparazione alla battaglia finale. Progetto: Quasi alla fine ma esausti, necessità di un ultimo sforzo, difendere i risultati raggiunti.",
            "rovescio": "Esaurimento, sconfitta imminente, mancanza di difese, paranoia, rigidità. Progetto: Burnout, incapacità di sostenere lo sforzo finale, sentirsi attaccati da tutte le parti."
        },
        "en": {
            "dritto": "Resilience, last stand, tired but not defeated, preparation for the final battle. Project: Almost at the end but exhausted, need for one last push, defending achieved results.",
            "rovescio": "Exhaustion, impending defeat, lack of defenses, paranoia, rigidity. Project: Burnout, inability to sustain the final effort, feeling attacked from all sides."
        }
    },
    "Dieci di Bastoni": {
        "it": {
            "dritto": "Fardello pesante, responsabilità eccessiva, stress, duro lavoro che porta a termine. Progetto: Carico di lavoro insostenibile, troppe responsabilità su pochi, fase finale molto faticosa.",
            "rovescio": "Rilasciare il fardello, delegare, sovraccarico che porta al collasso, incapacità di gestire. Progetto: Necessità di delegare o semplificare, rischio di fallimento per troppo carico."
        },
        "en": {
            "dritto": "Heavy burden, excessive responsibility, stress, hard work reaching completion. Project: Unsustainable workload, too many responsibilities on too few, very tiring final phase.",
            "rovescio": "Releasing the burden, delegating, overload leading to collapse, inability to manage. Project: Need to delegate or simplify, risk of failure due to overload."
        }
    },
    "Fante di Bastoni": {
        "it": {
            "dritto": "Esplorazione, entusiasmo, nuove idee, messaggero di buone notizie, spirito libero. Progetto: Nuove proposte creative, membro del team entusiasta, fase di esplorazione.",
            "rovescio": "Idee immature, mancanza di direzione, notizie deludenti, impulsività, procrastinazione. Progetto: Proposte poco pratiche, entusiasmo superficiale, ritardi nelle comunicazioni."
        },
        "en": {
            "dritto": "Exploration, enthusiasm, new ideas, messenger of good news, free spirit. Project: New creative proposals, enthusiastic team member, exploration phase.",
            "rovescio": "Immature ideas, lack of direction, disappointing news, impulsiveness, procrastination. Project: Impractical proposals, superficial enthusiasm, communication delays."
        }
    },
    "Cavaliere di Bastoni": {
        "it": {
            "dritto": "Azione rapida, avventura, impulsività, passione, carisma energetico. Progetto: Agire rapidamente, prendere l'iniziativa, energia contagiosa, ma rischio di avventatezza.",
            "rovescio": "Azione spericolata, ritardi frustranti, mancanza di energia, aggressività. Progetto: Decisioni affrettate e sbagliate, progetto bloccato, conflitti dovuti all'impulsività."
        },
        "en": {
            "dritto": "Rapid action, adventure, impulsiveness, passion, energetic charisma. Project: Acting quickly, taking initiative, contagious energy, but risk of recklessness.",
            "rovescio": "Reckless action, frustrating delays, lack of energy, aggression. Project: Hasty and wrong decisions, blocked project, conflicts due to impulsiveness."
        }
    },
    "Regina di Bastoni": {
        "it": {
            "dritto": "Confidenza, indipendenza, leadership carismatica, determinazione, calore. Progetto: Leader/membro del team capace e ispiratore, ambiente di lavoro vivace, determinazione.",
            "rovescio": "Intolleranza, gelosia, prepotenza, esaurimento energetico. Progetto: Leadership autoritaria, conflitti di potere, ambiente stressante, burnout."
        },
        "en": {
            "dritto": "Confidence, independence, charismatic leadership, determination, warmth. Project: Capable and inspiring leader/team member, lively work environment, determination.",
            "rovescio": "Intolerance, jealousy, bossiness, energy depletion. Project: Authoritarian leadership, power struggles, stressful environment, burnout."
        }
    },
    "Re di Bastoni": {
        "it": {
            "dritto": "Visione, leadership naturale, imprenditorialità, onore, ispirazione. Progetto: Leader visionario, strategia chiara, capacità di ispirare il team, prendere rischi calcolati.",
            "rovescio": "Autoritarismo, intolleranza, impulsività, aspettative irrealistiche, leadership debole. Progetto: Capo dispotico, piani irrealistici, mancanza di direzione strategica."
        },
        "en": {
            "dritto": "Vision, natural leadership, entrepreneurship, honor, inspiration. Project: Visionary leader, clear strategy, ability to inspire the team, taking calculated risks.",
            "rovescio": "Authoritarianism, intolerance, impulsiveness, unrealistic expectations, weak leadership. Project: Despotic boss, unrealistic plans, lack of strategic direction."
        }
    },

    # --- ARCANI MINORI: COPPE (Elemento Acqua: Emozioni, Relazioni, Intuizione, Creatività Artistica) ---
    # --- MINOR ARCANA: CUPS (Element Water: Emotions, Relationships, Intuition, Artistic Creativity) ---
    "Asso di Coppe": {
        "it": {
            "dritto": "Nuovo amore/emozione, creatività, intuizione, compassione, inizio di relazione (anche lavorativa). Progetto: Buon clima emotivo nel team, inizio di collaborazioni positive, flusso creativo.",
            "rovescio": "Emozioni bloccate, creatività repressa, rifiuto, tristezza, opportunità emotive mancate. Progetto: Mancanza di coesione nel team, blocchi creativi, difficoltà relazionali."
        },
        "en": {
            "dritto": "New love/emotion, creativity, intuition, compassion, beginning of a relationship (also work-related). Project: Good emotional climate in the team, start of positive collaborations, creative flow.",
            "rovescio": "Blocked emotions, repressed creativity, rejection, sadness, missed emotional opportunities. Project: Lack of team cohesion, creative blocks, relationship difficulties."
        }
    },
    "Due di Coppe": {
        "it": {
            "dritto": "Unione, partnership, attrazione reciproca, armonia, collaborazione efficace. Progetto: Partnership solida, buona intesa nel team, accordo raggiunto, collaborazione fruttuosa.",
            "rovescio": "Disarmonia, rottura di partnership, sfiducia, squilibrio, comunicazione difficile. Progetto: Conflitti tra partner o nel team, mancanza di fiducia, accordi falliti."
        },
        "en": {
            "dritto": "Union, partnership, mutual attraction, harmony, effective collaboration. Project: Solid partnership, good understanding in the team, agreement reached, fruitful collaboration.",
            "rovescio": "Disharmony, partnership breakdown, mistrust, imbalance, difficult communication. Project: Conflicts between partners or in the team, lack of trust, failed agreements."
        }
    },
    "Tre di Coppe": {
        "it": {
            "dritto": "Celebrazione, amicizia, comunità, collaborazione gioiosa, successo condiviso. Progetto: Team affiatato, celebrazione di un successo, buon ambiente di lavoro, eventi sociali positivi.",
            "rovescio": "Gossip, eccessi, isolamento, fine dell'armonia, celebrazione fuori luogo. Progetto: Pettegolezzi che minano il team, collaborazione superficiale, sentirsi esclusi."
        },
        "en": {
            "dritto": "Celebration, friendship, community, joyful collaboration, shared success. Project: Close-knit team, celebration of success, good work environment, positive social events.",
            "rovescio": "Gossip, excess, isolation, end of harmony, inappropriate celebration. Project: Gossip undermining the team, superficial collaboration, feeling excluded."
        }
    },
    "Quattro di Coppe": {
        "it": {
            "dritto": "Apatia, contemplazione, disinteresse, opportunità mancate, introspezione. Progetto: Mancanza di motivazione, rifiuto di nuove proposte, periodo di stasi riflessiva.",
            "rovescio": "Interesse rinnovato, accettazione di offerte, fine dell'apatia, nuove possibilità. Progetto: Ritrovare la motivazione, cogliere nuove opportunità, uscire da una fase di stallo."
        },
        "en": {
            "dritto": "Apathy, contemplation, disinterest, missed opportunities, introspection. Project: Lack of motivation, rejection of new proposals, period of reflective stagnation.",
            "rovescio": "Renewed interest, accepting offers, end of apathy, new possibilities. Project: Regaining motivation, seizing new opportunities, emerging from a stalemate."
        }
    },
    "Cinque di Coppe": {
        "it": {
            "dritto": "Perdita, rimpianto, delusione, concentrarsi sul negativo, tristezza. Progetto: Fallimento parziale, delusione per i risultati, focalizzarsi sugli errori, morale basso.",
            "rovescio": "Accettazione, perdono, vedere il positivo, superare il rimpianto, andare avanti. Progetto: Imparare dagli errori, superare una battuta d'arresto, vedere nuove prospettive."
        },
        "en": {
            "dritto": "Loss, regret, disappointment, focusing on the negative, sadness. Project: Partial failure, disappointment with results, focusing on mistakes, low morale.",
            "rovescio": "Acceptance, forgiveness, seeing the positive, overcoming regret, moving on. Project: Learning from mistakes, overcoming a setback, seeing new perspectives."
        }
    },
    "Sei di Coppe": {
        "it": {
            "dritto": "Nostalgia, ricordi felici, generosità, armonia passata, doni. Progetto: Basarsi su successi passati, collaborazione basata su vecchie relazioni, ritorno a metodi collaudati.",
            "rovescio": "Aggrapparsi al passato, mancanza di prospettiva futura, ricordi dolorosi, ingenuità. Progetto: Incapacità di innovare, vivere di rendita, idealizzare il passato."
        },
        "en": {
            "dritto": "Nostalgia, happy memories, generosity, past harmony, gifts. Project: Building on past successes, collaboration based on old relationships, return to proven methods.",
            "rovescio": "Clinging to the past, lack of future perspective, painful memories, naivety. Project: Inability to innovate, resting on laurels, idealizing the past."
        }
    },
    "Sette di Coppe": {
        "it": {
            "dritto": "Scelte multiple, illusioni, sogni ad occhi aperti, tentazioni, immaginazione. Progetto: Troppe opzioni tra cui scegliere, rischio di illusioni, necessità di concretezza.",
            "rovescio": "Chiarezza, decisione presa, realtà che si impone, evitare le tentazioni. Progetto: Scelta finalmente fatta, focus su opzioni realistiche, superamento della confusione."
        },
        "en": {
            "dritto": "Multiple choices, illusions, daydreams, temptations, imagination. Project: Too many options to choose from, risk of illusions, need for concreteness.",
            "rovescio": "Clarity, decision made, reality setting in, avoiding temptations. Project: Choice finally made, focus on realistic options, overcoming confusion."
        }
    },
    "Otto di Coppe": {
        "it": {
            "dritto": "Abbandono, ricerca di qualcosa di più, allontanarsi, delusione che porta al cambiamento. Progetto: Abbandonare un approccio/progetto insoddisfacente, cercare nuove strade.",
            "rovescio": "Paura di andarsene, rimanere in una situazione insoddisfacente, ritorno sui propri passi. Progetto: Incapacità di lasciare ciò che non funziona, paura del cambiamento, stagnazione."
        },
        "en": {
            "dritto": "Abandonment, searching for something more, moving away, disappointment leading to change. Project: Abandoning an unsatisfactory approach/project, seeking new paths.",
            "rovescio": "Fear of leaving, staying in an unsatisfactory situation, retracing steps. Project: Inability to leave what doesn't work, fear of change, stagnation."
        }
    },
    "Nove di Coppe": {
        "it": {
            "dritto": "Soddisfazione, desiderio esaudito, piacere, contentezza, successo emotivo. Progetto: Raggiungimento di un obiettivo desiderato, soddisfazione personale e del team, successo.",
            "rovescio": "Insoddisfazione, desideri non realizzati, avidità, compiacenza eccessiva. Progetto: Obiettivi non raggiunti, aspettative deluse, rischio di adagiarsi sugli allori."
        },
        "en": {
            "dritto": "Satisfaction, wish granted, pleasure, contentment, emotional success. Project: Achievement of a desired goal, personal and team satisfaction, success.",
            "rovescio": "Dissatisfaction, unfulfilled wishes, greed, excessive complacency. Project: Goals not met, disappointed expectations, risk of resting on laurels."
        }
    },
    "Dieci di Coppe": {
        "it": {
            "dritto": "Felicità familiare/comunitaria, armonia duratura, realizzazione emotiva, pace. Progetto: Team perfettamente allineato e felice, successo completo e condiviso, ambiente ideale.",
            "rovescio": "Famiglia/comunità disfunzionale, conflitto, felicità superficiale, rottura dell'armonia. Progetto: Gravi conflitti nel team, mancanza di coesione, successo apparente ma problemi di fondo."
        },
        "en": {
            "dritto": "Family/community happiness, lasting harmony, emotional fulfillment, peace. Project: Perfectly aligned and happy team, complete and shared success, ideal environment.",
            "rovescio": "Dysfunctional family/community, conflict, superficial happiness, breakdown of harmony. Project: Serious team conflicts, lack of cohesion, apparent success but underlying problems."
        }
    },
    "Fante di Coppe": {
        "it": {
            "dritto": "Messaggero emotivo, intuizione, creatività nascente, sensibilità, nuove idee emotive. Progetto: Notizie positive sul fronte relazionale/creativo, membro del team intuitivo e sensibile.",
            "rovescio": "Immaturità emotiva, blocchi creativi, cattive notizie emotive, ipersensibilità. Progetto: Reazioni emotive infantili, mancanza di ispirazione, notizie deludenti."
        },
        "en": {
            "dritto": "Emotional messenger, intuition, nascent creativity, sensitivity, new emotional ideas. Project: Positive news on the relational/creative front, intuitive and sensitive team member.",
            "rovescio": "Emotional immaturity, creative blocks, bad emotional news, hypersensitivity. Project: Childish emotional reactions, lack of inspiration, disappointing news."
        }
    },
    "Cavaliere di Coppe": {
        "it": {
            "dritto": "Romanticismo, fascino, offerta emotiva, seguire il cuore, diplomazia. Progetto: Approccio diplomatico, proposta collaborativa, agire guidati da valori positivi.",
            "rovescio": "Irrealismo, umoralità, manipolazione emotiva, offerte insincere. Progetto: Proposte irrealistiche, eccessiva emotività nelle decisioni, possibile inganno."
        },
        "en": {
            "dritto": "Romanticism, charm, emotional offer, following the heart, diplomacy. Project: Diplomatic approach, collaborative proposal, acting guided by positive values.",
            "rovescio": "Unrealism, moodiness, emotional manipulation, insincere offers. Project: Unrealistic proposals, excessive emotionality in decisions, possible deception."
        }
    },
    "Regina di Coppe": {
        "it": {
            "dritto": "Compassione, intuizione, empatia, nutrimento emotivo, saggezza interiore. Progetto: Leader/membro del team empatico e di supporto, attenzione al benessere del team, guida intuitiva.",
            "rovescio": "Ipersensibilità, dipendenza emotiva, manipolazione, instabilità emotiva. Progetto: Eccessiva emotività che crea problemi, bisogno di approvazione costante, possibile vittimismo."
        },
        "en": {
            "dritto": "Compassion, intuition, empathy, emotional nurturing, inner wisdom. Project: Empathetic and supportive leader/team member, attention to team well-being, intuitive guidance.",
            "rovescio": "Hypersensitivity, emotional dependence, manipulation, emotional instability. Project: Excessive emotionality causing problems, constant need for approval, possible victimhood."
        }
    },
    "Re di Coppe": {
        "it": {
            "dritto": "Controllo emotivo, compassione matura, equilibrio tra cuore e mente, diplomazia, tolleranza. Progetto: Leader equilibrato e saggio, gestione calma delle crisi, diplomazia efficace.",
            "rovescio": "Manipolazione emotiva, umoralità, freddezza emotiva, abuso di potere emotivo. Progetto: Leader che usa le emozioni per manipolare, instabilità, mancanza di empatia reale."
        },
        "en": {
            "dritto": "Emotional control, mature compassion, balance between heart and mind, diplomacy, tolerance. Project: Balanced and wise leader, calm crisis management, effective diplomacy.",
            "rovescio": "Emotional manipulation, moodiness, emotional coldness, abuse of emotional power. Project: Leader using emotions to manipulate, instability, lack of real empathy."
        }
    },

    # --- ARCANI MINORI: SPADE (Elemento Aria: Intelletto, Comunicazione, Conflitto, Verità, Sfide) ---
    # --- MINOR ARCANA: SWORDS (Element Air: Intellect, Communication, Conflict, Truth, Challenges) ---
    "Asso di Spade": {
        "it": {
            "dritto": "Chiarezza mentale, nuova idea brillante, verità, taglio netto, decisione. Progetto: Momento di grande chiarezza strategica, idea innovativa, decisione importante presa.",
            "rovescio": "Confusione, mancanza di idee, decisione sbagliata, comunicazione fallace, potenziale conflitto. Progetto: Piani confusi, idee non valide, cattiva comunicazione, inizio di dispute."
        },
        "en": {
            "dritto": "Mental clarity, brilliant new idea, truth, clean cut, decision. Project: Moment of great strategic clarity, innovative idea, important decision made.",
            "rovescio": "Confusion, lack of ideas, wrong decision, flawed communication, potential conflict. Project: Confused plans, invalid ideas, poor communication, beginning of disputes."
        }
    },
    "Due di Spade": {
        "it": {
            "dritto": "Indecisione, stallo, scelta difficile, tregua temporanea, necessità di equilibrio. Progetto: Blocco decisionale, necessità di valutare attentamente due opzioni, tregua in un conflitto.",
            "rovescio": "Decisione forzata o sbagliata, confusione, tradimento, ripresa del conflitto. Progetto: Scelta difficile fatta male, informazioni fuorvianti, fine della tregua."
        },
        "en": {
            "dritto": "Indecision, stalemate, difficult choice, temporary truce, need for balance. Project: Decision block, need to carefully evaluate two options, truce in a conflict.",
            "rovescio": "Forced or wrong decision, confusion, betrayal, resumption of conflict. Project: Difficult choice made poorly, misleading information, end of the truce."
        }
    },
    "Tre di Spade": {
        "it": {
            "dritto": "Dolore, perdita, tradimento, verità dolorosa, conflitto aperto. Progetto: Notizie negative, fallimento che causa dolore, conflitto che emerge chiaramente, rottura di fiducia.",
            "rovescio": "Guarigione dal dolore, perdono, superamento del conflitto, verità accettata. Progetto: Superamento di una crisi, risoluzione (anche se dolorosa) di un conflitto, accettazione della realtà."
        },
        "en": {
            "dritto": "Pain, loss, betrayal, painful truth, open conflict. Project: Negative news, failure causing pain, conflict emerging clearly, breach of trust.",
            "rovescio": "Healing from pain, forgiveness, overcoming conflict, accepted truth. Project: Overcoming a crisis, resolution (even if painful) of a conflict, acceptance of reality."
        }
    },
    "Quattro di Spade": {
        "it": {
            "dritto": "Riposo, recupero, contemplazione, pausa necessaria, tregua. Progetto: Necessità di una pausa per ricaricarsi, fase di riflessione dopo un periodo intenso, recupero.",
            "rovescio": "Stagnazione, esaurimento, rifiuto di riposare, ripresa forzata. Progetto: Pausa che si trasforma in blocco, burnout per mancanza di riposo, ripartenza prematura."
        },
        "en": {
            "dritto": "Rest, recovery, contemplation, necessary pause, truce. Project: Need for a break to recharge, reflection phase after an intense period, recovery.",
            "rovescio": "Stagnation, exhaustion, refusal to rest, forced resumption. Project: Pause turning into blockage, burnout from lack of rest, premature restart."
        }
    },
    "Cinque di Spade": {
        "it": {
            "dritto": "Conflitto umiliante, vittoria a caro prezzo, perdita, ostilità, prepotenza. Progetto: Conflitto distruttivo, vincere ma perdere relazioni, ambiente di lavoro tossico.",
            "rovescio": "Fine del conflitto, possibilità di riconciliazione, consapevolezza delle perdite, rilascio della tensione. Progetto: Possibile risoluzione di un conflitto aspro, presa di coscienza dei danni fatti."
        },
        "en": {
            "dritto": "Humiliating conflict, victory at a high cost, loss, hostility, arrogance. Project: Destructive conflict, winning but losing relationships, toxic work environment.",
            "rovescio": "End of conflict, possibility of reconciliation, awareness of losses, release of tension. Project: Possible resolution of a harsh conflict, awareness of the damage done."
        }
    },
    "Sei di Spade": {
        "it": {
            "dritto": "Transizione, superamento difficoltà, viaggio (anche metaforico), andare verso acque più calme. Progetto: Superamento di una fase difficile, transizione verso una situazione migliore, aiuto ricevuto.",
            "rovescio": "Transizione bloccata, resistenza al cambiamento, ritorno ai problemi, viaggio difficile. Progetto: Difficoltà a superare i problemi, rimanere bloccati nel passato, ostacoli imprevisti."
        },
        "en": {
            "dritto": "Transition, overcoming difficulties, journey (also metaphorical), moving towards calmer waters. Project: Overcoming a difficult phase, transition to a better situation, help received.",
            "rovescio": "Blocked transition, resistance to change, return to problems, difficult journey. Project: Difficulty overcoming problems, remaining stuck in the past, unforeseen obstacles."
        }
    },
    "Sette di Spade": {
        "it": {
            "dritto": "Inganno, furto, strategia nascosta, agire da soli, eludere. Progetto: Attenzione a comportamenti scorretti, strategie non trasparenti, possibile furto di idee/risorse.",
            "rovescio": "Confessione, ritorno all'onestà, smascheramento, consiglio prezioso ignorato. Progetto: Inganni scoperti, ritorno alla trasparenza, affrontare le conseguenze di azioni nascoste."
        },
        "en": {
            "dritto": "Deception, theft, hidden strategy, acting alone, evasion. Project: Beware of unethical behavior, non-transparent strategies, possible theft of ideas/resources.",
            "rovescio": "Confession, return to honesty, unmasking, valuable advice ignored. Project: Deceptions discovered, return to transparency, facing the consequences of hidden actions."
        }
    },
    "Otto di Spade": {
        "it": {
            "dritto": "Restrizione autoimposta, sentirsi intrappolati, impotenza, paura di agire. Progetto: Sentirsi bloccati da limiti mentali più che reali, paura di prendere decisioni, mancanza di prospettive.",
            "rovescio": "Liberazione, trovare soluzioni, superare le paure, vedere nuove possibilità. Progetto: Riconoscere i propri limiti autoimposti e superarli, trovare vie d'uscita, agire."
        },
        "en": {
            "dritto": "Self-imposed restriction, feeling trapped, powerlessness, fear of acting. Project: Feeling blocked by mental rather than real limits, fear of making decisions, lack of perspective.",
            "rovescio": "Liberation, finding solutions, overcoming fears, seeing new possibilities. Project: Recognizing one's self-imposed limits and overcoming them, finding ways out, taking action."
        }
    },
    "Nove di Spade": {
        "it": {
            "dritto": "Ansia, preoccupazione, incubi, stress mentale, paura profonda. Progetto: Forte stress legato al progetto, ansia per il futuro, preoccupazioni che tengono svegli la notte.",
            "rovescio": "Rilascio dell'ansia, superamento delle paure, ricerca di aiuto, vedere la luce. Progetto: Affrontare le cause dello stress, trovare supporto, le preoccupazioni si ridimensionano."
        },
        "en": {
            "dritto": "Anxiety, worry, nightmares, mental stress, deep fear. Project: High stress related to the project, anxiety about the future, worries keeping you up at night.",
            "rovescio": "Release of anxiety, overcoming fears, seeking help, seeing the light. Project: Addressing the causes of stress, finding support, worries diminish."
        }
    },
    "Dieci di Spade": {
        "it": {
            "dritto": "Fine dolorosa, fallimento completo, fondo toccato, tradimento finale, esaurimento. Progetto: Fallimento definitivo, fine di un progetto/fase in modo traumatico, necessità di accettare la fine.",
            "rovescio": "Sopravvivenza, ripresa dopo il disastro, fine del ciclo negativo, lezione imparata. Progetto: Anche se fallito, si impara qualcosa; possibilità di ripartire dopo aver toccato il fondo."
        },
        "en": {
            "dritto": "Painful ending, complete failure, rock bottom, final betrayal, exhaustion. Project: Definitive failure, traumatic end of a project/phase, need to accept the end.",
            "rovescio": "Survival, recovery after disaster, end of the negative cycle, lesson learned. Project: Even if failed, something is learned; possibility of starting over after hitting rock bottom."
        }
    },
    "Fante di Spade": {
        "it": {
            "dritto": "Curiosità, ricerca della verità, vigilanza, comunicazione diretta, nuove idee analitiche. Progetto: Membro del team analitico e curioso, comunicazione schietta, raccolta di informazioni.",
            "rovescio": "Gossip, comunicazione offensiva, indiscrezione, mancanza di tatto, paranoia. Progetto: Comunicazione che crea problemi, diffusione di notizie false o dannose, sospettosità eccessiva."
        },
        "en": {
            "dritto": "Curiosity, truth-seeking, vigilance, direct communication, new analytical ideas. Project: Analytical and curious team member, frank communication, information gathering.",
            "rovescio": "Gossip, offensive communication, indiscretion, lack of tact, paranoia. Project: Communication causing problems, spreading false or harmful news, excessive suspiciousness."
        }
    },
    "Cavaliere di Spade": {
        "it": {
            "dritto": "Azione rapida e decisa, ambizione, focalizzazione, andare dritti al punto. Progetto: Agire con determinazione e velocità, approccio diretto ai problemi, focus sull'obiettivo.",
            "rovescio": "Azione spericolata, aggressività, mancanza di pianificazione, fanatismo. Progetto: Decisioni affrettate e aggressive, non considerare le conseguenze, conflitti inutili."
        },
        "en": {
            "dritto": "Rapid and decisive action, ambition, focus, getting straight to the point. Project: Acting with determination and speed, direct approach to problems, focus on the objective.",
            "rovescio": "Reckless action, aggression, lack of planning, fanaticism. Project: Hasty and aggressive decisions, not considering consequences, unnecessary conflicts."
        }
    },
    "Regina di Spade": {
        "it": {
            "dritto": "Intelligenza acuta, indipendenza, onestà brutale, chiarezza di pensiero, esperienza. Progetto: Leader/membro del team molto intelligente e diretto, capace di analisi critica, non teme la verità.",
            "rovescio": "Critica eccessiva, amarezza, isolamento, freddezza, malizia. Progetto: Critica distruttiva, ambiente freddo e ostile, possibile sabotaggio intellettuale."
        },
        "en": {
            "dritto": "Sharp intelligence, independence, brutal honesty, clarity of thought, experience. Project: Very intelligent and direct leader/team member, capable of critical analysis, not afraid of the truth.",
            "rovescio": "Excessive criticism, bitterness, isolation, coldness, malice. Project: Destructive criticism, cold and hostile environment, possible intellectual sabotage."
        }
    },
    "Re di Spade": {
        "it": {
            "dritto": "Autorità intellettuale, verità, giustizia, etica, leadership basata sulla logica. Progetto: Leader giusto ed etico, decisioni basate su fatti e logica, chiarezza mentale e strategica.",
            "rovescio": "Autoritarismo intellettuale, cinismo, crudeltà, giudizio severo, abuso di potere mentale. Progetto: Leader che usa l'intelletto per dominare, mancanza di empatia, decisioni spietate."
        },
        "en": {
            "dritto": "Intellectual authority, truth, justice, ethics, logic-based leadership. Project: Fair and ethical leader, decisions based on facts and logic, mental and strategic clarity.",
            "rovescio": "Intellectual authoritarianism, cynicism, cruelty, severe judgment, abuse of mental power. Project: Leader using intellect to dominate, lack of empathy, ruthless decisions."
        }
    },

    # --- ARCANI MINORI: DENARI (Elemento Terra: Mondo Materiale, Lavoro, Finanze, Praticità, Risorse) ---
    # --- MINOR ARCANA: PENTACLES (Element Earth: Material World, Work, Finances, Practicality, Resources) ---
    "Asso di Denari": {
        "it": {
            "dritto": "Nuova opportunità (lavoro/finanza), manifestazione concreta, risorse, inizio solido. Progetto: Nuova offerta, finanziamento approvato, inizio pratico del lavoro, basi solide.",
            "rovescio": "Opportunità persa, cattiva gestione finanziaria, mancanza di pianificazione pratica, ritardi. Progetto: Finanziamento rifiutato, piani poco pratici, ritardi nell'avvio concreto."
        },
        "en": {
            "dritto": "New opportunity (work/finance), concrete manifestation, resources, solid start. Project: New offer, funding approved, practical start of work, solid foundations.",
            "rovescio": "Missed opportunity, poor financial management, lack of practical planning, delays. Project: Funding rejected, impractical plans, delays in concrete start."
        }
    },
    "Due di Denari": {
        "it": {
            "dritto": "Equilibrio, gestione di più priorità, adattabilità, flessibilità, multitasking. Progetto: Gestire diverse attività contemporaneamente, bilanciare budget/tempo, adattarsi ai cambiamenti.",
            "rovescio": "Squilibrio, cattiva gestione, sovraccarico, stress finanziario, inflessibilità. Progetto: Difficoltà a gestire tutto, budget fuori controllo, incapacità di adattarsi.",
        },
        "en": {
            "dritto": "Balance, managing multiple priorities, adaptability, flexibility, multitasking. Project: Managing different tasks simultaneously, balancing budget/time, adapting to changes.",
            "rovescio": "Imbalance, poor management, overload, financial stress, inflexibility. Project: Difficulty managing everything, budget out of control, inability to adapt."
        }
    },
    "Tre di Denari": {
        "it": {
            "dritto": "Lavoro di squadra, collaborazione, abilità riconosciuta, qualità, apprendimento. Progetto: Teamwork efficace, riconoscimento delle competenze, focus sulla qualità del lavoro.",
            "rovescio": "Lavoro di squadra scadente, mancanza di collaborazione, mediocrità, competenze non valorizzate. Progetto: Difficoltà a lavorare insieme, risultati di bassa qualità, conflitti sulle competenze."
        },
        "en": {
            "dritto": "Teamwork, collaboration, recognized skill, quality, learning. Project: Effective teamwork, recognition of skills, focus on work quality.",
            "rovescio": "Poor teamwork, lack of collaboration, mediocrity, unvalued skills. Project: Difficulty working together, low-quality results, conflicts over skills."
        }
    },
    "Quattro di Denari": {
        "it": {
            "dritto": "Controllo, stabilità, sicurezza materiale, conservatorismo, possesso. Progetto: Gestione attenta delle risorse, stabilità finanziaria, ma rischio di eccessiva rigidità.",
            "rovescio": "Avidità, paura della perdita, instabilità, cattiva gestione delle risorse, blocco. Progetto: Eccessivo attaccamento al budget/risorse che blocca il progresso, paura di investire."
        },
        "en": {
            "dritto": "Control, stability, material security, conservatism, possession. Project: Careful resource management, financial stability, but risk of excessive rigidity.",
            "rovescio": "Greed, fear of loss, instability, poor resource management, blockage. Project: Excessive attachment to budget/resources blocking progress, fear of investing."
        }
    },
    "Cinque di Denari": {
        "it": {
            "dritto": "Difficoltà finanziaria, perdita, insicurezza, isolamento, bisogno di aiuto. Progetto: Problemi di budget, mancanza di risorse, sensazione di abbandono, necessità di supporto esterno.",
            "rovescio": "Fine delle difficoltà, recupero finanziario, trovare aiuto, sentirsi inclusi. Progetto: Superamento di una crisi finanziaria, arrivo di nuove risorse o supporto."
        },
        "en": {
            "dritto": "Financial hardship, loss, insecurity, isolation, need for help. Project: Budget problems, lack of resources, feeling abandoned, need for external support.",
            "rovescio": "End of hardship, financial recovery, finding help, feeling included. Project: Overcoming a financial crisis, arrival of new resources or support."
        }
    },
    "Sei di Denari": {
        "it": {
            "dritto": "Generosità, carità, condivisione di ricchezza/conoscenza, equilibrio dare/avere. Progetto: Investimenti, finanziamenti ricevuti o dati, mentorship, giusto compenso.",
            "rovescio": "Debito, avidità, generosità calcolata, squilibrio nel dare/avere. Progetto: Problemi di debiti, cattiva gestione dei fondi, favoritismi, compensi ingiusti."
        },
        "en": {
            "dritto": "Generosity, charity, sharing wealth/knowledge, give/take balance. Project: Investments, funding received or given, mentorship, fair compensation.",
            "rovescio": "Debt, greed, calculated generosity, imbalance in giving/receiving. Project: Debt problems, poor fund management, favoritism, unfair compensation."
        }
    },
    "Sette di Denari": {
        "it": {
            "dritto": "Pazienza, valutazione degli investimenti, attesa dei risultati, lavoro a lungo termine. Progetto: Momento di valutazione del progresso, necessità di pazienza per vedere i frutti del lavoro.",
            "rovescio": "Impazienza, cattivo investimento, mancanza di risultati, lavoro sprecato. Progetto: Frustrazione per i risultati lenti, dubbi sulla strategia adottata, sforzi vani."
        },
        "en": {
            "dritto": "Patience, evaluating investments, waiting for results, long-term work. Project: Moment of progress evaluation, need for patience to see the fruits of labor.",
            "rovescio": "Impatience, bad investment, lack of results, wasted work. Project: Frustration with slow results, doubts about the adopted strategy, vain efforts."
        }
    },
    "Otto di Denari": {
        "it": {
            "dritto": "Apprendimento, maestria, attenzione ai dettagli, diligenza, lavoro meticoloso. Progetto: Fase di sviluppo competenze, lavoro di precisione, dedizione al miglioramento.",
            "rovescio": "Perfezionismo eccessivo, lavoro noioso, mancanza di ambizione, mediocrità. Progetto: Bloccarsi sui dettagli irrilevanti, lavoro ripetitivo senza crescita, scarsa qualità."
        },
        "en": {
            "dritto": "Learning, mastery, attention to detail, diligence, meticulous work. Project: Skill development phase, precision work, dedication to improvement.",
            "rovescio": "Excessive perfectionism, boring work, lack of ambition, mediocrity. Project: Getting stuck on irrelevant details, repetitive work without growth, poor quality."
        }
    },
    "Nove di Denari": {
        "it": {
            "dritto": "Indipendenza finanziaria, autosufficienza, lusso meritato, comfort, successo individuale. Progetto: Raggiungimento di un buon livello di stabilità e successo, godersi i risultati del proprio lavoro.",
            "rovescio": "Dipendenza finanziaria, eccesso di spesa, isolamento, successo superficiale. Progetto: Problemi di budget dovuti a cattiva gestione, lavorare troppo da soli, apparenza vs sostanza."
        },
        "en": {
            "dritto": "Financial independence, self-sufficiency, deserved luxury, comfort, individual success. Project: Achieving a good level of stability and success, enjoying the results of one's work.",
            "rovescio": "Financial dependence, overspending, isolation, superficial success. Project: Budget problems due to poor management, working too much alone, appearance vs substance."
        }
    },
    "Dieci di Denari": {
        "it": {
            "dritto": "Ricchezza duratura, eredità, stabilità familiare/aziendale, fondamenta solide, successo a lungo termine. Progetto: Successo consolidato, stabilità finanziaria del progetto/azienda, passaggio di consegne.",
            "rovescio": "Instabilità finanziaria, conflitti familiari/aziendali, perdita di eredità, fallimento delle fondamenta. Progetto: Problemi finanziari gravi, lotte interne per il controllo/risorse, rischio di fallimento."
        },
        "en": {
            "dritto": "Lasting wealth, legacy, family/business stability, solid foundations, long-term success. Project: Consolidated success, financial stability of the project/company, handover.",
            "rovescio": "Financial instability, family/business conflicts, loss of inheritance, foundation failure. Project: Serious financial problems, internal struggles for control/resources, risk of failure."
        }
    },
    "Fante di Denari": {
        "it": {
            "dritto": "Nuove opportunità pratiche, studio, apprendimento, messaggio riguardante denaro/lavoro. Progetto: Nuova offerta di lavoro/progetto, fase di studio/formazione, buone notizie finanziarie.",
            "rovescio": "Mancanza di impegno, cattive notizie finanziarie, procrastinazione nello studio/lavoro. Progetto: Scarsa dedizione, notizie negative sul budget, ritardi nell'apprendimento/esecuzione."
        },
        "en": {
            "dritto": "New practical opportunities, study, learning, message regarding money/work. Project: New job/project offer, study/training phase, good financial news.",
            "rovescio": "Lack of commitment, bad financial news, procrastination in study/work. Project: Poor dedication, negative budget news, delays in learning/execution."
        }
    },
    "Cavaliere di Denari": {
        "it": {
            "dritto": "Affidabilità, duro lavoro, routine, perseveranza, approccio metodico. Progetto: Membro del team/approccio molto affidabile e costante, lavoro fatto con metodo, perseveranza.",
            "rovescio": "Noia, stagnazione, pigrizia, eccessiva cautela, testardaggine. Progetto: Lavoro ripetitivo e noioso, mancanza di innovazione, eccessiva lentezza, resistenza al cambiamento."
        },
        "en": {
            "dritto": "Reliability, hard work, routine, perseverance, methodical approach. Project: Very reliable and consistent team member/approach, work done methodically, perseverance.",
            "rovescio": "Boredom, stagnation, laziness, excessive caution, stubbornness. Project: Repetitive and boring work, lack of innovation, excessive slowness, resistance to change."
        }
    },
    "Regina di Denari": {
        "it": {
            "dritto": "Praticità, nutrimento (anche materiale), affidabilità, generosità, comfort. Progetto: Leader/membro del team pratico e di supporto, buona gestione delle risorse, ambiente stabile.",
            "rovescio": "Materialismo eccessivo, soffocamento, preoccupazione per le apparenze, disordine. Progetto: Eccessiva attenzione al denaro/status, controllo opprimente, cattiva gestione pratica."
        },
        "en": {
            "dritto": "Practicality, nurturing (also material), reliability, generosity, comfort. Project: Practical and supportive leader/team member, good resource management, stable environment.",
            "rovescio": "Excessive materialism, smothering, concern for appearances, disorder. Project: Excessive focus on money/status, oppressive control, poor practical management."
        }
    },
    "Re di Denari": {
        "it": {
             "dritto": "Successo materiale, leadership affidabile, abbondanza, sicurezza, imprenditorialità solida. Progetto: Leader di successo e competente, gestione finanziaria eccellente, progetto stabile e prospero.",
             "rovescio": "Materialismo, avidità, testardaggine, corruzione, incompetenza pratica. Progetto: Leader avido o incompetente, cattiva gestione finanziaria, pratiche scorrette, rigidità eccessiva."
        },
        "en": {
             "dritto": "Material success, reliable leadership, abundance, security, solid entrepreneurship. Project: Successful and competent leader, excellent financial management, stable and prosperous project.",
             "rovescio": "Materialism, greed, stubbornness, corruption, practical incompetence. Project: Greedy or incompetent leader, poor financial management, unethical practices, excessive rigidity."
        }
    },

    # Fallback Card
    "Carta Mancante": {
         "it": {
             "dritto": "Significato dritto non disponibile per questa carta.",
             "rovescio": "Significato rovescio non disponibile per questa carta."
        },
         "en": {
             "dritto": "Upright meaning not available for this card.",
             "rovescio": "Reversed meaning not available for this card."
         }
    }
}

def get_tarot_card_display_name(card_info, lang):
    """Gets the display name of the card in the specified language."""
    return card_info.get(f"nome_{lang}", card_info.get("nome")) # Fallback to Italian name

def get_tarot_meaning(card_name_it, orientation, lang):
    """ Recupera il significato di una carta dal dizionario multilingua.
        Usa il nome italiano come chiave interna.
        L'orientamento è ancora 'dritto' o 'rovescio'.
    """
    meanings_all_langs = TAROT_MEANINGS_MULTI.get(card_name_it)

    if not meanings_all_langs:
        # Prova a gestire L' vs L\' se necessario (anche se le chiavi dovrebbero essere consistenti ora)
        normalized_name = card_name_it.replace("'", "\\'")
        meanings_all_langs = TAROT_MEANINGS_MULTI.get(normalized_name)
        if not meanings_all_langs:
            print(f"Attenzione: Nessun significato trovato per la carta '{card_name_it}'. Uso fallback.")
            meanings_all_langs = TAROT_MEANINGS_MULTI["Carta Mancante"]

    lang_meanings = meanings_all_langs.get(lang)
    if not lang_meanings:
        print(f"Attenzione: Nessun significato in lingua '{lang}' per '{card_name_it}'. Uso fallback 'en'.")
        lang_meanings = meanings_all_langs.get("en", {}) # Fallback to English

    meaning = lang_meanings.get(orientation)
    if meaning:
        return meaning
    else:
        # Fallback if orientation is wrong or missing for the language
        fallback_orientation = "dritto" if orientation == "dritto" else "rovescio"
        fallback_card = TAROT_MEANINGS_MULTI["Carta Mancante"]
        try:
            # Try to get the specific language fallback first
            fallback_meaning = fallback_card.get(lang, fallback_card["en"]).get(fallback_orientation, "Meaning not found")
        except (AttributeError, KeyError):
             # Ultimate fallback if structure is broken
             fallback_meaning = fallback_card["en"].get(fallback_orientation, "Meaning not found")

        print(f"Attenzione: Orientamento '{orientation}' non trovato per '{card_name_it}' in lingua '{lang}'. Uso fallback.")
        return fallback_meaning