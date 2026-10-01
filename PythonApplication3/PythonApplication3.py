'''
Ross Young
9/30/2026
This is a ceaser cipher program that encrypts messages by offsetting letters by a specified number of positions in the alphabet.
'''

with open("Quotefile.txt", "r") as file: # Getting the file to encrypt
    quote = file.read()
while True: # Loop to get the shift value from the user
    try:
        offset = int(input("Enter an offset between 1 and 20:")) # Getting the offset value from the user
        if 1 <= offset <= 20: # Checking if given value is in range
            break
        else:
            print("Input is out of range. Please enter a number between 1 and 20.") # Warning if the value is out of range
    except ValueError:
        print("Invalid input. Please enter a whole number.") # Warning if the value is anything but a whole number

message = "" # Creating an empty string to store the encrypted message
for i, ch in enumerate(quote):
    if ch.isalpha(): # Checking if the character is a letter
        base = ord('a') if ch.islower() else ord('A') # Getting the base value for lowercase or uppercase letters
        basenumber = ord(ch) - base # Converting the letter to a number between 0 and 25
        totalshift = offset + (i % 3) # Adding progressive offset by 0, 1, 2...
        offsetch = chr((basenumber + totalshift) % 26 + base) # Converting the offset number back to letters
        message += offsetch # Adding the encrypted character to the message
    else:
        message += ch # If the character is not a letter, it is added to the message without any changes

with open("EncryptedFile.txt", "w") as file: # Writing the encrypted message to a new file
    file.write(message)
print("The encrypted message has been saved to EncryptedFile.txt") # Confirming the message has been saved