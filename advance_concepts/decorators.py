"function which takes another function and extends it without modifying it"
# Define the decorator function
def my_decorator(func):
    # Define the wrapper function
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper

# Apply the decorator using the @ syntax
@my_decorator
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()
