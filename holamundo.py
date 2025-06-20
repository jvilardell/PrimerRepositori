# exemple de com ferlo servir

def mergesort(list):
    if len(list) < 2:
        return list
    else:
        middle = len(list) // 2
        left = mergesort(list[:middle])
        right = mergesort(list[middle:])
    return merge(left, right)

def merge(left, right):
    result = [ ]
    i ,j = 0, 0
    while(i < len(left) and j < len(right)):
        if (left[i] <= right[j]):
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    result += left[i:]
    result += right[j:]
    return result

print (mergesort ([2, 1, 4,3,5,9,10,6]))
print (mergesort ([300, 20, 304, 40, 2, 1, 9]))

# com estem