per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада:"))
deposit = []
deposit.append(money / 100 * 5.6)
deposit.append(money / 100 * 5.9)
deposit.append(money / 100 * 4.28)
deposit.append(money / 100 * 4.0)
print(deposit)
print("Максимальная сумма, которую можно заработать:", max(deposit))


