import numpy as np
import math


# Разложение на простые множители
def get_prime_factors(num):
    _factors = []
    while num % 2 == 0:
        _factors.append(2)
        num = num / 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            _factors.append(i)
            num = num / i
    if num > 2:
        _factors.append(int(num))
    return _factors


# Размерности для reshape
def get_dimensions_for_reshape(_factors, _dimension):
    dimensions = []
    for i in range(len(_factors)):
        if len(dimensions) < _dimension:
            dimensions.append(_factors[i])
        else:
            dimensions[_dimension - 1] *= _factors[i]
    return dimensions


count = int(input('Введите количество элементов массива: '))
factors = get_prime_factors(count)
dimension = int(input(f'Введите размерность массива не больше {len(factors)}: '))

if len(factors) < dimension:
    print(f'\nНевозможно создать из {count} элементов массив размерности {dimension}!')
else:
    arr = np.random.randint(0, 100, count).reshape(get_dimensions_for_reshape(factors, dimension))
    print('\nСгенерированный массив целых чисел (0..100):')
    print(arr, '\n')
    print('Квадратные корни исходного массива:')
    print(np.sqrt(arr), '\n')
    print('Максимальный элемент массива: ' + str(np.max(arr)))
