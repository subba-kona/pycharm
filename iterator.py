a=[1,2,3,4,5,6,7,8,9,10]
print(a[::-1])
a.reverse()
b=a[4::-1]
#making iterable
a=iter(a)
for i in range (5):
  print(a.__next__())

print(a.__sizeof__())
print(b)
