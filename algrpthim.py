
a= int(input("plase add an interger for a, "))
b= int(input("plase add an interger for b, "))
def gcd(a, b):
    if a == 0 :
        return b
    if b == 0:
        return a

    return gcd(b % a, a)
text = str(input("add message to incrypt: "))
hidden_text = ""
key= gcd(a,b)
def encryption(key, text, hidden_text=""):
    for let in text:
        hidden_text = hidden_text + chr(ord(let) + key)
    return hidden_text



print(gcd(a,b))
print(encryption(key,text, hidden_text))

