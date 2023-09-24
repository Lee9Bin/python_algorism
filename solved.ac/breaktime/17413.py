import sys
word = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(word):
    if word[i] == "<":
        i += 1 
        while word[i] != ">":
            i += 1 
        i += 1
    elif word[i] != " " and word[i] != "<" and word != ">":
        start = i
        while i < len(word) and word[i] != " " and word[i] != "<" and word != ">":
            i+=1
        tmp = word[start:i]
        tmp.reverse()
        word[start:i] = tmp
    else:
        i+=1

print("".join(word))