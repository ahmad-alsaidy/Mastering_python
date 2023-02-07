name = 'Elzero'

# Needed Output
# "lze"
# "Ezr"
# "rzE"

print('"{}"'.format(name[1:4]))  # "lze"
print('"{}"'.format(name[0:5:2]))  # "Ezr"

print('"{}"'.format(name[0:5:2][::-1]))  # "rzE"
print('"{}"'.format(name[-2:-7:-2]))  # "rzE"
