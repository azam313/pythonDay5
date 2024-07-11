collection = {1,2,2,2,"hello","world","world"}
coll = {1,3,4 ,2,"hello"}
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("azam")
collection.add((1,2,3))
collection.remove(1)
#collection.cleare() op:0
#print(collection.pop()) #it disply randon value from set
print(collection.union(coll))  #{1,2,3,4,"hello","world"}
print(collection.intersection(coll))  #common value
print(coll)
print(collection)
print(type(collection))
