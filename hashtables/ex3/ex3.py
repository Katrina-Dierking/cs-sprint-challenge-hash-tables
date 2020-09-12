"""
    * create a list of lists with integers
    * find the intersection  
"""


def intersection(arrays):
    cache = {}
    result = []
    
    for array in arrays:
        for num in array:
            key = num
            if key not in cache:
                cache[key] = 1
            else: 
                cache[key] +=1
    
    for x in cache:
        if cache[x] > 1:
            result.append(x)
                

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
