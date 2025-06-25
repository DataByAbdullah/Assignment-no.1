# Calculate Profit or Loss:

cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"\nProfit of: {profit}")
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print(f"\nLoss of: {loss}")
else:
    print("\nNo Profit No Loss")
