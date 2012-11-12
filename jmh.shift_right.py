def shift_right(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the right
    and shift the last item to the first position.

    Precondition: len(L) >= 1
    '''

    last_item = L[-1]

    # MISSING CODE GOES HERE
    for i in range(len(L) - 1):
        L[i] = L[i + 1]

    L[0] = last_item
