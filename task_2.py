number_bushes = int(input("Enter number bushes: "))
n = []
i = 1

while i <= number_bushes:
    n.append(i)
    i +=1

print(sum([n[-1], n[-2], n[-3]]))