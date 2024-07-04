#generators
def gen() :
   a=10
   yield a+1

x=gen()

print(next(x))
y=gen()
print(next(y))


#for i in range(10):
#   print(next(x))


