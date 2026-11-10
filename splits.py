expenses =[]

def add_expense(paid_by, amount, description, split_between):
    expense = {
        "paid_by" : paid_by,
        "amount" : amount,
        "description" : description,
        "split_between" : split_between,
    }

    expenses.append(expense)

add_expense("me", 75, "bowling", ["sam","surya", "siva"])
add_expense("me", 60, "dinner", ["raj", "me", "ana"])
add_expense("ana", 30, "movies", ["ana", "raj"])

#print(expenses)


def calculate_balances(expenses):
    balances = {}                                      # name -> money

    for expense in expenses:                           # each receipt
        share = expense["amount"] / len(expense["split_between"])

        payer = expense["paid_by"]
        balances[payer] = balances.get(payer, 0) + expense["amount"]   # payer gains full amount

        for person in expense["split_between"]:        # everyone splitting
            balances[person] = balances.get(person, 0) - share          # each loses their share

    return balances


#print(calculate_balances(expenses))


def settle_up(balances):
    remaining = balances.copy()
    payments =[]

    while abs(min(remaining.values()))> 0.01:
        creditor = max(remaining, key=remaining.get)
        debtor = min(remaining, key=remaining.get)
        amount = min(remaining[creditor], abs(remaining[debtor]))
        payments.append((debtor, creditor, amount))
        remaining[creditor] = remaining[creditor] - amount
        remaining[debtor] = remaining[debtor] + amount
    return payments

#print(settle_up(calculate_balances(expenses)))


print(settle_up({"A":50, "B":30, "C" : -60, "D": -20}))
