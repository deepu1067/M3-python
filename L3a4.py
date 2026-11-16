def calculate_due(total_amount, paid_amount):
    due = total_amount - paid_amount
    return due


# Function call with arguments
total = 5000
paid = 3000

result = calculate_due(total, paid)

print("Total Amount:", total)
print("Paid Amount:", paid)
print("Due Amount:", result)