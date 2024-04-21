#Tuple Assignment
#Q1.Add a list of elements to a given set
#Given:
sampleset = {"Yellow", "Orange", "Black"}
samplelist = ["Blue", "Green", "Red","Yellow","Orange"]

l1=list(sampleset)
samplelist=samplelist+l1
samplelist=set(samplelist)
print(samplelist)