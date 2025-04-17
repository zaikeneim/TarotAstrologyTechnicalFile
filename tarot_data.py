# tarot_data.py

# Struttura base del mazzo (nomi usati come chiavi nel dizionario dei significati)
MAZZO_STRUTTURA = [
    # Arcani Maggiori
    {'nome': 'Il Matto', 'arcano': 'Maggiore', 'numero': 0},
    {'nome': 'Il Mago', 'arcano': 'Maggiore', 'numero': 1},
    {'nome': 'La Papessa', 'arcano': 'Maggiore', 'numero': 2},
    {'nome': 'L\'Imperatrice', 'arcano': 'Maggiore', 'numero': 3},
    {'nome': 'L\'Imperatore', 'arcano': 'Maggiore', 'numero': 4},
    {'nome': 'Il Papa', 'arcano': 'Maggiore', 'numero': 5},
    {'nome': 'Gli Amanti', 'arcano': 'Maggiore', 'numero': 6},
    {'nome': 'Il Carro', 'arcano': 'Maggiore', 'numero': 7},
    {'nome': 'La Giustizia', 'arcano': 'Maggiore', 'numero': 8}, # O Forza (11)
    {'nome': 'L\'Eremita', 'arcano': 'Maggiore', 'numero': 9},
    {'nome': 'La Ruota della Fortuna', 'arcano': 'Maggiore', 'numero': 10},
    {'nome': 'La Forza', 'arcano': 'Maggiore', 'numero': 11}, # O Giustizia (8)
    {'nome': 'L\'Appeso', 'arcano': 'Maggiore', 'numero': 12},
    {'nome': 'La Morte', 'arcano': 'Maggiore', 'numero': 13},
    {'nome': 'La Temperanza', 'arcano': 'Maggiore', 'numero': 14},
    {'nome': 'Il Diavolo', 'arcano': 'Maggiore', 'numero': 15},
    {'nome': 'La Torre', 'arcano': 'Maggiore', 'numero': 16},
    {'nome': 'Le Stelle', 'arcano': 'Maggiore', 'numero': 17},
    {'nome': 'La Luna', 'arcano': 'Maggiore', 'numero': 18},
    {'nome': 'Il Sole', 'arcano': 'Maggiore', 'numero': 19},
    {'nome': 'Il Giudizio', 'arcano': 'Maggiore', 'numero': 20},
    {'nome': 'Il Mondo', 'arcano': 'Maggiore', 'numero': 21},

    # Arcani Minori - Bastoni
    {'nome': 'Asso di Bastoni', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 1},
    {'nome': 'Due di Bastoni', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 2},
    {'nome': 'Tre di Bastoni', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 3},
    {'nome': 'Quattro di Bastoni', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 4},
    {'nome': 'Cinque di Bastoni', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 5},
    {'nome': 'Sei di Bastoni', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 6},
    {'nome': 'Sette di Bastoni', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 7},
    {'nome': 'Otto di Bastoni', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 8},
    {'nome': 'Nove di Bastoni', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 9},
    {'nome': 'Dieci di Bastoni', 'arcano': 'Minore', 'seme': 'Bastoni', 'numero': 10},
    {'nome': 'Fante di Bastoni', 'arcano': 'Minore', 'seme': 'Bastoni', 'figura': 'Fante'},
    {'nome': 'Cavaliere di Bastoni', 'arcano': 'Minore', 'seme': 'Bastoni', 'figura': 'Cavaliere'},
    {'nome': 'Regina di Bastoni', 'arcano': 'Minore', 'seme': 'Bastoni', 'figura': 'Regina'},
    {'nome': 'Re di Bastoni', 'arcano': 'Minore', 'seme': 'Bastoni', 'figura': 'Re'},

    # Arcani Minori - Coppe
    {'nome': 'Asso di Coppe', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 1},
    {'nome': 'Due di Coppe', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 2},
    {'nome': 'Tre di Coppe', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 3},
    {'nome': 'Quattro di Coppe', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 4},
    {'nome': 'Cinque di Coppe', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 5},
    {'nome': 'Sei di Coppe', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 6},
    {'nome': 'Sette di Coppe', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 7},
    {'nome': 'Otto di Coppe', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 8},
    {'nome': 'Nove di Coppe', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 9},
    {'nome': 'Dieci di Coppe', 'arcano': 'Minore', 'seme': 'Coppe', 'numero': 10},
    {'nome': 'Fante di Coppe', 'arcano': 'Minore', 'seme': 'Coppe', 'figura': 'Fante'},
    {'nome': 'Cavaliere di Coppe', 'arcano': 'Minore', 'seme': 'Coppe', 'figura': 'Cavaliere'},
    {'nome': 'Regina di Coppe', 'arcano': 'Minore', 'seme': 'Coppe', 'figura': 'Regina'},
    {'nome': 'Re di Coppe', 'arcano': 'Minore', 'seme': 'Coppe', 'figura': 'Re'},

    # Arcani Minori - Spade
    {'nome': 'Asso di Spade', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 1},
    {'nome': 'Due di Spade', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 2},
    {'nome': 'Tre di Spade', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 3},
    {'nome': 'Quattro di Spade', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 4},
    {'nome': 'Cinque di Spade', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 5},
    {'nome': 'Sei di Spade', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 6},
    {'nome': 'Sette di Spade', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 7},
    {'nome': 'Otto di Spade', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 8},
    {'nome': 'Nove di Spade', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 9},
    {'nome': 'Dieci di Spade', 'arcano': 'Minore', 'seme': 'Spade', 'numero': 10},
    {'nome': 'Fante di Spade', 'arcano': 'Minore', 'seme': 'Spade', 'figura': 'Fante'},
    {'nome': 'Cavaliere di Spade', 'arcano': 'Minore', 'seme': 'Spade', 'figura': 'Cavaliere'},
    {'nome': 'Regina di Spade', 'arcano': 'Minore', 'seme': 'Spade', 'figura': 'Regina'},
    {'nome': 'Re di Spade', 'arcano': 'Minore', 'seme': 'Spade', 'figura': 'Re'},

    # Arcani Minori - Denari
    {'nome': 'Asso di Denari', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 1},
    {'nome': 'Due di Denari', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 2},
    {'nome': 'Tre di Denari', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 3},
    {'nome': 'Quattro di Denari', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 4},
    {'nome': 'Cinque di Denari', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 5},
    {'nome': 'Sei di Denari', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 6},
    {'nome': 'Sette di Denari', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 7},
    {'nome': 'Otto di Denari', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 8},
    {'nome': 'Nove di Denari', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 9},
    {'nome': 'Dieci di Denari', 'arcano': 'Minore', 'seme': 'Denari', 'numero': 10},
    {'nome': 'Fante di Denari', 'arcano': 'Minore', 'seme': 'Denari', 'figura': 'Fante'},
    {'nome': 'Cavaliere di Denari', 'arcano': 'Minore', 'seme': 'Denari', 'figura': 'Cavaliere'},
    {'nome': 'Regina di Denari', 'arcano': 'Minore', 'seme': 'Denari', 'figura': 'Regina'},
    {'nome': 'Re di Denari', 'arcano': 'Minore', 'seme': 'Denari', 'figura': 'Re'},
]

