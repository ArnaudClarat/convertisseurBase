# --------Fonctions--------
def menu():
	print("""\
	Bienvenur dans le convertisseur de base!
	Ceci est la V1 de ce programme!
	N'hésitez pas à l'ameliorer en n'oubliant pas de commenter votre commit""")

#----Variables Globales----
nbr1 = ""

#-------Main Program-------
menu()
while nbr1 != "Q" :
	nbr1 = input("""
	Quel chiffre voulez-vous convertir? 
	Tapez Q pour quitter
	""").upper()
	if nbr1 != "Q" : 
		base1 = input("	En quelle base est ce chiffre? ")
		base2 = input("	En quelle base voulez-vous le convertir? ")