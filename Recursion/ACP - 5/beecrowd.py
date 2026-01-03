# Beecrowd 1050
ddd_destination = {
    61 : "Brasilia",
    71 : "Salvador",
    11 : "Sao Paulo",
    21 : "Rio de Janeiro",
    32 : "Juiz de Fora",
    19 : "Campinas",
    27 : "Vitoria",
    31 : "Belo Horizonte"
}

ddd = int(input())
if ddd in ddd_destination:
    print(ddd_destination[ddd])
else:
    print("DDD nao cadastrado")


#Beecrowd 1051
salary = float(input())

if 0 <= salary <= 2000.00:
    print("Isento")
else:
    tax = 0
    if salary > 2000.00:
        amount_to_tax = min(salary, 3000.00) - 2000.00
        tax += amount_to_tax * 0.08
    if salary > 3000.00:
        amount_to_tax = min(salary, 4500.00) - 3000.00
        tax += amount_to_tax * 0.18
    if salary > 4500.00:
        amount_to_tax = salary - 4500.00
        tax += amount_to_tax * 0.28

    print(f"R$ {tax:.2f}")