name = "Lukas"

print("Hello. My name is {}".format(name))

# Ticket-100
def ausgabe(src):
    print(f"Das Ergebniss ist {src}!")



def calculate(num1, num2):
    return num1 + num2

ausgabe(calculate(5, 10))