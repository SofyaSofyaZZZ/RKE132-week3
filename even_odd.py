n = int(input("Sisesta täisarv: "))

match n:
    case 0:
        print("Arv on null")
    case _ if n > 0:
        print("Arv on positiivne")
    case _:
        print("Arv on negatiivne")
