'''n = int(input())
emails = []

for x in range(n):
    name = input().lower().replace("'", "").replace(" ", ".")
    emails.append(name)

for j in range(len(emails)):
    a = emails.count(emails[j])
    if a > 1:
        for r in range(a - 1):
            c = emails.index(emails[j], emails.index(emails[j]) + 1)
            emails[c] += str(r + 2)
    print(emails[j],end="@ucc.ie\n")      
'''

n = int(input())
emails = []
names = []
seenNames = {}  # key: name, value: number of occurences of this name

for _ in range(n):
    name = input().lower().replace("'", "").replace(" ", ".")
    names.append(name)

for x in names:
    count = seenNames.get(x, 0)
    seenNames[x] = count + 1

for y in seenNames:
    if seenNames[y] == 1:
        finalEmail = f"{y}@ucc.ie"
    else:

        finalEmail = f"{y}{seenNames[y]}@ucc.ie"
    print(finalEmail)

