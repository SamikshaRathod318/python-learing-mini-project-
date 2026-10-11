def numbers():  # A generator returns values one at a time using yield.
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6

for num in numbers():
    print(num)