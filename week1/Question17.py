# Convert minutes to hours and minutes

minutes = int(input("Enter number of minutes: "))


hours = minutes // 60
remaining_minutes = minutes % 60

print(f"{minutes} minutes = {hours} hours {remaining_minutes} minutes")
