import json
import shutil
import os

def load_config(filename):
    try:
        with open(filename, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print(f"Le fichier de configuration '{filename}' n'existe pas.")
        return None
    except IOError as e:
        print(f"Erreur lors de la lecture du fichier '{filename}': {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Erreur de décodage JSON dans '{filename}': {e}")
        return None

def backup_files(config):
    if config is None:
        return

    for item in config.get('backup_items', []):
        path = item.get('path', '')
        if os.path.exists(path):
            if os.path.isfile(path):
                # un fichier, copier vers le dossier de sauvegarde
                try:
                    shutil.copy(path, 'C:\\Log')
                    print(f"Fichier '{path}' sauvegardé avec succès.")
                except IOError as e:
                    print(f"Erreur lors de la sauvegarde du fichier '{path}': {e}")
            elif os.path.isdir(path):
                # répertoire, copier récursivement vers le dossier de sauvegarde
                try:
                    shutil.copytree(path, 'C:\\Log')
                    print(f"Répertoire '{path}' sauvegardé avec succès.")
                except IOError as e:
                    print(f"Erreur lors de la sauvegarde du répertoire '{path}': {e}")
            else:
                print(f"Le chemin '{path}' n'est ni un fichier ni un répertoire valide.")
        else:
            print(f"Le chemin '{path}' n'existe pas.")

def main():
    config_file = 'c:/Users/eliot/Documents/Cours/B3/Python/PythonCours/Ws5/'
    config = load_config(config_file)
    backup_files(config)

if __name__ == "__main__":
    main()
