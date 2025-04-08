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
    elif 12 <= age <= 18:
        print("Vous êtes un adolescent")
    elif age == 1 or age == 2:
        print("Vous êtes un bébé")
    elif age == 18:
        print("Bravo vous êtes majeur")
    elif age < 10:
        print("Vous êtes un enfant")
    elif age > 60:
        print("Vous êtes un sénior")
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
    while reponse_nom == "" or reponse_nom.isdigit():
        reponse_nom = input("Quel est votre nom ? ")
        if reponse_nom.isdigit():
            print("Le nom ne peut pas être un nombre. Veuillez réessayer.")
    return reponse_nom

# demander le nom 
nom = demander_nom()
 # demander l'age
age = demander_age()

# afficher le resultat
info_personne(nom, age)



