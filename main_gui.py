# main_gui.py
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from datetime import datetime
from logic import genera_report_proiezione # Importa la funzione logica principale
# Importa dati e funzioni di localizzazione
from localization import (
    LANGUAGES, set_language, get_string, CURRENT_LANG,
    get_internal_sign_key, get_valid_sign_display_names, get_display_sign_name
)
# Non servono più import diretti da tarot_data/astrology_data qui
# se non per validazione avanzata (ma usiamo get_valid_sign_display_names)

class TarotAstroApp:
    def __init__(self, root):
        self.root = root
        # Titolo iniziale, verrà aggiornato
        self.root.title(get_string("window_title"))

        # Stile
        style = ttk.Style()
        style.theme_use('clam')

        # Frame principale
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # --- Sezione Lingua ---
        lang_frame = ttk.Frame(self.main_frame)
        lang_frame.grid(row=0, column=0, sticky=tk.E, padx=5, pady=(0,5))

        self.lang_label = ttk.Label(lang_frame, text=get_string("language_select_label"))
        self.lang_label.grid(row=0, column=0, padx=(0, 5))

        self.selected_lang = tk.StringVar(value=CURRENT_LANG)
        # Crea opzioni (es: "en: English", "it: Italiano")
        lang_options = [f"{code}: {name}" for code, name in LANGUAGES.items()]
        self.lang_combobox = ttk.Combobox(lang_frame, textvariable=self.selected_lang,
                                          values=lang_options, state="readonly", width=15)
        # Imposta il valore iniziale visualizzato correttamente
        self.lang_combobox.set(f"{CURRENT_LANG}: {LANGUAGES[CURRENT_LANG]}")
        self.lang_combobox.grid(row=0, column=1)
        self.lang_combobox.bind("<<ComboboxSelected>>", self.change_language)


        # --- Sezione Input ---
        self.input_frame = ttk.LabelFrame(self.main_frame, text=get_string("project_data_frame"), padding="10")
        self.input_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=5, pady=5)
        self.input_frame.columnconfigure(1, weight=1)

        self.label_project_name = ttk.Label(self.input_frame, text=get_string("label_project_name"))
        self.label_project_name.grid(row=0, column=0, sticky=tk.W, pady=2)
        self.nome_progetto_entry = ttk.Entry(self.input_frame, width=40)
        self.nome_progetto_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=2)

        self.label_description = ttk.Label(self.input_frame, text=get_string("label_description"))
        self.label_description.grid(row=1, column=0, sticky=tk.W, pady=2)
        self.descrizione_entry = ttk.Entry(self.input_frame, width=40)
        self.descrizione_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=2)

        self.label_start_date = ttk.Label(self.input_frame, text=get_string("label_start_date"))
        self.label_start_date.grid(row=2, column=0, sticky=tk.W, pady=2)
        self.data_inizio_entry = ttk.Entry(self.input_frame, width=15)
        self.data_inizio_entry.grid(row=2, column=1, sticky=tk.W, pady=2)
        self.data_inizio_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))

        self.label_participants_num = ttk.Label(self.input_frame, text=get_string("label_participants_num"))
        self.label_participants_num.grid(row=3, column=0, sticky=tk.W, pady=2)
        self.num_partecipanti_entry = ttk.Entry(self.input_frame, width=10)
        self.num_partecipanti_entry.grid(row=3, column=1, sticky=tk.W, pady=2)
        self.num_partecipanti_entry.insert(0, "1")

        self.label_participants_signs = ttk.Label(self.input_frame, text=get_string("label_participants_signs"))
        self.label_participants_signs.grid(row=4, column=0, sticky=tk.W, pady=2)
        self.segni_partecipanti_entry = ttk.Entry(self.input_frame, width=40)
        self.segni_partecipanti_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=2)

        self.label_signs_example = ttk.Label(self.input_frame, text=get_string("label_signs_example"))
        self.label_signs_example.grid(row=5, column=1, sticky=tk.W, pady=1, padx=5)


        # --- Pulsante Genera ---
        self.generate_button = ttk.Button(self.main_frame, text=get_string("generate_button"), command=self.run_analysis)
        self.generate_button.grid(row=2, column=0, pady=10) # Cambiato row index

        # --- Sezione Output ---
        self.output_frame = ttk.LabelFrame(self.main_frame, text=get_string("output_frame"), padding="10")
        self.output_frame.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5) # Cambiato row index
        self.main_frame.rowconfigure(3, weight=1) # Aggiornato row index per espansione

        self.output_text = scrolledtext.ScrolledText(self.output_frame, wrap=tk.WORD, width=80, height=20, state=tk.DISABLED)
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.output_frame.rowconfigure(0, weight=1)
        self.output_frame.columnconfigure(0, weight=1)

        # Configura espansione griglia interna a main_frame
        self.main_frame.columnconfigure(0, weight=1)
        # Aggiorna UI alla lingua corrente inizialmente
        self.update_ui_language(CURRENT_LANG)


    def change_language(self, event=None):
        """Callback per il cambio lingua dal Combobox."""
        selected_display = self.selected_lang.get()
        # Estrae il codice lingua (es. 'en' da "en: English")
        lang_code = selected_display.split(":")[0]
        set_language(lang_code)
        self.update_ui_language(lang_code)

    def update_ui_language(self, lang):
        """Aggiorna tutti i testi della UI alla lingua selezionata."""
        self.root.title(get_string("window_title", lang))
        self.lang_label.config(text=get_string("language_select_label", lang))
        self.input_frame.config(text=get_string("project_data_frame", lang))
        self.label_project_name.config(text=get_string("label_project_name", lang))
        self.label_description.config(text=get_string("label_description", lang))
        self.label_start_date.config(text=get_string("label_start_date", lang))
        self.label_participants_num.config(text=get_string("label_participants_num", lang))
        self.label_participants_signs.config(text=get_string("label_participants_signs", lang))
        self.label_signs_example.config(text=get_string("label_signs_example", lang))
        self.generate_button.config(text=get_string("generate_button", lang))
        self.output_frame.config(text=get_string("output_frame", lang))
        # Aggiorna il combobox per mostrare la lingua selezionata correttamente
        self.lang_combobox.set(f"{lang}: {LANGUAGES[lang]}")


    def run_analysis(self):
        """ Raccoglie i dati, esegue la logica e mostra i risultati. """
        # Ottieni la lingua corrente per messaggi e logica
        current_lang = CURRENT_LANG

        # 1. Raccogli Input
        nome_progetto = self.nome_progetto_entry.get().strip()
        descrizione = self.descrizione_entry.get().strip()
        data_inizio_str = self.data_inizio_entry.get().strip()
        num_partecipanti_str = self.num_partecipanti_entry.get().strip()
        segni_str_input = self.segni_partecipanti_entry.get().strip()

        # 2. Validazione Input usando stringhe localizzate
        if not nome_progetto:
            messagebox.showerror(get_string("error_input_title", current_lang),
                                 get_string("error_project_name_required", current_lang))
            return

        try:
            data_inizio = datetime.strptime(data_inizio_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror(get_string("error_input_title", current_lang),
                                 get_string("error_invalid_date", current_lang))
            return

        try:
            num_partecipanti = int(num_partecipanti_str)
            if num_partecipanti < 0: raise ValueError("Numero partecipanti non può essere negativo")
        except ValueError:
             messagebox.showerror(get_string("error_input_title", current_lang),
                                  get_string("error_invalid_participants_num", current_lang))
             return

        # Validazione Segni Zodiacali (considerando la lingua)
        segni_partecipanti_keys = [] # Lista delle chiavi interne (italiano)
        if segni_str_input:
            potential_sign_names = [s.strip() for s in segni_str_input.split(',')]
            valid_display_names_current_lang = get_valid_sign_display_names(current_lang)
            valid_display_names_lower = [n.lower() for n in valid_display_names_current_lang]

            recognized_internal_keys = []
            unrecognized_display_names = []

            for name in potential_sign_names:
                if name.lower() in valid_display_names_lower:
                     # Converte dal nome visualizzato (in lingua corrente) alla chiave interna
                     internal_key = get_internal_sign_key(name, current_lang)
                     if internal_key != "Sconosciuto":
                         recognized_internal_keys.append(internal_key)
                     else: # Should not happen if logic is correct, but as fallback
                         unrecognized_display_names.append(name)
                elif name: # Ignora stringhe vuote risultanti da virgole multiple
                     unrecognized_display_names.append(name)

            segni_partecipanti_keys = recognized_internal_keys

            if unrecognized_display_names:
                 messagebox.showwarning(get_string("warning_signs_title", current_lang),
                                        get_string("warning_unrecognized_signs", current_lang,
                                                   ', '.join(unrecognized_display_names)))

            if len(segni_partecipanti_keys) != num_partecipanti and num_partecipanti > 0:
                 messagebox.showinfo(get_string("info_participants_title", current_lang),
                                     get_string("info_participants_mismatch", current_lang,
                                                num_partecipanti, len(segni_partecipanti_keys)))


        # 3. Prepara dati per la logica
        dati_progetto = {
            'nome': nome_progetto,
            'descrizione': descrizione,
            'data_inizio': data_inizio,
            'num_partecipanti': num_partecipanti, # Usa il numero inserito
            # Passa le chiavi interne (italiano) alla logica
            'segni_partecipanti_keys': segni_partecipanti_keys
        }

        # 4. Esegui Logica e Ottieni Report
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert('end', get_string("generating_message_astro", current_lang))
        self.output_text.insert('end', get_string("generating_message_shuffle", current_lang))
        self.output_text.insert('end', get_string("generating_message_draw", current_lang))
        self.root.update_idletasks() # Forza l'aggiornamento della UI per mostrare i messaggi

        try:
            # Passa la lingua selezionata alla funzione logica
            report = genera_report_proiezione(dati_progetto, current_lang)
        except Exception as e:
            messagebox.showerror(get_string("error_processing_title", current_lang),
                                 get_string("error_processing_message", current_lang, e))
            report = get_string("error_processing_fallback", current_lang)

        # 5. Mostra Risultato
        # L'output text era già stato abilitato e pulito prima dell'elaborazione
        self.output_text.insert(tk.END, "\n---\n" + report) # Aggiunge il report dopo i messaggi "generazione"
        self.output_text.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = TarotAstroApp(root)
    root.mainloop()