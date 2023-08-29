def double(arg):
    print('Before', arg)
    arg = arg * 2
    print('After', arg)


def change(arg):
    print('Before', arg)
    arg.append('More Data')
    print('After', arg)
