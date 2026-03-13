def make_change_naira(amountCharged, amountGiven):
        change = amountGiven - amountCharged

        denominations = {
                '1000 Naira bill': 1000,
                '500 Naira bill': 500,
                '200 Naira bill': 200,
                '100 Naira bill': 100,
                '50 Naira bill': 50,
                '20 Naira bill': 20,
                '10 Naira bill':  10,
                '5 Naira bill': 5,
                '1 Naira bill': 1
        }

        change_to_give = {}

        for denomination, value in denominations.items():
                if change >= value:
                        print(change, value)
                        num_of_denomination = change // value
                        change_to_give[denomination] = num_of_denomination
                        change -= num_of_denomination * value
                print(value)

        return change_to_give
                        



amount_charge = float(input('Enter amount to be charged: '))
amount_given = float(input('Enter the amount given: '))

change = make_change_naira(amount_charge, amount_given)

if isinstance(change, dict):
        print('Change to give back:') 
        for denomination, count in change.items():
                print(f"{count} x {denomination}")
else:
        print(change)