# Ask user for name

name = raw_input("what is your name ?:")



# Ask user for age

age = raw_input("how old are you?:")



# Ask user for city

city = raw_input("what city are you from?:")

# Ask user what they enjoy

enjoy = raw_input("what do you enjoy on your time off?:")

# Create output text
string = " your name is{} and your are{} years old. you live in{} and you enjoy{}"
output = string.format(name,age,city,enjoy)
# Print output to the screen
print(output)



