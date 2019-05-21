"""Example of String Slicing """

s='Hello World'

print(s[:])   # s[:] >> this prints the entire string >> output >> Hello world
print(s[1:])  # s[1:] >> Starting from index 1, print the entire string s. >>Output :ello world
print(s[:3])  # s[:3] >> print all the values up to index < 3 in the string s ie first 3 indexes(0,1,2) >> output :Hel
print(s[1:3]) # Print from first index till 3nd index (<3)
print(s[:-1]) # Print complete string except the -1 index value Output>> Hello Worl
print(s[-3:]) # Print complete string till -3 index >> Output >> rld
print(s[-3:-1]) # print the string from -1 till -3 and exclude the value at -1 >>Output>> rl

#Zero based indexing.
print(s[::-1]) ## To print the string in reverse
print(s[::2]) # print the value of every 2nd index starting from 0
