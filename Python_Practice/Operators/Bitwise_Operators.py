a = 10
b = 20

print(type(a), id(a), a)
print(type(b), id(b), b)
print("Binary of a", bin(a))
print("Binary of b", bin(b))

c = 0

# and
c = a & b;
print('A and B', c, ":", bin(c))

# or
c = a | b;
print("A or B", c, ":", bin(c))

# Xor

c = a ^ b;
print("A xor B is", c, ":", bin(c))

#compliment

c = ~b;
print("B compliment",c,":",bin(c))

# left shift

c = a <<2;

print("A left shift",c,":",bin(c))

#right shift

c = a >>2;
print("A right shift",c,":",bin(c))