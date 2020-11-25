"""
試著將一個班級有["Bill", "Doris", "Ace", "Carol", "Florence", "Ethan"]的list，
六個同學依照字母多寡，由少排至多印出，相同字母數的前後不拘，
所以結果會是=>["Ace", "Bill", "Doris", "Carol", "Ethan", "Florence"]
"""
names = ["Bill", "Doris", "Ace", "Carol", "Florence", "Ethan"]
print(names)
orderedNames = []

for i in range(len(names)):
    minName = names[0]
    for x in names:
        if len(minName) > len(x):
            minName = x
    orderedNames.append(minName)
    names.remove(minName)

print(orderedNames)
