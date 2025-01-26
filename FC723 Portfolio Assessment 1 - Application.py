
#this class is made to encrypt the message the user types
class Encryption:

    #initilize the methods
    def __init__(self, text):
        self.hidden_text = ""
        self.text = text

    #this function takes the key from the child glass and uses it encrypt the text
    def encrypt(self, key):
        #a for loop that encrypts the message
        for let in self.text:
            self.hidden_text += chr(ord(let) + key)
        return self.hidden_text

#the Euclidean algorithm well get the gcd and outputs it as key
class gcd(Encryption):
    #init method to get user input from outside the class.
    def __init__(self, a, b, text):

        #super__init__ to get text from parent class.
        super().__init__(text)
        #the key is the result of the function gcd(a,b)
        self.key = self.gcd(a, b)  # Calculate the GCD as the encryption key

    #this function gets the greatest common divisor
    def gcd(self, a, b):
        #the if condition is returns thr gcd(b % a, a) if either a or b are zero
        if a == 0:
            return b
        if b == 0:
            return a
        return self.gcd(b % a, a)

#this is where the user put the two numbers for encryption and the text they want to encrypt
a = int(input("Please insert a positive number for a: "))
b = int(input("Please insert a positive number for b: "))
text = input("Insert text to be encrypted: ")

#this gcd is the insentience of a class so we can get output from the class
gcd = gcd(a, b, text)

#encrypted_text is the way to get the encrypted text.
encrypted_text = gcd.encrypt(gcd.key)

#prints out the original text and encrypted text.
print("original text:",text)
print("encrypted_text",encrypted_text)