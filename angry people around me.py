def calculate_power(base, exponent):
    return base ** exponent

# Get input from user
try:
    base = float(input("Enter the base number: "))
    exponent = int(input("Enter the power (exponent): "))
    
    # Calculate and display result
    result = calculate_power(base, exponent)
    print(f"{base} raised to the power of {exponent} is: {result}")
    
except ValueError:
    print("Please enter valid numbers (base can be decimal, exponent must be an integer)")
    
    
    
    
    
    
try:
    age = int(input("Enter your age: "))
    
    if 10 <= age <= 20:
        print("Your age is between 10 and 20 years.")
    else:
        print("Your age is not between 10 and 20 years.")
        
except ValueError:
    print("Please enter a valid integer age.")