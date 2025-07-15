# Saisie des informations
nom = input("Nom du produit : ")
prix = float(input("Prix (en €) : "))
stock = int(input("Stock disponible : "))
remise = float(input("Remise en % : "))

# Calcul du prix final
prix_final = prix * (1 - remise / 100)

# Affichage
print("\n--- Fiche Produit ---")
print(f"Nom : {nom}")
print(f"Prix initial : {prix} €")
print(f"Remise : {remise} %")
print(f"Prix final : {prix_final:.2f} €")
print(f"Stock : {stock}")

