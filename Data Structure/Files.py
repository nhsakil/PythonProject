stuff= "Hello\nWorld!"
filename = open("mbox")
for line in filename:
    line = line.strip()
    if not "@" in line:
        continue
    print(line)
for line in filename:
    line = line.strip()
    if line.startswith('Now'):
        print(line)


fname = input("Enter the file name\n")
try:
    fileopen = open(fname)
except:
    print("File can't be open", filename)
    quit()

count = 0
for line in filename:
    if line.startswith("From"):
        count = count+1
print("There are total", count, "Subject line in", fileopen)
