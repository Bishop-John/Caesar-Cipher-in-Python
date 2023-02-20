alphabet = 'abcdefghijklmnopqrstuvwxyz'

message = input("Enter a message to encrypt: ").lower()
key = int(input("What number would you like for your key value?"))
cipherText = ""
for i in range(len(message)):
    if message[i] in alphabet:
        newPosition = (alphabet.find(message[i]) + key) % 26
        cipherText = cipherText + alphabet[newPosition]
    else:
        cipherText = cipherText + message[i]

print("The encrypted message is", cipherText)

