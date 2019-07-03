import random

def binary_search(sortedList, x):
 
    start = 0
    end = len(sortedList) - 1

    while(start <= end):
        mid = (start + end)/2
        if (x == sortedList[mid]):
            return mid
        elif(x < sortedList[mid]):
            end = mid - 1
        else:
            start = mid + 1 
 
    raise Exception("Element not found")
    
if __name__ == '__main__':
    sampleList = list(range(10))
    try:
        sampleList.remove(random.randint(1,11))
        sampleList.remove(random.randint(1,11))
        sampleList.remove(random.randint(1,11))
    except:
        pass

    print("List : " + str(sampleList))
    key = input("Enter the element to search : ")
    print(binary_search(sampleList, key))