# Significati orientati al contesto "Progetto"
TAROT_MEANINGS = {
    # --- ARCANI MAGGIORI ---
    "Il Matto": {
        "dritto": "Nuovo inizio, potenziale grezzo, fede nell'ignoto, innovazione. Progetto: Lancio audace, approccio non convenzionale, necessità di valutare i rischi, entusiasmo iniziale.",
        "rovescio": "Avventatezza, ingenuità, caos, paura di iniziare, mancanza di preparazione. Progetto: Piani irrealistici, decisioni impulsive, rischio non calcolato, blocco all'avvio."
    },
    "Il Mago": {
        "dritto": "Abilità, risorse disponibili, volontà, manifestazione, comunicazione efficace. Progetto: Avere gli strumenti/competenze, focus sull'obiettivo, capacità di trasformare idee in realtà.",
        "rovescio": "Manipolazione, talenti sprecati, inganno, mancanza di focus, cattiva comunicazione. Progetto: Risorse non utilizzate, piani confusi, potenziale inganno o mancanza di trasparenza."
    },
    "La Papessa": {
        "dritto": "Intuizione, conoscenza nascosta, pazienza, mistero, introspezione. Progetto: Necessità di guardare oltre le apparenze, fidarsi dell'istinto, fase di studio o ricerca silenziosa.",
        "rovescio": "Segreti svelati, superficialità, ignorare l'intuizione, informazioni nascoste problematiche. Progetto: Mancanza di profondità nell'analisi, gossip, decisioni basate su dati incompleti."
    },
    "L'Imperatrice": {
        "dritto": "Creatività, nutrimento, abbondanza, fertilità, crescita. Progetto: Fase fertile e produttiva, ambiente di lavoro armonioso, sviluppo di idee, risultati tangibili.",
        "rovescio": "Blocco creativo, dipendenza, esaurimento risorse, sovra-controllo. Progetto: Creatività soffocata, problemi di budget/risorse, burnout, ambiente di lavoro opprimente."
    },
    "L'Imperatore": {
        "dritto": "Autorità, struttura, controllo, stabilità, leadership. Progetto: Necessità di ordine e pianificazione, figura di leader forte, basi solide, rispetto delle regole.",
        "rovescio": "Autoritarismo, rigidità, mancanza di controllo, caos, abuso di potere. Progetto: Leadership tirannica, eccessiva burocrazia, mancanza di flessibilità, ribellione alle regole."
    },
    "Il Papa": {
        "dritto": "Tradizione, conformità, guida spirituale/morale, istituzioni, apprendimento. Progetto: Seguire procedure consolidate, mentorship, importanza dei valori condivisi, consulenza esterna.",
        "rovescio": "Ribellione alle regole, sfidare le convenzioni, guida fuorviante, rigidità dogmatica. Progetto: Necessità di innovare oltre le norme, conflitto con la gerarchia, cattivi consigli."
    },
    "Gli Amanti": {
        "dritto": "Scelte importanti, unione, partnership, valori, comunicazione. Progetto: Decisioni cruciali da prendere, importanza della collaborazione e dell'allineamento, definizione dei valori del progetto.",
        "rovescio": "Conflitto, indecisione, scelte sbagliate, rottura di partnership, valori disallineati. Progetto: Difficoltà decisionali, tensioni nel team/partnership, comunicazione fallace."
    },
    "Il Carro": {
        "dritto": "Vittoria, determinazione, autocontrollo, azione decisa, superamento ostacoli. Progetto: Spinta in avanti, controllo degli elementi contrastanti, raggiungimento di un traguardo importante.",
        "rovescio": "Mancanza di direzione, perdita di controllo, aggressività, fallimento, ostacoli insormontabili. Progetto: Progetto fuori controllo, conflitti interni, direzione incerta, sforzi vani."
    },
    "La Giustizia": {
        "dritto": "Equità, verità, legge (causa-effetto), responsabilità, decisioni oggettive. Progetto: Necessità di trasparenza e onestà, decisioni basate sui fatti, conseguenze delle azioni passate, contratti.",
        "rovescio": "Ingiustizia, disonestà, squilibrio, eludere responsabilità, conseguenze legali negative. Progetto: Decisioni parziali, mancanza di trasparenza, dispute contrattuali, problemi legali."
    },
    "L'Eremita": {
        "dritto": "Introspezione, ricerca interiore, guida, saggezza, ritiro temporaneo. Progetto: Fase di riflessione, analisi approfondita, ricerca di consiglio esperto, necessità di lavorare in solitudine.",
        "rovescio": "Isolamento, solitudine, rifiuto della guida, eccessiva prudenza, ritardi. Progetto: Lavorare troppo isolati, paura di agire, informazioni chiave ignorate, stagnazione."
    },
    "La Ruota della Fortuna": {
        "dritto": "Cambiamento, cicli, destino, fortuna, eventi inaspettati (positivi). Progetto: Punto di svolta, cambiamento di direzione, fattori esterni favorevoli, adattabilità richiesta.",
        "rovescio": "Sfortuna, eventi negativi inaspettati, resistenza al cambiamento, cicli negativi. Progetto: Imprevisti problematici, resistenza all'adattamento, periodo difficile, fattori esterni sfavorevoli."
    },
    "La Forza": {
        "dritto": "Coraggio interiore, pazienza, controllo emotivo, influenza gentile, compassione. Progetto: Affrontare le sfide con calma e resilienza, gestire situazioni difficili con diplomazia, forza morale.",
        "rovescio": "Debolezza,insicurezza, rabbia incontrollata, mancanza di autodisciplina. Progetto: Reazioni emotive sproporzionate, mancanza di fiducia nelle proprie capacità, conflitti interni."
    },
    "L'Appeso": {
        "dritto": "Sacrificio, attesa, nuova prospettiva, sospensione, lasciar andare. Progetto: Necessità di una pausa per rivalutare, vedere le cose da un'altra angolazione, sacrificio necessario per un bene maggiore.",
        "rovescio": "Stallo inutile, rifiuto di sacrificarsi, martirio, indecisione prolungata. Progetto: Progetto bloccato senza motivo apparente, incapacità di fare le scelte necessarie, sforzi sprecati."
    },
    "La Morte": {
        "dritto": "Fine necessaria, trasformazione, cambiamento radicale, lasciar andare il passato. Progetto: Chiusura di una fase, necessità di abbandonare vecchi metodi, trasformazione significativa.",
        "rovescio": "Resistenza al cambiamento, paura della fine, stagnazione, fine dolorosa ma ritardata. Progetto: Aggrapparsi a ciò che non funziona più, paura di chiudere, processo di cambiamento bloccato."
    },
    "La Temperanza": {
        "dritto": "Equilibrio, moderazione, pazienza, integrazione, armonia. Progetto: Trovare il giusto mezzo, combinare diverse risorse/idee, pazienza nel processo, team ben bilanciato.",
        "rovescio": "Squilibrio, eccesso, impazienza, conflitto, mancanza di visione a lungo termine. Progetto: Estremismi, risorse mal gestite, conflitti tra diverse parti, fretta eccessiva."
    },
    "Il Diavolo": {
        "dritto": "Attaccamento materiale, dipendenza, limitazioni autoimposte, tentazione, potere oscuro. Progetto: Attenzione a scorciatoie non etiche, dipendenza da un approccio/risorsa, dinamiche di potere tossiche.",
        "rovescio": "Rompere le catene, libertà, distacco, consapevolezza delle limitazioni. Progetto: Liberarsi da vincoli (contrattuali, mentali), prendere coscienza di dinamiche negative e agire."
    },
    "La Torre": {
        "dritto": "Distruzione improvvisa, rivelazione scioccante, caos, cambiamento forzato, crollo di strutture. Progetto: Crisi improvvisa, fallimento di piani, necessità di ricostruire dalle fondamenta.",
        "rovescio": "Evitare il disastro, paura del cambiamento, ritardare l'inevitabile, crisi più contenuta. Progetto: Riuscire a evitare il peggio, ma la necessità di cambiamento rimane, disagio latente."
    },
    "Le Stelle": {
        "dritto": "Speranza, ispirazione, guarigione, serenità, guida spirituale. Progetto: Ottimismo per il futuro, visione chiara, ispirazione rinnovata, periodo di calma dopo la tempesta.",
        "rovescio": "Disperazione, mancanza di fede, scoraggiamento, visione offuscata. Progetto: Perdita di motivazione, pessimismo, sentirsi persi o senza direzione chiara."
    },
    "La Luna": {
        "dritto": "Illusione, paura, ansia, inconscio, confusione, intuizione profonda. Progetto: Attenzione a ciò che non è chiaro, paura dell'ignoto, informazioni nascoste, fidarsi dell'istinto ma verificare.",
        "rovescio": "Chiarezza emergente, paure superate, confusione che si dissipa, verità rivelata. Progetto: Superamento di un periodo di incertezza, comprensione di dinamiche nascoste."
    },
    "Il Sole": {
        "dritto": "Successo, vitalità, gioia, chiarezza, ottimismo, realizzazione. Progetto: Successo evidente, energia positiva, team entusiasta, obiettivi raggiunti, chiarezza strategica.",
        "rovescio": "Successo ritardato, ottimismo eccessivo, mancanza di chiarezza, arroganza. Progetto: Risultati meno brillanti del previsto, sottovalutare le sfide, difficoltà a vedere i problemi."
    },
    "Il Giudizio": {
        "dritto": "Risveglio, resa dei conti, valutazione, rinnovamento, chiamata a uno scopo superiore. Progetto: Valutazione finale, momento di bilancio, decisione importante sul futuro, rinnovamento degli obiettivi.",
        "rovescio": "Autocritica eccessiva, paura del giudizio, ignorare la chiamata, opportunità perse. Progetto: Incapacità di valutare oggettivamente, paura delle conseguenze, rimanere bloccati nel passato."
    },
    "Il Mondo": {
        "dritto": "Completamento, integrazione, successo, realizzazione, fine di un ciclo. Progetto: Conclusione positiva del progetto, raggiungimento di tutti gli obiettivi, integrazione riuscita, soddisfazione.",
        "rovescio": "Incompletezza, mancanza di chiusura, successo parziale, ritardi finali. Progetto: Progetto non concluso del tutto, obiettivi mancati, difficoltà nell'integrazione finale, sensazione di incompiuto."
    },

    # --- ARCANI MINORI: BASTONI (Elemento Fuoco: Energia, Azione, Creatività, Impresa) ---
    "Asso di Bastoni": {
        "dritto": "Nuova scintilla creativa, ispirazione, potenziale, inizio energico, intraprendenza. Progetto: Kick-off entusiasta, nuova idea promettente, fase di avvio dinamica.",
        "rovescio": "Mancanza di energia, ritardi, falsa partenza, blocco creativo, idee non realizzate. Progetto: Difficoltà a iniziare, mancanza di motivazione, ostacoli iniziali."
    },
    "Due di Bastoni": {
        "dritto": "Pianificazione futura, progresso iniziale, decisioni, scoperta, valutazione opzioni. Progetto: Fase di pianificazione strategica, scelta della direzione, valutazione di partnership.",
        "rovescio": "Paura dell'ignoto, mancanza di pianificazione, indecisione, piani bloccati. Progetto: Incapacità di decidere la strategia, paura di espandersi, limitazioni autoimposte."
    },
    "Tre di Bastoni": {
        "dritto": "Espansione, lungimiranza, attesa dei risultati, preparazione, collaborazione iniziale. Progetto: Primi risultati positivi, espansione delle attività, visione a lungo termine.",
        "rovescio": "Ritardi nei risultati, ostacoli all'espansione, mancanza di visione, piani irrealistici. Progetto: Le aspettative non si concretizzano, difficoltà di crescita, poca lungimiranza."
    },
    "Quattro di Bastoni": {
        "dritto": "Celebrazione, armonia, stabilità raggiunta, traguardo intermedio, lavoro di squadra positivo. Progetto: Raggiungimento di una milestone importante, team coeso, ambiente positivo.",
        "rovescio": "Mancanza di armonia, instabilità, celebrazione prematura, tensioni nascoste. Progetto: Conflitti nel team, risultati instabili, festeggiamenti fuori luogo."
    },
    "Cinque di Bastoni": {
        "dritto": "Conflitto, competizione, disaccordo, sfide, diverse opinioni. Progetto: Discussioni accese, competizione interna/esterna, necessità di gestire opinioni divergenti.",
        "rovescio": "Evitare il conflitto, accordo forzato, tensione repressa, fine della competizione. Progetto: Paura di affrontare i problemi, accordi superficiali, possibile risoluzione dei conflitti."
    },
    "Sei di Bastoni": {
        "dritto": "Successo pubblico, riconoscimento, vittoria, leadership acclamata, progresso. Progetto: Raggiungimento di un obiettivo chiave con successo, riconoscimento del lavoro svolto, morale alto.",
        "rovescio": "Fallimento, mancanza di riconoscimento, tradimento, arroganza dopo il successo. Progetto: Obiettivo mancato, lavoro non apprezzato, possibile sabotaggio, eccessiva sicurezza."
    },
    "Sette di Bastoni": {
        "dritto": "Difesa, perseveranza, sfida, mantenere la propria posizione, coraggio. Progetto: Difendere il progetto da critiche o ostacoli, perseverare nonostante le difficoltà.",
        "rovescio": "Sopraffazione, arrendersi, stanchezza, perdere terreno, mancanza di fiducia. Progetto: Sentirsi sopraffatti dalle sfide, dubitare della validità del progetto, cedere alle pressioni."
    },
    "Otto di Bastoni": {
        "dritto": "Movimento rapido, azione veloce, comunicazione rapida, notizie in arrivo, progresso accelerato. Progetto: Sviluppi rapidi, decisioni veloci necessarie, comunicazioni importanti.",
        "rovescio": "Ritardi, frustrazione, rallentamenti, comunicazioni bloccate, resistenza al progresso. Progetto: Ostacoli che rallentano tutto, difficoltà di comunicazione, inerzia."
    },
    "Nove di Bastoni": {
        "dritto": "Resilienza, ultima resistenza, stanchezza ma non sconfitta, preparazione alla battaglia finale. Progetto: Quasi alla fine ma esausti, necessità di un ultimo sforzo, difendere i risultati raggiunti.",
        "rovescio": "Esaurimento, sconfitta imminente, mancanza di difese, paranoia, rigidità. Progetto: Burnout, incapacità di sostenere lo sforzo finale, sentirsi attaccati da tutte le parti."
    },
    "Dieci di Bastoni": {
        "dritto": "Fardello pesante, responsabilità eccessiva, stress, duro lavoro che porta a termine. Progetto: Carico di lavoro insostenibile, troppe responsabilità su pochi, fase finale molto faticosa.",
        "rovescio": "Rilasciare il fardello, delegare, sovraccarico che porta al collasso, incapacità di gestire. Progetto: Necessità di delegare o semplificare, rischio di fallimento per troppo carico."
    },
    "Fante di Bastoni": {
        "dritto": "Esplorazione, entusiasmo, nuove idee, messaggero di buone notizie, spirito libero. Progetto: Nuove proposte creative, membro del team entusiasta, fase di esplorazione.",
        "rovescio": "Idee immature, mancanza di direzione, notizie deludenti, impulsività, procrastinazione. Progetto: Proposte poco pratiche, entusiasmo superficiale, ritardi nelle comunicazioni."
    },
    "Cavaliere di Bastoni": {
        "dritto": "Azione rapida, avventura, impulsività, passione, carisma energetico. Progetto: Agire rapidamente, prendere l'iniziativa, energia contagiosa, ma rischio di avventatezza.",
        "rovescio": "Azione spericolata, ritardi frustranti, mancanza di energia, aggressività. Progetto: Decisioni affrettate e sbagliate, progetto bloccato, conflitti dovuti all'impulsività."
    },
    "Regina di Bastoni": {
        "dritto": "Confidenza, indipendenza, leadership carismatica, determinazione, calore. Progetto: Leader/membro del team capace e ispiratore, ambiente di lavoro vivace, determinazione.",
        "rovescio": "Intolleranza, gelosia, prepotenza, esaurimento energetico. Progetto: Leadership autoritaria, conflitti di potere, ambiente stressante, burnout."
    },
    "Re di Bastoni": {
        "dritto": "Visione, leadership naturale, imprenditorialità, onore, ispirazione. Progetto: Leader visionario, strategia chiara, capacità di ispirare il team, prendere rischi calcolati.",
        "rovescio": "Autoritarismo, intolleranza, impulsività, aspettative irrealistiche, leadership debole. Progetto: Capo dispotico, piani irrealistici, mancanza di direzione strategica."
    },

    # --- ARCANI MINORI: COPPE (Elemento Acqua: Emozioni, Relazioni, Intuizione, Creatività Artistica) ---
    "Asso di Coppe": {
        "dritto": "Nuovo amore/emozione, creatività, intuizione, compassione, inizio di relazione (anche lavorativa). Progetto: Buon clima emotivo nel team, inizio di collaborazioni positive, flusso creativo.",
        "rovescio": "Emozioni bloccate, creatività repressa, rifiuto, tristezza, opportunità emotive mancate. Progetto: Mancanza di coesione nel team, blocchi creativi, difficoltà relazionali."
    },
    "Due di Coppe": {
        "dritto": "Unione, partnership, attrazione reciproca, armonia, collaborazione efficace. Progetto: Partnership solida, buona intesa nel team, accordo raggiunto, collaborazione fruttuosa.",
        "rovescio": "Disarmonia, rottura di partnership, sfiducia, squilibrio, comunicazione difficile. Progetto: Conflitti tra partner o nel team, mancanza di fiducia, accordi falliti."
    },
    "Tre di Coppe": {
        "dritto": "Celebrazione, amicizia, comunità, collaborazione gioiosa, successo condiviso. Progetto: Team affiatato, celebrazione di un successo, buon ambiente di lavoro, eventi sociali positivi.",
        "rovescio": "Gossip, eccessi, isolamento, fine dell'armonia, celebrazione fuori luogo. Progetto: Pettegolezzi che minano il team, collaborazione superficiale, sentirsi esclusi."
    },
    "Quattro di Coppe": {
        "dritto": "Apatia, contemplazione, disinteresse, opportunità mancate, introspezione. Progetto: Mancanza di motivazione, rifiuto di nuove proposte, periodo di stasi riflessiva.",
        "rovescio": "Interesse rinnovato, accettazione di offerte, fine dell'apatia, nuove possibilità. Progetto: Ritrovare la motivazione, cogliere nuove opportunità, uscire da una fase di stallo."
    },
    "Cinque di Coppe": {
        "dritto": "Perdita, rimpianto, delusione, concentrarsi sul negativo, tristezza. Progetto: Fallimento parziale, delusione per i risultati, focalizzarsi sugli errori, morale basso.",
        "rovescio": "Accettazione, perdono, vedere il positivo, superare il rimpianto, andare avanti. Progetto: Imparare dagli errori, superare una battuta d'arresto, vedere nuove prospettive."
    },
    "Sei di Coppe": {
        "dritto": "Nostalgia, ricordi felici, generosità, armonia passata, doni. Progetto: Basarsi su successi passati, collaborazione basata su vecchie relazioni, ritorno a metodi collaudati.",
        "rovescio": "Aggrapparsi al passato, mancanza di prospettiva futura, ricordi dolorosi, ingenuità. Progetto: Incapacità di innovare, vivere di rendita, idealizzare il passato."
    },
    "Sette di Coppe": {
        "dritto": "Scelte multiple, illusioni, sogni ad occhi aperti, tentazioni, immaginazione. Progetto: Troppe opzioni tra cui scegliere, rischio di illusioni, necessità di concretezza.",
        "rovescio": "Chiarezza, decisione presa, realtà che si impone, evitare le tentazioni. Progetto: Scelta finalmente fatta, focus su opzioni realistiche, superamento della confusione."
    },
    "Otto di Coppe": {
        "dritto": "Abbandono, ricerca di qualcosa di più, allontanarsi, delusione che porta al cambiamento. Progetto: Abbandonare un approccio/progetto insoddisfacente, cercare nuove strade.",
        "rovescio": "Paura di andarsene, rimanere in una situazione insoddisfacente, ritorno sui propri passi. Progetto: Incapacità di lasciare ciò che non funziona, paura del cambiamento, stagnazione."
    },
    "Nove di Coppe": {
        "dritto": "Soddisfazione, desiderio esaudito, piacere, contentezza, successo emotivo. Progetto: Raggiungimento di un obiettivo desiderato, soddisfazione personale e del team, successo.",
        "rovescio": "Insoddisfazione, desideri non realizzati, avidità, compiacenza eccessiva. Progetto: Obiettivi non raggiunti, aspettative deluse, rischio di adagiarsi sugli allori."
    },
    "Dieci di Coppe": {
        "dritto": "Felicità familiare/comunitaria, armonia duratura, realizzazione emotiva, pace. Progetto: Team perfettamente allineato e felice, successo completo e condiviso, ambiente ideale.",
        "rovescio": "Famiglia/comunità disfunzionale, conflitto, felicità superficiale, rottura dell'armonia. Progetto: Gravi conflitti nel team, mancanza di coesione, successo apparente ma problemi di fondo."
    },
    "Fante di Coppe": {
        "dritto": "Messaggero emotivo, intuizione, creatività nascente, sensibilità, nuove idee emotive. Progetto: Notizie positive sul fronte relazionale/creativo, membro del team intuitivo e sensibile.",
        "rovescio": "Immaturità emotiva, blocchi creativi, cattive notizie emotive, ipersensibilità. Progetto: Reazioni emotive infantili, mancanza di ispirazione, notizie deludenti."
    },
    "Cavaliere di Coppe": {
        "dritto": "Romanticismo, fascino, offerta emotiva, seguire il cuore, diplomazia. Progetto: Approccio diplomatico, proposta collaborativa, agire guidati da valori positivi.",
        "rovescio": "Irrealismo, umoralità, manipolazione emotiva, offerte insincere. Progetto: Proposte irrealistiche, eccessiva emotività nelle decisioni, possibile inganno."
    },
    "Regina di Coppe": {
        "dritto": "Compassione, intuizione, empatia, nutrimento emotivo, saggezza interiore. Progetto: Leader/membro del team empatico e di supporto, attenzione al benessere del team, guida intuitiva.",
        "rovescio": "Ipersensibilità, dipendenza emotiva, manipolazione, instabilità emotiva. Progetto: Eccessiva emotività che crea problemi, bisogno di approvazione costante, possibile vittimismo."
    },
    "Re di Coppe": {
        "dritto": "Controllo emotivo, compassione matura, equilibrio tra cuore e mente, diplomazia, tolleranza. Progetto: Leader equilibrato e saggio, gestione calma delle crisi, diplomazia efficace.",
        "rovescio": "Manipolazione emotiva, umoralità, freddezza emotiva, abuso di potere emotivo. Progetto: Leader che usa le emozioni per manipolare, instabilità, mancanza di empatia reale."
    },

    # --- ARCANI MINORI: SPADE (Elemento Aria: Intelletto, Comunicazione, Conflitto, Verità, Sfide) ---
    "Asso di Spade": {
        "dritto": "Chiarezza mentale, nuova idea brillante, verità, taglio netto, decisione. Progetto: Momento di grande chiarezza strategica, idea innovativa, decisione importante presa.",
        "rovescio": "Confusione, mancanza di idee, decisione sbagliata, comunicazione fallace, potenziale conflitto. Progetto: Piani confusi, idee non valide, cattiva comunicazione, inizio di dispute."
    },
    "Due di Spade": {
        "dritto": "Indecisione, stallo, scelta difficile, tregua temporanea, necessità di equilibrio. Progetto: Blocco decisionale, necessità di valutare attentamente due opzioni, tregua in un conflitto.",
        "rovescio": "Decisione forzata o sbagliata, confusione, tradimento, ripresa del conflitto. Progetto: Scelta difficile fatta male, informazioni fuorvianti, fine della tregua."
    },
    "Tre di Spade": {
        "dritto": "Dolore, perdita, tradimento, verità dolorosa, conflitto aperto. Progetto: Notizie negative, fallimento che causa dolore, conflitto che emerge chiaramente, rottura di fiducia.",
        "rovescio": "Guarigione dal dolore, perdono, superamento del conflitto, verità accettata. Progetto: Superamento di una crisi, risoluzione (anche se dolorosa) di un conflitto, accettazione della realtà."
    },
    "Quattro di Spade": {
        "dritto": "Riposo, recupero, contemplazione, pausa necessaria, tregua. Progetto: Necessità di una pausa per ricaricarsi, fase di riflessione dopo un periodo intenso, recupero.",
        "rovescio": "Stagnazione, esaurimento, rifiuto di riposare, ripresa forzata. Progetto: Pausa che si trasforma in blocco, burnout per mancanza di riposo, ripartenza prematura."
    },
    "Cinque di Spade": {
        "dritto": "Conflitto umiliante, vittoria a caro prezzo, perdita, ostilità, prepotenza. Progetto: Conflitto distruttivo, vincere ma perdere relazioni, ambiente di lavoro tossico.",
        "rovescio": "Fine del conflitto, possibilità di riconciliazione, consapevolezza delle perdite, rilascio della tensione. Progetto: Possibile risoluzione di un conflitto aspro, presa di coscienza dei danni fatti."
    },
    "Sei di Spade": {
        "dritto": "Transizione, superamento difficoltà, viaggio (anche metaforico), andare verso acque più calme. Progetto: Superamento di una fase difficile, transizione verso una situazione migliore, aiuto ricevuto.",
        "rovescio": "Transizione bloccata, resistenza al cambiamento, ritorno ai problemi, viaggio difficile. Progetto: Difficoltà a superare i problemi, rimanere bloccati nel passato, ostacoli imprevisti."
    },
    "Sette di Spade": {
        "dritto": "Inganno, furto, strategia nascosta, agire da soli, eludere. Progetto: Attenzione a comportamenti scorretti, strategie non trasparenti, possibile furto di idee/risorse.",
        "rovescio": "Confessione, ritorno all'onestà, smascheramento, consiglio prezioso ignorato. Progetto: Inganni scoperti, ritorno alla trasparenza, affrontare le conseguenze di azioni nascoste."
    },
    "Otto di Spade": {
        "dritto": "Restrizione autoimposta, sentirsi intrappolati, impotenza, paura di agire. Progetto: Sentirsi bloccati da limiti mentali più che reali, paura di prendere decisioni, mancanza di prospettive.",
        "rovescio": "Liberazione, trovare soluzioni, superare le paure, vedere nuove possibilità. Progetto: Riconoscere i propri limiti autoimposti e superarli, trovare vie d'uscita, agire."
    },
    "Nove di Spade": {
        "dritto": "Ansia, preoccupazione, incubi, stress mentale, paura profonda. Progetto: Forte stress legato al progetto, ansia per il futuro, preoccupazioni che tengono svegli la notte.",
        "rovescio": "Rilascio dell'ansia, superamento delle paure, ricerca di aiuto, vedere la luce. Progetto: Affrontare le cause dello stress, trovare supporto, le preoccupazioni si ridimensionano."
    },
    "Dieci di Spade": {
        "dritto": "Fine dolorosa, fallimento completo, fondo toccato, tradimento finale, esaurimento. Progetto: Fallimento definitivo, fine di un progetto/fase in modo traumatico, necessità di accettare la fine.",
        "rovescio": "Sopravvivenza, ripresa dopo il disastro, fine del ciclo negativo, lezione imparata. Progetto: Anche se fallito, si impara qualcosa; possibilità di ripartire dopo aver toccato il fondo."
    },
    "Fante di Spade": {
        "dritto": "Curiosità, ricerca della verità, vigilanza, comunicazione diretta, nuove idee analitiche. Progetto: Membro del team analitico e curioso, comunicazione schietta, raccolta di informazioni.",
        "rovescio": "Gossip, comunicazione offensiva, indiscrezione, mancanza di tatto, paranoia. Progetto: Comunicazione che crea problemi, diffusione di notizie false o dannose, sospettosità eccessiva."
    },
    "Cavaliere di Spade": {
        "dritto": "Azione rapida e decisa, ambizione, focalizzazione, andare dritti al punto. Progetto: Agire con determinazione e velocità, approccio diretto ai problemi, focus sull'obiettivo.",
        "rovescio": "Azione spericolata, aggressività, mancanza di pianificazione, fanatismo. Progetto: Decisioni affrettate e aggressive, non considerare le conseguenze, conflitti inutili."
    },
    "Regina di Spade": {
        "dritto": "Intelligenza acuta, indipendenza, onestà brutale, chiarezza di pensiero, esperienza. Progetto: Leader/membro del team molto intelligente e diretto, capace di analisi critica, non teme la verità.",
        "rovescio": "Critica eccessiva, amarezza, isolamento, freddezza, malizia. Progetto: Critica distruttiva, ambiente freddo e ostile, possibile sabotaggio intellettuale."
    },
    "Re di Spade": {
        "dritto": "Autorità intellettuale, verità, giustizia, etica, leadership basata sulla logica. Progetto: Leader giusto ed etico, decisioni basate su fatti e logica, chiarezza mentale e strategica.",
        "rovescio": "Autoritarismo intellettuale, cinismo, crudeltà, giudizio severo, abuso di potere mentale. Progetto: Leader che usa l'intelletto per dominare, mancanza di empatia, decisioni spietate."
    },

    # --- ARCANI MINORI: DENARI (Elemento Terra: Mondo Materiale, Lavoro, Finanze, Praticità, Risorse) ---
    "Asso di Denari": {
        "dritto": "Nuova opportunità (lavoro/finanza), manifestazione concreta, risorse, inizio solido. Progetto: Nuova offerta, finanziamento approvato, inizio pratico del lavoro, basi solide.",
        "rovescio": "Opportunità persa, cattiva gestione finanziaria, mancanza di pianificazione pratica, ritardi. Progetto: Finanziamento rifiutato, piani poco pratici, ritardi nell'avvio concreto."
    },
    "Due di Denari": {
        "dritto": "Equilibrio, gestione di più priorità, adattabilità, flessibilità, multitasking. Progetto: Gestire diverse attività contemporaneamente, bilanciare budget/tempo, adattarsi ai cambiamenti.",
        "rovescio": "Squilibrio, cattiva gestione, sovraccarico, stress finanziario, inflessibilità. Progetto: Difficoltà a gestire tutto, budget fuori controllo, incapacità di adattarsi.",
    },
    "Tre di Denari": {
        "dritto": "Lavoro di squadra, collaborazione, abilità riconosciuta, qualità, apprendimento. Progetto: Teamwork efficace, riconoscimento delle competenze, focus sulla qualità del lavoro.",
        "rovescio": "Lavoro di squadra scadente, mancanza di collaborazione, mediocrità, competenze non valorizzate. Progetto: Difficoltà a lavorare insieme, risultati di bassa qualità, conflitti sulle competenze."
    },
    "Quattro di Denari": {
        "dritto": "Controllo, stabilità, sicurezza materiale, conservatorismo, possesso. Progetto: Gestione attenta delle risorse, stabilità finanziaria, ma rischio di eccessiva rigidità.",
        "rovescio": "Avidità, paura della perdita, instabilità, cattiva gestione delle risorse, blocco. Progetto: Eccessivo attaccamento al budget/risorse che blocca il progresso, paura di investire."
    },
    "Cinque di Denari": {
        "dritto": "Difficoltà finanziaria, perdita, insicurezza, isolamento, bisogno di aiuto. Progetto: Problemi di budget, mancanza di risorse, sensazione di abbandono, necessità di supporto esterno.",
        "rovescio": "Fine delle difficoltà, recupero finanziario, trovare aiuto, sentirsi inclusi. Progetto: Superamento di una crisi finanziaria, arrivo di nuove risorse o supporto."
    },
    "Sei di Denari": {
        "dritto": "Generosità, carità, condivisione di ricchezza/conoscenza, equilibrio dare/avere. Progetto: Investimenti, finanziamenti ricevuti o dati, mentorship, giusto compenso.",
        "rovescio": "Debito, avidità, generosità calcolata, squilibrio nel dare/avere. Progetto: Problemi di debiti, cattiva gestione dei fondi, favoritismi, compensi ingiusti."
    },
    "Sette di Denari": {
        "dritto": "Pazienza, valutazione degli investimenti, attesa dei risultati, lavoro a lungo termine. Progetto: Momento di valutazione del progresso, necessità di pazienza per vedere i frutti del lavoro.",
        "rovescio": "Impazienza, cattivo investimento, mancanza di risultati, lavoro sprecato. Progetto: Frustrazione per i risultati lenti, dubbi sulla strategia adottata, sforzi vani."
    },
    "Otto di Denari": {
        "dritto": "Apprendimento, maestria, attenzione ai dettagli, diligenza, lavoro meticoloso. Progetto: Fase di sviluppo competenze, lavoro di precisione, dedizione al miglioramento.",
        "rovescio": "Perfezionismo eccessivo, lavoro noioso, mancanza di ambizione, mediocrità. Progetto: Bloccarsi sui dettagli irrilevanti, lavoro ripetitivo senza crescita, scarsa qualità."
    },
    "Nove di Denari": {
        "dritto": "Indipendenza finanziaria, autosufficienza, lusso meritato, comfort, successo individuale. Progetto: Raggiungimento di un buon livello di stabilità e successo, godersi i risultati del proprio lavoro.",
        "rovescio": "Dipendenza finanziaria, eccesso di spesa, isolamento, successo superficiale. Progetto: Problemi di budget dovuti a cattiva gestione, lavorare troppo da soli, apparenza vs sostanza."
    },
    "Dieci di Denari": {
        "dritto": "Ricchezza duratura, eredità, stabilità familiare/aziendale, fondamenta solide, successo a lungo termine. Progetto: Successo consolidato, stabilità finanziaria del progetto/azienda, passaggio di consegne.",
        "rovescio": "Instabilità finanziaria, conflitti familiari/aziendali, perdita di eredità, fallimento delle fondamenta. Progetto: Problemi finanziari gravi, lotte interne per il controllo/risorse, rischio di fallimento."
    },
    "Fante di Denari": {
        "dritto": "Nuove opportunità pratiche, studio, apprendimento, messaggio riguardante denaro/lavoro. Progetto: Nuova offerta di lavoro/progetto, fase di studio/formazione, buone notizie finanziarie.",
        "rovescio": "Mancanza di impegno, cattive notizie finanziarie, procrastinazione nello studio/lavoro. Progetto: Scarsa dedizione, notizie negative sul budget, ritardi nell'apprendimento/esecuzione."
    },
    "Cavaliere di Denari": {
        "dritto": "Affidabilità, duro lavoro, routine, perseveranza, approccio metodico. Progetto: Membro del team/approccio molto affidabile e costante, lavoro fatto con metodo, perseveranza.",
        "rovescio": "Noia, stagnazione, pigrizia, eccessiva cautela, testardaggine. Progetto: Lavoro ripetitivo e noioso, mancanza di innovazione, eccessiva lentezza, resistenza al cambiamento."
    },
    "Regina di Denari": {
        "dritto": "Praticità, nutrimento (anche materiale), affidabilità, generosità, comfort. Progetto: Leader/membro del team pratico e di supporto, buona gestione delle risorse, ambiente stabile.",
        "rovescio": "Materialismo eccessivo, soffocamento, preoccupazione per le apparenze, disordine. Progetto: Eccessiva attenzione al denaro/status, controllo opprimente, cattiva gestione pratica."
    },
    "Re di Denari": {
        "dritto": "Successo materiale, leadership affidabile, abbondanza, sicurezza, imprenditorialità solida. Progetto: Leader di successo e competente, gestione finanziaria eccellente, progetto stabile e prospero.",
        "rovescio": "Materialismo, avidità, testardaggine, corruzione, incompetenza pratica. Progetto: Leader avido o incompetente, cattiva gestione finanziaria, pratiche scorrette, rigidità eccessiva."
    },

    # Fallback per sicurezza
    "Carta Mancante": {
         "dritto": "Significato dritto non disponibile per questa carta.",
         "rovescio": "Significato rovescio non disponibile per questa carta."
    }
}

