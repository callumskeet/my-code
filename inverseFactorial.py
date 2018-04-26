#! python3
# inverseFactorial.py - performs the inverse of the factorial function


def inverseFactorial(product):
    if product == 1:
        print('1 = 1!')
        return True
    elif product < 1:
        print('Impossible')
        return True
    x = product
    i = 1
    while x != 1.0:
        if x % i >= 1:
            print(str(product) + '  NONE')
            break
        x = x // i  # floor division ensures the number is stored at full precision
        i += 1
        if x == 1.0:
            print(str(product) + ' = ' + str(i - 1) + '!')


if __name__ == "__main__":
    print('Examples:')
    inverseFactorial(3628800)
    inverseFactorial(479001600)
    inverseFactorial(6)
    inverseFactorial(18)
    print()
    while True:
        number = input()
        if number == '':
            break
        inverseFactorial(int(number))
