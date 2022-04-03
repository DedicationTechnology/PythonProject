import functools

"""
    decorator:
        advantage: Adding new features without modifying legacy features.
        disadvantage: The decorator will modify the name of the original function
        Solutions: use @functools.wraps() decorator
        Using "@function decorator name" to decorate the original function is equivalent to creating a variable
            with the same name as the original function and associating it with the embedded function; therefore,
            the embedded function is executed when the original function is executed and the original function is executed in the embedded function.
"""


def new(parameter):
    # @functools.wraps(parameter)  # Return the name of the original function
    def wrapper():
        print("new feature")
        parameter()  # Execute legacy functions

    return wrapper


"""
    @Function Name A
        def Function Name B():
            first. B()
            second. B(A)
            third. A = B(A)
"""


@new  # Equivalent to 'old = new(old)', Pass old as a parameter to new()
def old():
    print("legacy feature")


"""
    If there is no decorator @, old() indicates a request to the old function. Add a decorator @,
        old indicates the return value of new function(Here it means wrapper), old() indicates the function of return value
        (here it means wrapper())
"""

old()  # >> new feature \n legacy feature
# disadvantage: The decorator will modify the name of the original function
print(old.__name__)  # >> wrapper
# use @functools.wraps decorator return the name of original function
# print(old.__name__)  # >> old