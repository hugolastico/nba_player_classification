import requests
import json

# URL de l'API Flask
url = "http://127.0.0.1:5000/predict"

def main():
    
    try:
        # Demander les entrées à l'utilisateur
        gp = int(input("Games Played : "))
        min_ = float(input("Minutes Played : "))
        pts = float(input("Points Per Game : "))
        reb = float(input("Rebounds : "))
        ast = float(input("Assists : "))
        stl = float(input("Steals : "))
        blk = float(input("Blocks : "))
        
        # Créer les données au format JSON
        data = {
            "GP": gp,
            "PTS/MIN": pts/min_,
            'REB': reb, 
            'AST': ast, 
            'STL': stl, 
            'BLK': blk
        }
        
        # Envoyer une requête POST
        response = requests.post(url, json=data)
        
        # Afficher la réponse
        if response.status_code == 200:
            print("\nRésultat de la prédiction :", response.json())
        else:
            print("\nErreur :", response.status_code, response.text)
    
    except ValueError:
        print("Erreur : Veuillez entrer des valeurs valides.")
    except requests.exceptions.RequestException as e:
        print("Erreur de connexion à l'API :", e)

if __name__ == "__main__":
    main()
