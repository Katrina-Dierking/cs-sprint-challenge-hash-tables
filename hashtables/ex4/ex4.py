"""
* set dict and list
* loop through list
"""

def has_negatives(a):
    nums = {}
    result = []
    
    for i in a:
        #if absolute value of nums exists, add it to the list
        if abs(i) in nums:
            result.append(abs(i))
        #if not, add it to the dict
        else:
            nums[abs(i)] = 1

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
