# with open("binary", "bw") as bin_file:
#     bin_file.write(bytes(range(17))) # passed a list with single i to bytes()
#
# with open("binary", "br") as bin_file_2:
#     for b in bin_file_2:
#         print(b)

a = 65534   # FF FE
b = 65535   # FF FF
c = 65536   # 00 01 00 00
x = 2998302  # 02 2D C0 1E

# first number is number bytes of memory
with open("binary_2", "bw") as bin_file:
    bin_file.write(a.to_bytes(2, "big"))
    bin_file.write(b.to_bytes(2, "big"))  # big indian and little indian format
    bin_file.write(c.to_bytes(4, "big"))
    bin_file.write(x.to_bytes(4, "big"))
    bin_file.write(x.to_bytes(4, "little"))  # written in little indian format

with open("binary_2", "br") as bin_file:  # intentionally reusing name
    e = int.from_bytes(bin_file.read(2), "big")  # a
    print(e)
    f = int.from_bytes(bin_file.read(2), "big")  # b
    print(f)
    g = int.from_bytes(bin_file.read(4), "big")  # c
    print(g)
    h = int.from_bytes(bin_file.read(4), "big")  # x big indian
    print(h)
    i = int.from_bytes(bin_file.read(4), "big")  # x big indian, but trying to read in big, will error
    print(i)
