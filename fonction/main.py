def demander_age():
    age_int = 0
    while age_int == 0:
        age_str = input("Quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    return age_int


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
print(f"Bonjour {nom}, tu as {age} ans")
print(f"Tu auras {age + 1} ans dans un an")



