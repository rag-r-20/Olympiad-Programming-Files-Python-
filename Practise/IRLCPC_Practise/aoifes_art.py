from math import ceil

c, w = map(int, input().split())
sentence = list(map(str, input().split()))
maxLength = 0
maxLengthIndex = 0
numStars = 2

for word in sentence:
    if len(word) > maxLength:
        maxLength = len(word)
        maxLengthIndex = sentence.index(word)

numStars += ceil(maxLength/2)
print(" ".join(["*" for _ in range(numStars)]))

newSentence = []
for s in range(len(sentence)):
    currentLength = 0
    if len(sentence[s]) < maxLength:
        currentLength = len(sentence[s])
        z = s
        while currentLength <= maxLength and z < len(sentence) - 1:
            potentialLength = len(sentence[z]+" "+sentence[z+1])
            if currentLength + potentialLength <= maxLength:
                print("in here")
                currentLength += potentialLength
                newWord = sentence[z] + " " + sentence[z+1]
                newSentence.append(newWord)
                z += 1
            else:
                print("What about here?")
                newSentence.append(sentence[z])
                z += 1
    else:
        print("over there")
        newSentence.append(sentence[s])

for l in newSentence:
    print("*", l, "*")

print(" ".join(["*" for _ in range(numStars)]))