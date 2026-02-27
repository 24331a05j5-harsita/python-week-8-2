t1=(3,1,2,9)
t2=(8,7,6,2)
lst=[t1,t2]
def getlast(lst):
    return lst[-1]
lst1=sorted(lst,key=getlast)
print("sorted tuples: ",lst1)
