jabber = open("/Users/noahkawasaki/Desktop/Programs/Text Files/sample.txt", 'r')  # read mode

for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end="")

jabber.close()

print("=" * 40)
with open("/Users/noahkawasaki/Desktop/Programs/Text Files/sample.txt", 'r') as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end="")

print("=" * 40)
with open("/Users/noahkawasaki/Desktop/Programs/Text Files/sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end="")
        line = jabber.readline()

print("=" * 40)
# returns lines in a single list
# you can see the \n here in file itself, which is why we need end="" in print statement
# using with, you dont have to close the file
with open("/Users/noahkawasaki/Desktop/Programs/Text Files/sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines:
    print(line, end="")

print("=" * 40)
# reverses lines
with open("/Users/noahkawasaki/Desktop/Programs/Text Files/sample.txt", 'r') as jabber:
        lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end="")

print("=" * 40)
# reverses entire thing
with open("/Users/noahkawasaki/Desktop/Programs/Text Files/sample.txt", 'r') as jabber:
    lines = jabber.read()
print(lines)

for line in lines[::-1]:
    print(line, end="")