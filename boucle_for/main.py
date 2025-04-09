def info_personne(nom, age, taille=0):    
    print(f"Bonjour {nom}, tu as {age} ans")
    print(f"Tu auras {age + 1} ans dans un an")

    if not taille == 0:
        print(f"votre taile est de {taille}m")


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
NB_PERSONNES = 1


# la boucle for
for i in range (0, NB_PERSONNES):
    nom = "Inconnu " + str(i + 1)
    age = demander_age(nom)
    info_personne(nom, age, 1.80)
    