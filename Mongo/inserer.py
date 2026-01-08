# nom du fichier : inserer.py

import json
from pymongo import MongoClient

# Connexion à MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Accès à la base de données (créée si elle n'existe pas)
db = client["Tests_Performences"]

# --- Insertion du fichier JMeter ---
try:
    with open("document_JMeter.json", "r", encoding="utf-8") as f_jmeter:
        document_jmeter = json.load(f_jmeter)

    collection_jmeter = db["jmeter"]

    if isinstance(document_jmeter, list):
        result = collection_jmeter.insert_many(document_jmeter)
        print(f"{len(result.inserted_ids)} documents JMeter insérés avec succès.")
    else:
        result = collection_jmeter.insert_one(document_jmeter)
        print(f"Document JMeter inséré avec succès. ID : {result.inserted_id}")
except FileNotFoundError:
    print("Le fichier 'document_JMetre.json' est introuvable.")

# --- Insertion du fichier Gatling ---
try:
    with open("document_Gatling.json", "r", encoding="utf-8") as f_gatling:
        document_gatling = json.load(f_gatling)

    collection_gatling = db["gatling"]

    if isinstance(document_gatling, list):
        result = collection_gatling.insert_many(document_gatling)
        print(f"{len(result.inserted_ids)} documents Gatling insérés avec succès.")
    else:
        result = collection_gatling.insert_one(document_gatling)
        print(f"Document Gatling inséré avec succès. ID : {result.inserted_id}")
except FileNotFoundError:
    print(" Le fichier 'document_Gatling.json' est introuvable.")