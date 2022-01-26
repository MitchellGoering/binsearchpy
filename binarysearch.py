#binary search
#binary search works by selecting a value, select middle point in list, and see if value is higher, lower, or correct. 
#If higher or lower, narrow the list to that selection and repeat the search. 
#can be recursive or iterative

numberbank = [4, 5, 8, 13, 14, 16, 19, 22, 25, 26, 27, 28, 33, 37, 40, 41, 42, 88]  #array of numbers to search through
number_to_search = 16                                                                #choose which number to search

def binarySearch(numberbank, number_to_search):                                     #defining the function
    lower = 0                                                                       #lower half of the array, starts at index zero
    higher = len(numberbank) -1                                                     #higher half of the array, starts at index final number
    middle = 0                                                                      #middle of the array, starts at zero for manipulation

    while lower <= higher:                                                          #the while loop. starts by making sure lower is less than higher in order to make continuation criteria

        middle = (higher + lower) // 2                                              #this gets the middle index point of the array and sets middle to that

        if numberbank[middle] < number_to_search:                                   #if the number we search is higher than the middle value of the array, we set the lower bound for the next search to the middle plus one
            lower = middle + 1

        elif numberbank[middle] > number_to_search:                                 #if the number we search is lower than the middle value of the array, we set the upper bound for the next search to the middle minus one
            higher = middle -1

        else:                                                                       #if the number we search IS the middle value of the array, we return that index number
            return middle

    return -1                                                                       #if the number we search is not in the array, we return negative one to signal the output


result = binarySearch(numberbank, number_to_search)                                 #this is the result of the function defined as a variable

if result != -1:                                                                    #if the result is anything other than the negative one signal from line 27, we print the victory text
    print("The number you searched is in the list at index", str(result))
else:                                                                               #if the result is the negative one signal, we print the text saying the number is not in the array
    print("The number you searched is not in the list")

#the computational complexity for this iterative binary search is simple. The space complexity depends on how large the array is, which contributes to the total number of iterations the while loop goes through.
#this can be O(1) if the algorithm hits the number it's searching on the first try, or O(n^2) where n is something related to the array size.
#The time complexity also depends on the array size. It can be O(1) if the algorith hits on the first search, or O(log n) where n is something related to the array size.
