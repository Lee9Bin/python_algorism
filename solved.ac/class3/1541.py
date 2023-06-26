import sys

susik = sys.stdin.readline()

result = 0
num = []
now = '+'
for i in susik:
    if now == '+':
        if i == '+' or i == '\n':
            a = ''.join(num)
            result += int(a)
            num = []
        elif i == '-':
            a = ''.join(num)
            result += int(a)
            num = []
            now ='-'
        else:
            num.append(i)
    elif now == '-':
        if i == '+' or i == '\n':
            a = ''.join(num)
            result -= int(a)
            num = []
        elif i == '-':
            a = ''.join(num)
            result -= int(a)
            num = []
            now ='-'
        else:
            num.append(i)
print(result)