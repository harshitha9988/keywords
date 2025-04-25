def calculate_due_amount(**kwargs):
    total_bill = kwargs.get('total_bill', 0)
    amount_paid = kwargs.get('amount_paid', 0)

    due_amount = total_bill - amount_paid
    return due_amount

if __name__ == "__main__":
    total_bill = float(input("Enter the total bill amount: $"))
    amount_paid = float(input("Enter the amount paid: $"))

    due_amount = calculate_due_amount(total_bill=total_bill, amount_paid=amount_paid)

    if due_amount > 0:
        print(f"The remaining due amount is: ${due_amount:.2f}")
    elif due_amount == 0:
        print("The bill has been fully paid. No due amount.")
    else:
        print(f"The customer has overpaid by: ${-due_amount:.2f}")
