import json
from datetime import datetime

# Lire le fichier .jmx
with open("Test.jmx", "r", encoding="utf-8") as fichier:
    contenu_jmx = fichier.read()

# Encoder le contenu : guillemets et sauts de ligne
contenu_encode = contenu_jmx.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

# Créer le document JSON final
document = {
    "nom_test": "Test de charge API locale",
    "outil": "JMeter",
    "type": "charge",
    "prompt_utilise": "Génère un script JMeter au format XML (.jmx) pour faire un test de charge de 70 utilisateurs pendant 1 minute sur l’URL http://localhost:3000/api/test. Utilise la méthode POST et inclue un Header Manager avec Content-Type: application/json. Le corps de la requête doit être { \"message\": \"Bonjour\" }.",
    "date_creation": datetime.utcnow().isoformat() + "Z",
    "valide": False,
    "script_jmx": contenu_encode
}

# Enregistrer dans un nouveau fichier JSON
with open("document_JMeter.json", "w", encoding="utf-8") as sortie:
    json.dump(document, sortie, indent=2)