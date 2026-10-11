pet = "dog"
age = 1

if pet == "dog" and age < 1:
    print("Puppy food")
elif pet == "dog":
    print("Adult dog food")
elif pet == "cat" and age < 1:
    print("Kitten food")
elif pet == "cat":
    print("Adult cat food")
else:
    print("Unknown pet")