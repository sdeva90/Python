# cumilative sum of element in the list:
    output = [input[0]]
    for i in range(0, len(input)-1):
        s = output[i]+input[i+1]
        output.append(s)
    return output

assert solution([1,1,1]) == [1,2,3]
assert solution([1,-1,3]) == [1,0,3]
