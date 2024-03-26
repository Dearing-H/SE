# Standard Algorithms
# Accepted ways of solving
# Particular Problems

# # Liner Search 
def LinearSearch(arr):
    found = False
    i = 0 
    search_term = int(input())
    while found == False:
        if arr[i] == search_term:
            found = True
        i += 1
    return found

arr = [7, 4, 8, 18, 19, 5, 348, 
       6, 1400, 666, 9, 42]

print(LinearSearch(arr))

# Pythonic Way
# def shorter_linear(arr):
#     found = False
#     search_term = int(input())
#     for i in arr :
#         if i == search_term
#         found = True
#         break
#     return found 
# print(shorter_linear(arr))



# Binaty Search 
# Find min/max values
# Permutation sort
# Merge sort
# Selection


