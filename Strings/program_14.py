#14. FINDING THE MEDIAN OF A LIST OF INTEGERS

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
numbers.sort()

#check if N is odd or even
if N % 2 == 1:
    # finding the median for odd N
    median = numbers[N // 2]
else:
    mid1 = numbers[N // 2 - 1]
    mid2 = numbers[N // 2]
    # findig the median for even N
    median = (mid1 + mid2) / 2

print(median)