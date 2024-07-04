

#list slicing
#list[Initial:End:Indexjump]

a=[1,2,3,4,5,6,7,8,9,10]

print("slicing")

print(a[::1]) #print all with step 1
print(a[::]) #print all with step 1(default)
print(a[0::1]) #print all with step 1, same as above 0 is default
print(a[0:10:1]) #print all with step 1, same as above 0 is default and 10(end) is default
print(a[1:10:1]) #print from 1  with step 1,
print(a[2:8:1]) #print from subscript 2(subscript 0,1,2) till subscript 7 with step 1
print(a[3:9:2]) #print from subscript 3(subscript 0,1,2,3) till 8
print(a[3:10:2]) #print from subscript 3(subscript 0,1,2,3) till 10(9)
print(a[2:9:2]) #print from subscript 3(subscript 0,1,2,3) till 8
print(a[3:9:1]) #print from subscript 3(subscript 0,1,2,3) till 8

#negative indexing

print("negative slicing")

print(a[-10:-1:1])
print(a[-10::1])
print(a[-1::1])

print("negative step")

print(a[::-1])
print(a[10::-1])

print(a[::-2])

print(a[::-3])

#modify lsit with slicing

print("modify lsit with slicing")

a[2:4] = [80,90,100,110,120]

print(a)





