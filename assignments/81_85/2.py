# Create Your Decorator Here
def add_hash(func):
    def nested_func():
        print("Sugar Added From Decorators")
        func()
        print("####################")
    return nested_func


@add_hash
def make_tea():
    print("Tea Created")


@add_hash
def make_coffe():
    print("Coffe Created")


make_tea()
make_coffe()

# Needed Output

# "Sugar Added From Decorators"
# "Tea Created"
# "####################"
# "Sugar Added From Decorators"
# "Coffe Created"
# "####################"
