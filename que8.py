#Q4. Swap the following two tuples
tuple1 = (11, 22)
tuple2 = (99, 88)

v1,v2=tuple1
tuple1=tuple2
tuple2=v1,v2

print("tuple1:",tuple1)
print("tuple2:",tuple2)