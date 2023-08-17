import sys
senten = sys.stdin.readline().rstrip()
boom = sys.stdin.readline().rstrip()

result = []

for i in senten:
    result.append(i)
    if len(result) >= len(boom):
        if ''.join(result[len(result)-len(boom):len(result)]) == boom:
            for k in range(len(boom)):
                result.pop()
if len(result) == 0:
    print("FRULA")
else:
    print(''.join(result))