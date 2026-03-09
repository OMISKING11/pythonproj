a = "00001"
b = "00010"
c = "00011"
d = "00100"
e = "00101"
f = "00110"
g = "00111"
h = "01000"
i = "01001"
j = "01010"
k = "01011"
l = "01100"
m = "01101"
n = "01110"
o = "01111"
p = "10000"
q = "10001"
r = "10010"
s = "10011"
t = "10100"
u = "10101"
v = "10110"
w = "10111"
x = "11000"
y = "11001"
z = "11010"
space = "00000"

s = str(input("Enter the code to get decoded: "))
chunks = [s[i:i+5] for i in range(0, len(s), 5)]
print(chunks)

A = 0
for i in chunks:
    if chunks[A] == "00001":
        chunks[A] = "a"
    if chunks[A] == "00010":
        chunks[A] = "b"
    if chunks[A] == "00011":
        chunks[A] = "c"
    if chunks[A] == "00100":
        chunks[A] = "d"
    if chunks[A] == "00101":
        chunks[A] = "e"
    if chunks[A] == "00110":
        chunks[A] = "f"
    if chunks[A] == "00111":
        chunks[A] = "g"
    if chunks[A] == "01000":
        chunks[A] = "h"
    if chunks[A] == "01001":
        chunks[A] = "i"
    if chunks[A] == "01010":
        chunks[A] = "j"
    if chunks[A] == "01011":
        chunks[A] = "k"
    if chunks[A] == "01100":
        chunks[A] = "l"
    if chunks[A] == "01101":
        chunks[A] = "m"
    if chunks[A] == "01110":
        chunks[A] = "n"
    if chunks[A] == "01111":
        chunks[A] = "o"
    if chunks[A] == "10000":
        chunks[A] = "p"
    if chunks[A] == "10001":
        chunks[A] = "q"
    if chunks[A] == "10010":
        chunks[A] = "r"
    if chunks[A] == "10011":
        chunks[A] = "s"
    if chunks[A] == "10100":
        chunks[A] = "t"
    if chunks[A] == "10101":
        chunks[A] = "u"
    if chunks[A] == "10110":
        chunks[A] = "v"
    if chunks[A] == "10111":
        chunks[A] = "w"
    if chunks[A] == "11000":
        chunks[A] = "x"
    if chunks[A] == "11001":
        chunks[A] = "y"
    if chunks[A] == "11010":
        chunks[A] = "z"
    if chunks[A] == "00000":
        chunks[A] = " "
    A += 1
print(chunks)