# afficher les informations de la personne

def info_personne(nom, age):    
    print(f"Bonjour {nom}, tu as {age} ans")
    print(f"Tu auras {age + 1} ans dans un an")

    # verifier si la personne est majeur
    condition_majeur = age >= 18
    if condition_majeur:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")   

    if age == 17:
        print("Vous êtes presque majeur")
    elif age == 18:
        print("Bravo vous êtes majeur")
    elif age >= 18:
        print("Vous êtes un jeune")
    else:
        print("Vous êtes un mineur")

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



