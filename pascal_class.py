#! python3
from fractions import Fraction


class pascal:

    def __init__(self, row_num):
        self.row_num = row_num

    def row(self):
        ''' Returns a list of numbers in row n of Pascal's Triangle '''
        row_numerator = [self.row_num + 1 - i
                         for i in range(1, self.row_num)]
        row_fractions = [Fraction(row_numerator[i - 1], i)
                         for i in range(1, self.row_num)]
        row_list = [row_fractions[0], ]
        for i in range(1, len(row_fractions)):
            row_list += [row_list[i - 1] * row_fractions[i]]
        row_list = [int(i) for i in row_list]
        return row_list

    def aks_test(self):
        ''' Performs the AKS Test to determine if a number is prime '''
        for coeffiecient in self.row():
            if coeffiecient % self.row_num != 0:
                return False
        return True


if __name__ == "__main__":
    x = pascal(19)
    print(x.row())
    print(x.aks_test())
