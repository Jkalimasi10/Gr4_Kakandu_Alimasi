note1 = float(input("Note 1 sur 20 : "))
note2 = float(input("Note 2 sur 20 : "))
note3 = float(input("Note 3 sur 20 : "))

moyenne = (note1 + note2 + note3) / 3

print(f"Moyenne : {moyenne:.2f}")
if moyenne >= 10:
    print("Étudiant reçu.")
else:
    print("Étudiant non reçu.")
