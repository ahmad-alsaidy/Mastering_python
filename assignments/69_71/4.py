def my_all(iterable):

    status = True

    for i in iterable:
        if bool(i) == False:
            status = False

    return status


# my_all
print(my_all([1, 2, 3]))  # True
print(my_all([1, 2, 3, []]))  # False

print('=' * 30)


def my_any(iterable):
    status = False

    for i in iterable:
        if bool(i) == True:
            status = True

    return status


# my_any
print(my_any([0, 1, [], False]))  # True
print(my_any([(), 0, False]))  # False

print('=' * 30)


def my_min(iterable):
    minimum = iterable[0]

    for i in iterable:
        if i < minimum:
            minimum = i

    return minimum


# my_min
print(my_min([10, 100, -20, -100, 50]))  # -100
print(my_min((10, 100, -20, -100, 50)))  # -100

print('=' * 30)


def my_max(iterable):
    maximum = iterable[0]

    for i in iterable:
        if i > maximum:
            maximum = i

    return maximum


# my_max
print(my_max([10, 100, -20, -100, 50, 700]))  # 700
print(my_max((10, 100, -20, -100, 50, 700)))  # 700
