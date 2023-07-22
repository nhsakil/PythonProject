fname = input("Enter file name: ")
fh = open("fname")
lst = list()
for line in fh:
    line = line.strip()
    line = line.split()
    lst.append(line)
lst = [x for word in lst for x in word]
lst = set(lst)
print(sorted(lst))