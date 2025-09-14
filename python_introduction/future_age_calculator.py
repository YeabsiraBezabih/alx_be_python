# Future age calculator
current_year = 2023
future_year = 2050
years_to_add = future_year - current_year

# Get user input for current age
try:
    current_age = int(input("How old are you? "))

    # Calculate age in 2050
    age_in_2050 = current_age + years_to_add

    # Print the result
    print(f"In 2050, you will be {age_in_2050} years old.")

except ValueError:
    print("Please enter a valid integer for your age.")
