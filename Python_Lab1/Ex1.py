# Exercise 1: Integer Input and Operations
while 1:
    try:
        a = int(input("Enter the first integer: "))
        break
    except: continue
while 1:
    try:
        b = int(input("Enter the second integer: "))
        break
    except: continue

print("Sum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)


