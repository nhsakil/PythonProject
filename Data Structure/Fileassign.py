# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:

    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    if line.startswith("X-DSPAM-Confidence:"):
        filedot = line.find(".")
        value = line[filedot - 1:]
        line = float(value)
        total = total+line
        count = count + 1

print("Average spam confidence:", total / count)
