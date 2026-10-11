def greet():
    name = "Sam"
    print(name)

greet()


# Global Scope
x = "Global variable"

def outer():
    # Enclosing Scope
    y = "Enclosing variable"

    def inner():
        # Local Scope
        z = "Local variable"

        print(z)       # Local
        print(y)       # Enclosing
        print(x)       # Global
        print(len("Python"))  # Built-in

    inner()

outer()