def decorator(func):
    def wrapper():
        print("Before starting...")
        func()
        print("After starting...")

    return wrapper

@decorator
@decorator
@decorator
@decorator
@decorator
def testing():
    print("testing...")


testing()

# def decorator(func):
#     if type(func).__name__ == "function":
#         func()
#
# decorator(testing)

# def decorator():
#     def wrapper():
#         print("tesing wrapper function...")
#
#     return wrapper
#
# t = decorator()
# t()


# testing = decorator(testing)
# testing = decorator(testing)
# testing = decorator(testing)
#
# testing()
