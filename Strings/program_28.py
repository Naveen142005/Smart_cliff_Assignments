#28. DICTIONARY TO FIND MIRROR CHARACTERS IN A STRING

position = int(input())
if position <= 0:
    print("Invalid position, Position starting from 1..")
    exit()
s = input()
#storing the chat until the given position
val = s[:position - 1]

for i in range (position - 1 , len(s)):
    #mirror the char using ASCII
    val += chr(122 - ord(s[i]) + 97)

print(val)

