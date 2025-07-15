montant_HT = float(input("Montant HT : "))
taux_TVA = float(input("Taux de TVA (%) : "))

montant_TTC = montant_HT * (1 + taux_TVA / 100)

print(f"Montant TTC : {montant_TTC:.2f} €")
