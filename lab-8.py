def lengh_multiples(list):
    list1=[]
    for i,value in enumerate(list):
        list1.append(value * i )
    return list1
  

list1 = [1,2,3,4,5]
result1 = lengh_multiples (list1)
print(result1)


list1 = ["john","taylor","will","sean","ryan"]
result1 = lengh_multiples(list1)
print(result1)


