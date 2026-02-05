# Exercise 9 :  Prime factor
# Input loop with control
while True:
    try:
        N = int(input("Enter an integer strictly greater than 2: "))
        if N >2 : break
        
    except: continue
# Loop through all numbers from 2 to N
for i in range(2, N+1):
    # Check if i is a factor of N
    if N % i == 0:
        # Test if i is prime
        for j in range(2, (i // 2) + 1):
            if i % j == 0:
                break  # i is not prime
        else:
            # If loop completes without break, i is prime
            print(i, end=" ")

print()  # newline at the end
