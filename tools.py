def binsearch(item, array, beg, end):
    if beg >= end:
        return None
    mid = (beg + end)//2
    if array[mid] > item:
        return binsearch(item, array, beg, mid - 1)
    elif array[mid] < item:
        return binsearch(item, array, mid + 1, end)
    else:
        return mid
