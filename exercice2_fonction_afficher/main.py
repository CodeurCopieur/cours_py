# afficher les informations de la personne

def info_personne(nom, age):    
    print(f"Bonjour {nom}, tu as {age} ans")
    print(f"Tu auras {age + 1} ans dans un an")


def demander_age():
    reponse_age = 0
    while reponse_age == 0:
        age_str = input("Quel est votre age ? ")
        try:
            reponse_age = int(age_str)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    return reponse_age


def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom

# demander le nom 
nom = demander_nom()
 # demander l'age
age = demander_age()

# afficher le resultat
info_personne(nom, age)



