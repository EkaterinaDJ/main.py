tickets = int(input("Количество билетов: "))
price = 0
N = 1
while N <= tickets:
    age = int(input(f"Возраст посетителя для билета № {N}: "))
    if age < 18:
        print("Стоимость билета: 0 руб.")
        N += 1
    elif 18 <= age < 25:
        price += 990
        print("Стоимость билета: 990 руб.")
        N += 1
    else:
        price += 1390
        print("Стоимость билета: 1390 руб.")
        N += 1

if tickets >= 3:
 discount = price - ((price / 100) * 10)
 print(f'К оплате с учетом скидки: {discount}) ')
else:
 print("Сумма к оплате: ", price, "рублей")

