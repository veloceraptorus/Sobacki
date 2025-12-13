def count_of_myxac(m: int):
    for i in range(20):
        yield int(str(i)*1)*m
        yield int(str(i)*2)*m
        yield int(str(i)*3)*m
    
    
g = count_of_myxac(10)

for i in g:
    print(i)
