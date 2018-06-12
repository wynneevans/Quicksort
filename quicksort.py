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
    i = lo - 1
    j = hi + 1
    while True:
        while True:
            j = j - 1
            if A[j] <= pivot:
                break
        while True:
            i = i + 1
            if A[i] >= pivot:
                break
        if i >= j:
            return j
        temp1 = A[j]
        A[j] = A[i]
        A[i] = temp1

input_A = []
input_B = []

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(prog='Something')
parser.add_argument("Integers", nargs='*', type=int)
args = parser.parse_args()
if len(args.Integers) < 1:
    input_A = [5, 3, 13, 4, 5, 3, 8, 11]
    print('''You can input your own list of integers if you like. For example: 
$ python3 quicksort.py 5 13 3 34 15 13 8 21\n''')
else:
    input_A = args.Integers

input_B = input_A

lomuto_quicksort(input_A, 0, len(input_A)-1)
hoare_quicksort(input_B, 0, len(input_B)-1)

print("Lomuto result: {}".format(input_A))
print("Hoare result: {}".format(input_B))