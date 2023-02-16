''''This is a module for assignment_5'''

myFriends = ["Ahmed", "Osama", "Sayed"]


def say_hello(some_poeple: list) -> None:
    '''This function each element of a list of poeple'''
    for someone in some_poeple:
        print(f"Hello {someone}")


say_hello(myFriends)
