ddd_to_destination = {
	61 : "Brasilia",
	71 : "Salvador",
	11 : "Sao Paulo",
	21 : "Rio de Janeiro",
	32 : "Juiz de Fora",
	19 : "Campinas",
	27 : "Vitoria",
	31 : "Belo Horizonte"
}

ddd = int(input(""))

if ddd in ddd_to_destination:
	print(ddd_to_destination[ddd])
else:
	print("DDD nao cadastrado")