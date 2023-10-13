import numpy
from matrix import mat_mult_dnc, mat_mult_naive, mat_mult_strassen

def main():
    # type: ignore
    print(mat_mult_naive(numpy.matrix([[1, 2], [3, 4]]), numpy.matrix([[1, 2], [3, 4]])))
    print(mat_mult_dnc(numpy.matrix([[1, 2], [3, 4]]), numpy.matrix([[1, 2], [3, 4]])))
    print(mat_mult_strassen(numpy.matrix([[1, 2], [3, 4]]), numpy.matrix([[1, 2], [3, 4]])))


if __name__ == f'__main__':
    main()
