# Logika bolean

# not and or xor

print("==========not==========")
x = False
z = not x
print("nilai z = ", z)


print("======== AND ========")
x = False
y = False
nilai = x and y
print(x, "and", y, "=", nilai)

x = False
y = True
nilai = x and y
print(x, "and", y, "=", nilai)

x = True
y = False
nilai = x and y
print(x, "and", y, "=", nilai)

x = True
y = True
nilai = x and y
print(x, "and", y, "=", nilai)

print ("======== OR ========")
x = True
y = False
nilai = x or y
print(x, "or" , y, "=", nilai)

x = True
y = True
nilai = x or y
print(x, "or" , y, "=", nilai)

x = False
y = False
nilai = x or y
print(x, "or" , y, "=", nilai)

x = False
y = True
nilai = x or y
print(x, "or" , y, "=", nilai)

print ("======== XOR ========")
x = True
y = False
nilai =(x or y) and not (x and y)
print({x, "xor" , y}, "=", nilai)

x = True
y = True
nilai =(x or y) and not (x and y)
print({x, "xor" , y}, "=", nilai)

x = False
y = False
nilai =(x or y) and not (x and y)
print({x, "xor" , y}, "=", nilai)

x = False
y = True
nilai =(x or y) and not (x and y)
print({x, "xor" , y}, "=", nilai)