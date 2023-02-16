# Write Function With Help To Get The Output
def say_hello_to(name: str) -> str:
    '''
    parameter(someone) => Person Name
    Function To Say Hello To Anyone
    '''
    return f"Hello {name}"


print(say_hello_to("Osama"))  # "Hello Osama"

print(say_hello_to.__doc__)

# Function Doc String Output
# "parameter(someone) => Person Name"
# "Function To Say Hello To Anyone"
