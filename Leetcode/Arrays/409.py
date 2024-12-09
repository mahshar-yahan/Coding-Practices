p = "abccccdd"

char_set = set()
length = 0

for char in p:
    if char in char_set:
        char_set.remove(char)
        length+=2
    else:
        char_set.add(char)

if char_set:
    length+=1

print(length)