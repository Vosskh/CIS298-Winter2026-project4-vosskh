import sys
from xmlrpc.client import MAXINT

def get_taxes_at_bracket(start_of_bracket, end_of_bracket, rate, adjusted_gross_income):
    if adjusted_gross_income < start_of_bracket:
        return 0
    if adjusted_gross_income > end_of_bracket:
        return ( end_of_bracket - start_of_bracket) * rate
    return ( adjusted_gross_income - start_of_bracket ) * rate

def get_totals(prompt):
    total = 0
    more = 'y'
    while more == 'y':
        try:
            total += int(input(prompt))
        except ValueError:
            print("invalid number")
        more = input("Do you have more to enter? (y/n)")
    return total

total_deductions = get_totals("Enter a deduction")

if total_deductions < 15750:
    total_deductions = 15750

gross_income = get_totals("Enter an income")

adjusted_gross_income = gross_income - total_deductions

if adjusted_gross_income < 0:
    adjusted_gross_income = 0

start_of_brackets = [
    0, 11_925, 48_475, 103_350, 197_300, 250_525, 626_350
]

end_of_brackets = [
    # bing - python max int
    11_925, 48_475, 103_350, 197_300, 250_525, 626_350, sys.maxsize
]

bracket_rates = [
    .1, .12, .22, .24, .32, .35, .37
]

money_owed_at_brackets = []
for index in range(len(bracket_rates)):
    money_owed_at_brackets.append(
        get_taxes_at_bracket(start_of_brackets[index],
                             end_of_brackets[index],
                             bracket_rates[index],
                             adjusted_gross_income))

for index in range(len(bracket_rates)):
    print(f'Taxes owed at {bracket_rates[index]*100}%:'
          f' ${money_owed_at_brackets[index]:,.2f}')

total_taxes = sum(money_owed_at_brackets)
print(f'Total Taxes owed: ${total_taxes:,}')
print(f'Taxes owed as % of gross income {total_taxes/gross_income*100:.2f}%')
print(f'Taxes owed as % of adjusted gross income {total_taxes/adjusted_gross_income*100:.2f}%')