import json
from datetime import datetime

# Lire le fichier .Scala
with open("Test.Scala", "r", encoding="utf-8") as fichier:
    contenu_Scala = fichier.read()

# Encoder le contenu : guillemets et sauts de ligne
contenu_encode = contenu_Scala.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

# Créer le document JSON final
document = {
    "nom_test": "Test de charge API locale",
    "outil": "Gatling",
    "type": "charge",
    "prompt_utilise": "Génère un script Gatling en Scala pour faire un test de charge afin de simuler 70 utilisateurs progressifs pendant 1 minute, en envoyant une requête POST à l’URL http://localhost:3000/api/test avec un corps JSON {\"message\": \"Bonjour\" } et un en-tête Content-Type: application/json.",
    "date_creation": datetime.utcnow().isoformat() + "Z",
    "valide": False,
    "script_Scala": contenu_encode
}

# Enregistrer dans un nouveau fichier JSON
with open("document_Gatling.json", "w", encoding="utf-8") as sortie:
    json.dump(document, sortie, indent=2)
