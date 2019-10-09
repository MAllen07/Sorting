# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    #[] []
    #[0,1,2, 3, 4, 5, 6, 7, 8, 9]

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    


    # TO-DO
    # test that we have an array of 1 or 0 then return the array

    #cut array in half
    middle =arr.length / 2 
    firstHalf= [0:middle]
    secondHalf = [middle:]

    # call merge_sort on  each half
    firstMerged = merge_sort(firstHalf)
    secondMerged = merge_sort(secondHalf)

    #call helper function merge to merge the two arrays 
    merge()
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
