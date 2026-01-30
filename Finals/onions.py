n = int(input()) # No. of magic onions
onions = list(map(int, input().split()))
hp = 0
maxOnions = 0
positiveOns = 0
poshp = 0
negativeOns = 0
neghp = 0
leaveOnions = False

for q in range(n):
    if onions[q] >= 0:
        positiveOns += 1
        poshp += onions[q]
    else:
        negativeOns += 1
        neghp += onions[q]

diffhp = poshp + neghp
maxOnions = positiveOns

if diffhp < 0:
    leaveOnions = True

for o in range(n):
    # Can she eat 'o' number of onions?
    # She can eat as many onions as there are positive integers
    # She can eat more negative onions as long as hp >= 0
    # If all onions are negative, she can't eat any:
    if positiveOns == 0:
        break
    # If the onion is positive, add it to hp
    elif onions[o] >= 0:
        hp += onions[o]
    # If the onion is negative, check if it can be added to hp
    elif onions[o] < 0:
        if hp + onions[o] >= 0:
            hp += onions[o]
            maxOnions += 1

print(maxOnions)
print(leaveOnions)