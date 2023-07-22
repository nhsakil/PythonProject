
handel =open("romeo.txt")
counts  = dict()
for line in handel:
    words = line.strip().split()
    for word in words:
        counts[word] = counts.get(word, 0)+1

listofWords = list()
for key,value in counts.items():
    newTuple = (value, key)
    listofWords.append(newTuple)
print(listofWords)
listofWords = sorted(listofWords, reverse=True)
print(listofWords)

for value, key in listofWords[:10]:
    print(key, value)
    
print(sorted(([(value, key) for key, value in counts.items()])))
