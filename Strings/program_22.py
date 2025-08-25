#22. MIXED STRING

#Reading input
s1 = input()
s2 = input()
s3 = ""
i = 0
j = len(s2) - 1

while i < len(s1) and j >= 0:
    #adding from front
    s3 += s1[i]
    #adding from back
    s3 += s2[j]
    i += 1
    j -= 1
#checking the edge cases
if j >= 0:
    s2 = s2[0:j][::-1]
    s3 += s2
if i < len(s1):
    s3 += s1[i:]

print(s3)