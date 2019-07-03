import random

#The searching function
def binary_search(sortedList, x):
    """Takes a sorted list and a key value and returns the position of the key value in the list.
        Raises an exception 'Element not found' if the value is absent in the list."""
    
    #start and end variables used to find the mid
    start = 0
    end = len(sortedList) - 1

    #If the element is present, the loop breaking condition is never met.
    while(start <= end):
        mid = int((start + end)/2)
        
        # Element found
        if (x == sortedList[mid]):
            return mid
        # Given value less than middle value
        elif(x < sortedList[mid]):
            end = mid - 1
        # Given value more than middle value
        else:
            start = mid + 1 
 
    raise Exception("Element not found")

#Used to run the program
if __name__ == '__main__':
    sampleList = list(range(10))
    try:
        sampleList.remove(random.randint(1,11))
        sampleList.remove(random.randint(1,11))
        sampleList.remove(random.randint(1,11))
    except:
        pass

    print("List : " + str(sampleList))
    key = int(input("Enter the element to search : "))
    print(binary_search(sampleList, key))
