from forex_python.converter import CurrencyRates

def afficher_devises_disponibles():
    c = CurrencyRates()
    devises = c.get_rates('EUR')
    print("Devises disponibles :")
    for devise in devises:
        print(devise)

def convertir_devises(historique, devises_preferees):
    continuer = True
    while continuer:
        montant = float(input("Entrez le montant à convertir : "))
        
        afficher_devises_disponibles()

        devise_source = input("Entrez la devise source : ").upper()
        devise_cible = input("Entrez la devise cible : ").upper()
        
        if devise_source in devises_preferees and devise_cible in devises_preferees:
            taux_conversion_source = devises_preferees[devise_source]
            taux_conversion_cible = devises_preferees[devise_cible]
            
            try:
                resultat = montant * (1 / taux_conversion_source) * taux_conversion_cible
                print(f"{montant} {devise_source} équivaut à {resultat} {devise_cible}")
                historique.append(f"{montant} {devise_source} = {resultat} {devise_cible}")
            except ValueError as e:
                print("La conversion est impossible pour ces devises.")
                print(e)
        else:
            c = CurrencyRates()
            try:
                resultat = c.convert(devise_source, devise_cible, montant)
                print(f"{montant} {devise_source} équivaut à {resultat} {devise_cible}")
                historique.append(f"{montant} {devise_source} = {resultat} {devise_cible}")
            except ValueError as e:
                print("La conversion est impossible pour ces devises.")
                print(e)
        
        action = input("Voulez-vous voir l'historique des conversions ? (O/N) : ").upper()
        if action == 'O':
            afficher_historique(historique)
        
        choix = input("Voulez-vous continuer ? (O/N) : ").upper()
        if choix != 'O':
            continuer = False

def afficher_historique(historique):
    if historique:
        print("Historique des conversions :")
        for i, conversion in enumerate(historique, 1):
            print(f"{i}. {conversion}")
    else:
        print("Historique vide")

def ajouter_devise_preferee(devises_preferees):
    devise = input("Entrez le code de la devise à ajouter aux devises préférées : ").upper()
    devises_preferees[devise] = None  
    print(f"{devise} a été ajouté aux devises préférées.")

def creer_devise(devises_preferees):
    devise = input("Entrez le code de la devise à créer : ").upper()
    taux_conversion = float(input(f"Entrez le taux de conversion pour 1 {devise} : "))
    devises_preferees[devise] = taux_conversion
    print(f"{devise} a été créé.")

def afficher_devises_preferees(devises_preferees):
    print("Vos sources préférées :")
    for devise in devises_preferees:
        print(f"- {devise}")

if __name__ == "__main__":
    historique = []
    devises_preferees = {}  
    
    while True:
        choix = input("Que souhaitez-vous faire ? (C pour convertir, A pour ajouter une devise préférée, D pour créer une devise, Q pour quitter) : ").upper()
        
        if choix == 'C':
            convertir_devises(historique, devises_preferees)
        elif choix == 'A':
            ajouter_devise_preferee(devises_preferees)
        elif choix == 'D':
            creer_devise(devises_preferees)
        elif choix == 'Q':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
        
        afficher_devises_preferees(devises_preferees)
