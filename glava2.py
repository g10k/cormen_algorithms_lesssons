# -*- encoding: utf-8 -*-
__author__ = 'g10k'
"""
Сортировка вставкой.
 - Инвариант цикла - условие, которое выполняется каждую итерацию. Обладают 3 свойствами: инициализация, сохранение и завершение.
Анализ алгоритмов.
 - Для простоты при анализе и сравнении алгоритмов принято использовать RAM модель (random access machine),
    однопроцессорная машина, где команды выполняются последовательно.
 Важные понятия для анализа алгоритмов.
 - размер входных данных (чаще всего размер массива, бывает и по-другому, например, размер двух чисел которые нужно перемножить)
 - время работы. измеряется в количестве элементарных операций,  или "шагов". Исходим из того, что на каждый такой "шаг"
   требуется фиксированное время.
 Анализ алгоритма вставками:
  T(n) = c1n + c2(n-1) + c4(n-1) + c5*sum(tj) + c6*sum(tj-1) + ct*sum(tj-1) + c8(n-1)
    где tj - количество шагов для вставки очередного числа.
  В самом благоприятном случае (когда массив уже отсортирован в обратном порядке)
    c1n + c2(n-1) + c4(n-1) + c3(n-1) + c8(n-1) = a*n+b (где а и b некоторые константы)
  В самом неблагоприятном получится a*n^2 + b*n + c - квадратичная функция

 ПОрядок роста.
 Было допущено несколько упрощений. - RAM; Cj - некоторое время, a = sum(cj .... cjj)

 Очередное упрощение, называемое порядок роста (или скорость роста) брать только главный член формулы a*n^2. Потому что при больших n
"""


def insertion_sort(array):
    result = array[0:1]
    slozhnost = {'c1':0, 'c2':0,'c3':0}
    for i, a in enumerate(array[1:], start=1):
        slozhnost['c1'] += 1
        inserted = False
        for j, b in enumerate(result):
            slozhnost['c2'] += 1
            if a < b:
                result.insert(j, a)
                inserted = True
                break
        if not inserted:
            result.append(a)
    # print slozhnost
    return result

def selection_sort(array):
    """Сортировка выбором
    Сложность фиксирует все "шаги"
    """
    result = []
    slozhnost = {'c1': 0, 'c2': 0, 'c3': 0}
    for i, a in enumerate(array[:-1]):
        slozhnost['c1'] += 1
        m = 99999999
        for j, b in enumerate(array):

            slozhnost['c2'] += 1
            if b < m:
                m = b
        result.append(m)
        array.pop()
    # print slozhnost
    return result


def merge(a_list, b_list):
    res = []
    index = 0
    while a_list or b_list:
        if not a_list:
            res.extend(b_list)
            break
        elif not b_list:
            res.extend(a_list)
            break
        if a_list[index] < b_list[index]:
            res.append(a_list[index])
            a_list.remove(a_list[index])
        else:
            res.append(b_list[index])
            b_list.remove(b_list[index])
    return res

def merge_sort(array):
    l = len(array)
    if l == 1:
        return array
    first = array[:l/2]
    second = array[l/2:]
    res = merge(merge_sort(first), merge_sort(second))
    return res


def bubble_sort():
    pass


import timeit
import random
if __name__ == '__main__':

    general_setup = 'from copy import copy; import random;l = random.sample(range(10000), 500)'

    t = timeit.Timer('insertion_sort(copy(l))', setup='from glava2 import insertion_sort; ' + general_setup)
    print 'insertion_sort', t.timeit(100)

    t = timeit.Timer('selection_sort(copy(l))', setup='from glava2 import selection_sort;' + general_setup)
    print 'selection_sort', t.timeit(100)

    t = timeit.Timer('merge_sort(copy(l))', setup='from glava2 import merge_sort,merge;' + general_setup)
    print 'merge_sort', t.timeit(100)
