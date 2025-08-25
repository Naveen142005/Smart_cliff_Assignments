
#13. SEPARATING POSITIVE AND NEGATIVE NUMBERS IN A LIST

#reading input

N = int(input())
numbers = []
for _ in range(N):
    num = int(input())
    numbers.append(num)
positive_numbers = []
negative_numbers = []

# separating positive and negative numbers
for i in numbers:
    if i >= 0:
        positive_numbers.append(i)
    else:
        negative_numbers.append(i)
print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)