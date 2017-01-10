#! python3
# fibonacci.py - prints Fibonacci sequence 'n' times

while True:
    print('Input sequence length:')
    sequence_no = int(input())

    F = [0, 1]
    n = 1
    while n < sequence_no:
        F = F + [F[n] + F[n - 1]]
        n += 1

    print(str(F).strip('[]') + '\n')
