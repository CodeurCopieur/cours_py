# boucle while : tant que la condition est vraie, on exécute le bloc d'instructions

# Exemple 1
i = 0 
while i < 5:
    print(f"la valeur de i est {i}")
    i += 1

# Exemple 2

mdp = ""
while mdp != "mdp":
    mdp = input("Entrez votre mot de passe: ")
print("Mot de passe correct")