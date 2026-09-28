#Expanse anaylezer
import numpy as np

expenses = np.array([
    500, 1200, 300, 800, 1500,
    450, 700, 250, 900, 600
])

print("Expenses:", expenses)
print("Total Expense:", np.sum(expenses))
print("Average Expense:", np.mean(expenses))
print("Highest Expense:", np.max(expenses))
print("Lowest Expense:", np.min(expenses))

large_expenses = expenses[expenses > 800]

print("Expenses above 800:", large_expenses)