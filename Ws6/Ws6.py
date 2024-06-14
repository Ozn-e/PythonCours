import json
import shutil
import os

def loadconfig(filename):
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

def backupfiles(config):
    if config is None:
        return

    for item in config.get('backupitems', []):
        path = item.get('path', '')
        if os.path.exists(path):
            if os.path.isfile(path):
                # C'est un fichier, copier vers le dossier de sauvegarde
                try:
                    shutil.copy(path, '/chemin/vers/le/dossier/de/sauvegarde')
                    print(f"Fichier '{path}' sauvegardé avec succès.")
                except IOError as e:
                    print(f"Erreur lors de la sauvegarde du fichier '{path}': {e}")
            elif os.path.isdir(path):
                # C'est un répertoire, copier récursivement vers le dossier de sauvegarde
                try:
                    shutil.copytree(path, '/chemin/vers/le/dossier/de/sauvegarde')
                    print(f"Répertoire '{path}' sauvegardé avec succès.")
                except IOError as e:
                    print(f"Erreur lors de la sauvegarde du répertoire '{path}': {e}")
            else:
                print(f"Le chemin '{path}' n'est ni un fichier ni un répertoire valide.")
        else:
            print(f"Le chemin '{path}' n'existe pas.")

def main():
    configfile = 'config.json'
    config = loadconfig(configfile)
    backupfiles(config)

if __name__ == "__main":
    main()