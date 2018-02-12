oneTo10 =range(1,11)

def num_dub(num):
    return num*2
# use of map in function
print("use of function with map")
print(list(map(num_dub,oneTo10)))

#use of lambda with map
print("use of lambda with map")
print((list(map(lambda x:x*3,oneTo10))))

print(list(map(lambda x,y: x+y, [1,2,3,4],[2,3,4])))


print(list(filter(lambda x:x%2==0, range(1,11) )))