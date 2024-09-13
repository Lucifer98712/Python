List = [1, True, 'Hello', 'Bye']
print(List)

if(List[1] == 'True'):
    print('Ok')

princeCastle = 'Killer Clown'
print(len(List)) 
print(List[1:len(List):2])
print(len(List))
List[1]=False
print(List)

#From pythons perspective lists are objects of data type list
print(type(List))

#List constructor: list(), it can also be used to create a list 
List2 = list(('True', 12, 34, False))
print(List2)

#-ve indexing
print(List2[-1])

#Range indexing
print(List2[1:])

if 34 in List2:
    print('Ok')
else:
    print('Not Ok')

#Changing items in the list    