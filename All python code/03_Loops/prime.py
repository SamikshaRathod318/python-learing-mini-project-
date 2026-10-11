num = 7
prime = True

if num < 2:
    prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

if prime:
    print("Prime number")
else:
    print("Not a prime number")