n, max = map(int, input().split())
paras = []

for _ in range(n):
    para = list(map(str, input().split()))
    paras.append(para)

# Sample paras: [['Hello,', 'this', 'is', 'para1'], ['para2', 'starts'], ['para3', 'starts']]

outind = 0
lines = []
s = " "

while outind < n:
    insind = 0
    while insind < len(paras[outind]):
        length = len(paras[outind][insind])
        currentWord = paras[outind][insind]
        while insind < len(paras[outind]) - 1 and length + len(paras[outind][insind + 1]) + 1 <= max:
            insind += 1
            currentWord += s + paras[outind][insind]
            length = len(currentWord)
        lines.append(currentWord)
        insind += 1
    outind += 1


for i in range(len(lines)):
    if i != len(lines) - 1:
        if len(lines[i]) < max:
            spacesNeeded = max - len(lines[i])

        
        if spacesNeeded % 2 == 0:
            words = str(lines[i]).split()
            spacesBWEach = spacesNeeded//(len(words) - 1)
            lines[i] = (" "*(spacesBWEach + 1)).join(j for j in words)
        else:
            words = str(lines[i]).split()
            spacesBWEach1 = (spacesNeeded//(len(words)-1)) + 1
            spacesBWEach2 = (spacesNeeded//(len(words)-1)) 
            part = (" "*(spacesBWEach2 + 1)).join(words[k] for k in range(1, len(words)))
            lines[i] = words[0] + (" "*(spacesBWEach1 + 1)) + part
for h in lines:
    print(h)






'''
outind = 0
insind = 0
lines = []
s = " "
while outind < n:
    while insind < len(paras[outind]):
        length = len(paras[outind][insind])
        while length <= max and insind < n - 1:
            if length + len(paras[outind][insind + 1]) <= max:
                currentWord = paras[outind][insind] + s + paras[outind][insind + 1]
                length = len(currentWord)
            else:
                currentWord = paras[outind][insind]
        lines.append(currentWord)
        insind += 1
    outind += 1
print(lines)
'''