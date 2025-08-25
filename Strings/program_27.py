#27. K’TH NON-REPEATING CHARACTER


string = input()
freq = [0] * 256
k = int(input())

#Getting frequency of each element
for i in string:
    if i != ' ':
        freq[ord(i) - 97] += 1

for i in string:
    if i == ' ': continue
   #Finding the kth non-repeating character
    if freq[ord(i) - 97] == 1:
        k -= 1

    if k == 0:
        print(i)
        break
else:
    print('No found')

