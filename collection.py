from collections import deque

stack = [1,2,3,4,5]

print(stack)

stack = deque(stack)


print(stack)

stack.append(6)

print(stack)

stack.pop()

print(stack)

#union of collections

x={1,2,3,4}
y={6,7,8,9}
z=x.union(y)

print (x,y,z)