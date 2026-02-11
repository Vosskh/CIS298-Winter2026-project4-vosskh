import csv

current_age = int(input("How old are you"))
retirement_age = int(input("How old do you want to be when you retire?"))

mattress_money = float(input("How much do you have saved under your mattress"))
bank_money = float(input("How much do you have saved in a bank account"))
bonds_money = float(input("How much do you have invested in bonds"))
stocks_money = float(input("How much do you have invested in stocks"))

rate_of_returns_bonds = []
rate_of_returns_stocks = []

with open("BondsAndStocksAnnualReturn.csv") as data:
    lines = data.readlines()
    for index in range(1, len(lines)):
        tokens = lines[index].split(',')
        rate_of_returns_stocks.append(float(tokens[1][:-1])/100)
        rate_of_returns_bonds.append(float(tokens[2].strip()[:-1])/100)

balances = [["Mattress Savings", 'Bank Savings', "Bonds", "Stocks", "Total"]]

for year in range(retirement_age - current_age):
    choice = -1

    while choice != 0:
        choice = int(input(
"""Do you want to:
0 - Go to next year
1 - Add money to mattress savings
2 - Add money to bank savings
3 - Add money to bonds investment
4 - Add money to stocks investment
"""))

        if choice != 0:
            money = float(input("How much money do you want to add?"))
        if choice == 1:
            mattress_money += money
            mattress_money = mattress_money.round(2)
        elif choice == 2:
            bank_money += money
            bank_money = bank_money.round(2)
        elif choice == 3:
            bonds_money += money
            bonds_money = bonds_money.round(2)
        elif choice == 4:
            stocks_money += money
            stocks_money = stocks_money.round(2)

    bank_money *= 1.02
    bonds_money *= ( 1 + rate_of_returns_bonds[year])
    stocks_money *= ( 1 + rate_of_returns_stocks[year])

    balances.append([mattress_money, bank_money, bonds_money, stocks_money])
    balances[-1].append(sum(balances[-1]))

    print(f"Your current balances at age {current_age+year}: ")
    print(f"Mattress: ${mattress_money:,.2f}")
    print(f"Bank: ${bank_money:,.2f}")
    print(f"Bonds: ${bonds_money:,.2f}")
    print(f"Stocks: ${stocks_money:,.2f}")
    print(f'Total Balance ${balances[-1][-1]:,.2f}')


print(f'Your total savings adjusted for inflation is'
      f' ${balances[-1][-1]/(1.02**(retirement_age-current_age)):,.2f}')

# https://github.com/EricCharnesky/CIS298-Winter2026/blob/main/week4-files/main.py
csv_file = open('balances.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerows(balances)
csv_file.close()