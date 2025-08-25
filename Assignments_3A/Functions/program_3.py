#Functions

#Find the smallest index with specific condition
def find_smallest_index(nums):
    for i in range(len(nums)):
        if i % 10 == nums[i]:
            return i
    return -1

def main():
    nums = list(map(int, input().split(',')))
    res = find_smallest_index(nums)
    print(res)

if __name__ == "__main__":
    main()
