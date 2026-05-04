"""
User Settings Manager
Un utilitar pentru gestionarea setărilor de sistem folosind dicționare în Python.
"""

def add_setting(settings, key_value_tuple):
    key = str(key_value_tuple[0]).lower()
    value = str(key_value_tuple[1]).lower()

    if key in settings:
        return f"❌ Eroare: Setarea '{key}' există deja!"
    
    settings[key] = value
    return f"✅ Setarea '{key}' a fost adăugată cu succes."

def update_setting(settings, key_value_tuple):
    key = str(key_value_tuple[0]).lower()
    value = str(key_value_tuple[1]).lower()

    if key in settings:
        settings[key] = value
        return f"🔄 Setarea '{key}' a fost actualizată la '{value}'."
    
    return f"❌ Eroare: Setarea '{key}' nu există!"

def delete_setting(settings, key):
    key = str(key).lower()
    if key in settings:
        del settings[key]
        return f"🗑️ Setarea '{key}' a fost ștearsă."
    return "❌ Eroare: Setarea nu a fost găsită."

def view_settings(settings):
    if not settings:
        return "\nℹ️ Nu există setări disponibile."
    
    output = "\n--- Setări Utilizator Curente ---\n"
    for key, value in settings.items():
        output += f"🔹 {key.capitalize()}: {value}\n"
    return output

# --- Exemplu de rulare ---
if __name__ == "__main__":
    my_settings = {'theme': 'dark', 'language': 'romanian'}
    
    print(view_settings(my_settings))
    print(add_setting(my_settings, ('Volume', 'High')))
    print(update_setting(my_settings, ('Language', 'English')))
    print(view_settings(my_settings))