# 21. COUNT STRING

#Reading input
s = input().strip()
lower_count = 0
upper_count = 0
non_letters = 0

for ch in s:
    if ch.islower():
        lower_count += 1
    elif ch.isupper():
        upper_count += 1
    else:
        non_letters += 1

print("Lower case letters:", lower_count)
print("Upper case letters:", upper_count)
print("Non - letters:", non_letters)
