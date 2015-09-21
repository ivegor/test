__author__ = 'air'
from time import time
from random import shuffle


def test_sort(alg, long, count):
    """
    :param alg: sort algorithm - function
    :param long:  length of array - int
    :param count: count of cycles - int
    :return: time of work - float
    """
    l = test_list = list(i for i in range(long))
    start = time()
    for i in range(count):
        shuffle(l)
        alg(l)
        if l != test_list:
            return "bad sort: must be\n %s but \n %s" % test_list, l
    finish = time()-start
    return finish