import urllib.request, urllib.parse, urllib.error

fileHandle = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

for line in fileHandle:
    print(line.decode().strip())

counts = dict()
for line in fileHandle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0)+1

print(counts)