def info_personne(nom, age):    
    print(f"Bonjour {nom}, tu as {age} ans")
    print(f"Tu auras {age + 1} ans dans un an")


def demander_age(nom):
    reponse_age = 0
    while reponse_age == 0:
        age_str = input(f"{nom} Quel est votre age ? ")
        try:
            reponse_age = int(age_str)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    return reponse_age


# demander le nom 
nb_personnes = 3


# la boucle for
for i in range (0, nb_personnes):
    nom = "Inconnu " + str(i + 1)
    age = demander_age(nom)
    info_personne(nom, age)
    