def get_tarot_meaning(card_name, orientation):
    """ Recupera il significato di una carta dal dizionario. """
    # Tenta di trovare la corrispondenza esatta
    meanings = TAROT_MEANINGS.get(card_name)
    if meanings:
        return meanings.get(orientation, f"Orientamento '{orientation}' non valido per {card_name}.")
    else:
        # Se non trova il nome esatto, prova a normalizzare (es. L'Imperatrice vs L\'Imperatrice)
        # Questo è un tentativo base, potrebbe essere migliorato
        normalized_name = card_name.replace("'", "\\'")
        meanings = TAROT_MEANINGS.get(normalized_name)
        if meanings:
             return meanings.get(orientation, f"Orientamento '{orientation}' non valido per {normalized_name}.")
        else:
            # Se ancora non trova, usa il fallback
            print(f"Attenzione: Nessun significato trovato per la carta '{card_name}'. Uso fallback.")
            fallback_meanings = TAROT_MEANINGS["Carta Mancante"]
            return fallback_meanings.get(orientation, "Orientamento non valido per fallback.")


# --- Esempio d'uso (puoi rimuoverlo) ---
# if __name__ == '__main__':
#     # Test rapido per verificare che le chiavi e la funzione funzionino
#     print("Verifica rapida significati:")
#     test_cards = ["Il Matto", "Dieci di Spade", "Regina di Denari", "Carta Inesistente", "L'Imperatrice"]
#     for card in test_cards:
#         print(f"\n--- {card} ---")
#         print(f"Dritto: {get_tarot_meaning(card, 'dritto')}")
#         print(f"Rovescio: {get_tarot_meaning(card, 'rovescio')}")
#
#     print(f"\nNumero totale di carte definite in MAZZO_STRUTTURA: {len(MAZZO_STRUTTURA)}")
#     print(f"Numero totale di significati definiti in TAROT_MEANINGS (escluso fallback): {len(TAROT_MEANINGS) - 1}")
#     if len(MAZZO_STRUTTURA) == len(TAROT_MEANINGS) - 1:
#         print("OK: Numero di carte e significati corrispondono.")
#     else:
#         print("ATTENZIONE: Il numero di carte nella struttura e nei significati non corrisponde!")