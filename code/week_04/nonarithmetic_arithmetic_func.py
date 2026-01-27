def plus_one(num):
    """ adds one to the provided argument """
    return num + 1

def add(num1, num2):
    """ adds two numbers together """
    sum = num1
    for num in range(num2):
        sum = plus_one(sum)
    return sum

def multiply(num1, num2):
    """ multiplies two numbers together """
    product = 0
    for num in range(num2):
        product = add(product, num1)
    return product

def exponent(num1, num2):
    """ raises one number to the power of another """
    power = 1
    for num in range(num2):
        power = multiply(power, num1)
    return power

print(exponent(8, 9))