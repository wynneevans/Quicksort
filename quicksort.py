import argparse

# Lomuto partition scheme
def lomuto_quicksort(A, lo, hi):
    if lo < hi:
        p = lomuto_partition(A, lo, hi)
        lomuto_quicksort(A, lo, p-1)
        lomuto_quicksort(A, p+1, hi)

def lomuto_partition(A, lo, hi):
    pivot = A[hi]
    i = lo - 1
    for j in range(lo, hi):
        if A[j] < pivot:
            i = i + 1
            temp1 = A[j]
            A[j] = A[i]
            A[i] = temp1

    temp2 = A[hi]
    A[hi] = A[i+1]
    A[i+1] = temp2
    return i + 1


# Hoare partition scheme
def hoare_quicksort(A, lo, hi):
    if lo < hi:
        p = hoare_partition(A, lo, hi)
        hoare_quicksort(A, lo, p)
        hoare_quicksort(A, p+1, hi)

def hoare_partition(A, lo, hi):
    pivot = A[lo]
    i = lo
    j = hi
    while True:
        print(i)
        while A[j] > pivot:
            j = j - 1
        while A[i] < pivot:
            i = i + 1
        if i >= j:
            return j
        temp1 = A[j]
        A[j] = A[i]
        A[i] = temp1


parser = argparse.ArgumentParser("Input some integers.")
parser.add_argument("Integers", nargs='+', type=int)
args = parser.parse_args()
input_A = args.Integers
input_B = input_A
lomuto_quicksort(input_A, 0, len(input_A)-1)
print(input_A)
hoare_quicksort(input_B, 0, len(input_B)-1)
print(input_B)