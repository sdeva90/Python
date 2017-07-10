# to retun teh odd position value in teh list
def solution(input):
    output = []
    for i in range(1, len(input), 2):
        output.append(input[i])
    return(output)

assert solution([0,1,2,3,4,5]) == [1,3,5]
assert solution([1,-1,2,-2]) == [-1,-2]
