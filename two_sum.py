def twoSum(arr, tgt):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == tgt:
                return [i, j]


print(twoSum([3, 2, 4], 6))  # [1,2]
