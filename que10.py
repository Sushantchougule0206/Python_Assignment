#Q7.Take two integer values in a & b. Swap their values using tuple, using temparary variable and without tuple and without temparary variable.
a,b=10,23
tup=()

tup=a,b
b,a=tup
print(a,b)
