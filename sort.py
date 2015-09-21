def bubble_sort(l):
    """
    l - list
    best O(n)
    worst, ave - O(n^2)

    """
    leng = len(l)
    change = False
    while leng > 1:
        for el in range(leng-1):
            if l[el] > l[el+1]:
                l[el], l[el+1] = l[el+1], l[el]
                change = True
        if not change: break
        leng -= 1


def select_sort(l):
    """
    l - list
    always O(n^2)
    """
    leng = len(l)
    while leng > 1:
        max_el = 0
        for i in range(1, leng):
            if l[max_el] < l[i]:
                max_el = i
            l[max_el], l[leng-1] = l[leng-1], l[max_el]
        leng -= 1


def insert_sort(l, start=0, gap=1):
    """
    l - list
    O(n^2)
    """
    for i in range(start+gap, len(l), gap):
        current = l[i]
        pos = i
        while (pos >= gap) and (current < l[pos-gap]):
            l[pos] = l[pos-gap]
            pos -= gap
        l[pos] = current


def shell_sort(l):
    """
    l - list
    with this increment ave O(n^(7/6)) worst O(n^(4/3))
    """
    def new_increment(a):
        """
        a - list
        algorithm by Sedgewick
        """
        results = [1]
        number = 0
        while len(a) > 3 * results[-1]:
            number += 1
            if number % 2:
                new = 8*(2**number) - 6*2**((number+1)/2) + 1
            else:
                new = 9*(2**number) - 9*2**(number/2) + 1
            results.append(int(new))
        results.reverse()
        return results

    for inc in new_increment(l):
        for i in range(inc):
            insert_sort(l, i, inc)


def merge_sort(l):
    """
    l - list
    O(n*log n)
    """

    if len(l) > 1:
        mid = len(l)//2
        left = l[:mid]
        right = l[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0     # index left list
        j = 0     # index right list
        k = 0     # index common list

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k] = left[i]
                i += 1
            else:
                l[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1

from random import randrange
def quick_sort(l, start=0, end="default"):
    """
    l - list
    ave O(n*log n) worst O(n^2)
    """
    if end == "default":
        end = len(l)
    if start < end:
        mid = randrange(start, end)
        right = start
        left = end-1
        while True:
            while right <= left and l[right] <= l[mid]:
                right += 1
            while left >= right and l[left] >= l[mid]:
                left -= 1
            if right > left:
                break
            else:
                l[right], l[left] = l[left], l[right]
        if mid > left:
            l[mid], l[left+1] = l[left+1], l[mid]
        else:
            l[mid], l[left] = l[left], l[mid]
        quick_sort(l, left+1, end)
        quick_sort(l, start, left)

if __name__ == "__main__":
    try:
        import test
        leng = 500
        cycle = 50
        print("Bubble:", test.test_sort(bubble_sort, leng, cycle))
        print("Select:", test.test_sort(select_sort, leng, cycle))
        print("Insert:", test.test_sort(insert_sort, leng, cycle))
        print("Shell:", test.test_sort(shell_sort, leng, cycle))
        print("Merge:", test.test_sort(merge_sort, leng, cycle))
        print("Quick:", test.test_sort(quick_sort, leng, cycle))
    except:
        alist = [1, 54, 26, 93, 17, 77, 31, 44, 55, 20]
        alist2 = [20, 30, 40, 90, 50, 60, 70, 80, 100]
        alist3 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        alist4 = [15, 5, 4, 18, 12, 19, 14, 10, 8, 20]
        alist5 = [5, 16, 20, 12, 3, 8, 9, 17, 19, 7]
        alist6 = [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]
        alist7 = [14, 17, 13, 15, 19, 10, 3, 16, 9, 12]
        bubble_sort(alist)
        bubble_sort(alist2)
        select_sort(alist3)
        insert_sort(alist4)
        shell_sort(alist5)
        merge_sort(alist6)
        quick_sort(alist7)
        print(alist)
        print(alist3)
        print(alist4)
        print(alist5)
        print(alist6)
        print(alist7)# data-structure
