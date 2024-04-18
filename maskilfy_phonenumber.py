def maskify(phone_number):
    masked_number = '#' * (len(phone_number) - 3) + phone_number[-3:]
    return masked_number

# Get user input for mobile number
user_number = input("Enter your mobile number: ")

# Maskify the mobile number
masked_result = maskify(user_number)

# Print the masked number
print("Masked number:", masked_result)
