def gen_factorial(n):
    factorial1 = 1
    el = 1
    while el <= n:
        factorial1 *= el
        el += 1
        yield factorial1

print([f'Факториал {i+1}! = {el}' for i, el in enumerate(gen_factorial(10))]) # Факториал до 10