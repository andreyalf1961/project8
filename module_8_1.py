def add_everything_up(a, b):
    try:
        return round(a + b, 3)
    except:
        return str(a) + str(b)


print(add_everything_up(123.456, 'string'))
print(add_everything_up('apple', 42.15))
print(add_everything_up(123.456, 7))
