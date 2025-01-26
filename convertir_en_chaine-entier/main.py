nom = "wid"
age = 25
age_prochain = age + 1

# Convertir l'entier en chaines de caractères
# str() permet de convertir une valeur en chaine de caractères
# str(25) => "25"
print(f"vous vous appelez {nom} vous avez {age} ans.")
print("vous vous appelez " + nom + "vous avez " + str(age) + "ans.")

# Convertir la chaine de caractères en entier
# age = int(input("Bonjour, quel est votre âge ? "))
print("vous vous appelez " + nom + " tu auras " + str(age_prochain) + " ans. v1")
print(f"vous vous appelez {nom} tu auras {age_prochain} ans. v2")


print(type(nom))
print(type(age))
print(type(age_prochain))