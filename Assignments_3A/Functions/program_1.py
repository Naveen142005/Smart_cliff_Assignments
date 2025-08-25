#Functions

def shuffle_list(nums, n):
    size = len(nums)
    i = 0
    j = size // 2
    res = []
    #Perform the shuffle operations
    while j < size:
        res.append(nums[i])
        res.append(nums[j])
        i += 1
        j += 1

    return res

def main():
    #Reading input
    n = int(input())
    nums = list(map(int, input().split(',')))
    #Calling function
    res = shuffle_list(nums, n)
    print(res)

if __name__ == "__main__":
    main()
