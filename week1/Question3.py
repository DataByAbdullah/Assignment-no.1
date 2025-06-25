# Compound Interest Calculator

P = float(input("Enter the principal amount: "))
R = float(input("Enter the annual interest rate (in %): "))
T = float(input("Enter the time in years: "))

compound_interest = P * (1 + R / 100) ** T - P

print(f"The compound interest is: {compound_interest}")