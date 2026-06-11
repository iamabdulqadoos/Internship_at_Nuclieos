# Filter Odd Numbers in a list Using Lambda Function 
List = [1,2,3,4,5,7,8,9,88,11,13,1,2,12,22,3,33]
lam =filter(lambda a: a % 2 !=0, List)
print(list(lam)) # This will print [1, 3, 5, 7, 9, 11, 13, 1, 2, 3, 33] because these are the odd numbers in the list.