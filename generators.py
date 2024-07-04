#generators
def gen() :
    yield 1
    yield 2
    yield 3
x=gen()

print(next(x))
y=gen()
print(next(y))

for i in gen() :
    print(i+4)



#for i in range(10):
#   print(next(x))


