def heapify(ls, i):
    i_left = 2*i + 1
    i_right = 2*i + 2
    n = len(ls)
    i_largest = i

    if i_left < n and ls[i_left] > ls[i_largest]:
        i_largest = i_left
    if i_right < n and ls[i_right] > ls[i_largest]:
        i_largest = i_right
    
    if i_largest != i:
        ls[i], ls[i_largest] = ls[i_largest], ls[i]
        heapify(ls, i_largest)
