
def demander_age():
    age_int = 0
    while age_int == 0:
        age_str = input("Quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    return age_int

# demander le nom 
nom = ""
while nom == "":
    nom = input("Quel est votre nom ? ")

 # demander l'age
age = demander_age()

# afficher le resultat
print(f"Bonjour {nom}, tu as {age} ans")
print(f"Tu auras {age + 1} ans dans un an")



